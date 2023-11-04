import tvm
from tvm import relax, tir
from tvm.relax.backend.contrib.cutlass import partition_for_cutlass
from tvm.relax.dpl import (
    PatternContext,
    is_const,
    is_op,
    is_tuple_get_item,
    rewrite_bindings,
    rewrite_call,
    wildcard,
)
from tvm.script import relax as R


def simplify_div(f):
    """Fuse divides where possible."""
    lhs_pat = wildcard()
    rhs_pat = is_const()
    pattern = is_op("relax.divide")(lhs_pat, rhs_pat)

    def is_one(v):
        if isinstance(v, relax.expr.Constant) and v.data.numpy() == 1:
            return True
        return False

    def callback(orig, matchings):
        if is_one(matchings[rhs_pat]):
            return matchings[lhs_pat]
        return orig

    return rewrite_call(pattern, callback, f)


def simplify_stride_slice(f):
    """Remove any useless slices."""
    inp_pat = wildcard()
    pattern = is_op("relax.strided_slice")(inp_pat)

    def is_nop(v, begin, end, strides):
        shape = v.struct_info.shape
        for i in range(len(shape)):
            if begin[i] != 0 or end[i] != shape[i] or strides[i] != 1:
                return False
        return True

    def callback(orig, matchings):
        inp = matchings[inp_pat]
        if is_nop(inp, orig.attrs.begin, orig.attrs.end, orig.attrs.strides):
            return inp
        return orig

    return rewrite_call(pattern, callback, f)


def simplify_permute_dims(f):
    """Remove duplicate permute_dim operations."""
    inp_pat = wildcard()
    pattern = is_op("relax.permute_dims")(is_op("relax.permute_dims")(inp_pat))

    def callback(orig, matchings):
        before = matchings[inp_pat]
        after = matchings[pattern]
        before_shape = [int(s) for s in before.struct_info.shape]
        after_shape = [int(s) for s in after.struct_info.shape]
        if before_shape == after_shape:
            return before
        return orig

    f = rewrite_call(pattern, callback, f)

    inp_pat = wildcard()
    pattern2 = is_op("relax.permute_dims")(inp_pat)

    def callback2(orig, matchings):
        before = matchings[inp_pat]
        if hasattr(orig, "attrs") and [int(a) for a in orig.attrs.axes] == [0, 1, 2, 3]:
            return before
        return orig

    return rewrite_call(pattern2, callback2, f)


def simplify_reshape_permute(f):
    """Rewrite inefficient permute reshape pattern."""
    inp_pat = wildcard()
    shape_pat = wildcard()
    pattern = is_op("relax.permute_dims")(is_op("relax.reshape")(inp_pat, shape_pat))

    def callback(orig, matchings):
        shape = matchings[shape_pat]
        shape = [int(v) for v in shape.values]
        inp = matchings[inp_pat]

        if (
            len(inp.struct_info.shape) == 2
            and shape[0] == 1
            and shape[-2:] == [1, 1]
            and list(orig.attrs.axes) == [0, 2, 3, 1]
        ):
            return R.expand_dims(inp, [1, 2])
        return orig

    return rewrite_call(pattern, callback, f)


def simplify_expand_dims_permute(f):
    """Remove unnecessary extra expand dim operators."""
    inp_pat = wildcard()
    pattern = is_op("relax.permute_dims")(
        is_op("relax.expand_dims")(is_op("relax.expand_dims")(inp_pat))
    )

    def callback(orig, matchings):
        inp = matchings[inp_pat]

        if len(inp.struct_info.shape) == 2 and [int(a) for a in orig.attrs.axes] == [
            0,
            2,
            3,
            1,
        ]:
            return R.expand_dims(inp, [1, 2])
        return orig

    return rewrite_call(pattern, callback, f)


def rewrite_group_norm(f):
    """Rewrite any expanded group norm calls to a more efficient representation."""
    inp_pat = wildcard()
    eps_pat = wildcard()
    const2 = wildcard()
    const3 = wildcard()
    weight = wildcard()
    bias = wildcard()
    lv51 = is_op("relax.reshape")(inp_pat, wildcard())
    lv52 = is_op("relax.mean")(lv51)
    lv53 = is_op("relax.subtract")(lv51, lv52)
    lv54 = is_op("relax.variance")(lv51)
    lv55 = is_op("relax.add")(lv54, eps_pat)
    lv56 = is_op("relax.sqrt")(lv55)
    lv57 = is_op("relax.divide")(lv53, lv56)
    lv58 = is_op("relax.reshape")(const2, wildcard())
    lv59 = is_op("relax.multiply")(lv57, lv58)
    lv60 = is_op("relax.reshape")(const3, wildcard())
    lv61 = is_op("relax.add")(lv59, lv60)
    lv62 = is_op("relax.reshape")(lv61, wildcard())
    lv63 = is_op("relax.multiply")(lv62, weight)
    pattern = is_op("relax.add")(lv63, bias)

    def callback(orig, matchings):
        return R.nn.group_norm(
            matchings[inp_pat],
            R.squeeze(matchings[weight], [1, 2]),
            R.squeeze(matchings[bias], [1, 2]),
            num_groups=32,  # hardcoded for SDXL
            channel_axis=1,
            axes=[2, 3],
            epsilon=9.9999997473787516e-06,
        )

    return rewrite_call(pattern, callback, f)


def rewrite_silu(f):
    """Rewrite silu decomposition into a single op."""
    inp_pat = wildcard()
    pattern = is_op("relax.multiply")(inp_pat, is_op("relax.sigmoid")(inp_pat))

    def callback(orig, matchings):
        inp = matchings[inp_pat]
        return R.nn.silu(inp)

    return rewrite_call(pattern, callback, f)


def rewrite_geglu(f):
    """Rewrite any geglu patterns into a more efficient form."""
    inp_pat = wildcard()
    weight_pat = wildcard()
    bias_pat = wildcard()
    lv273 = is_op("relax.matmul")(inp_pat, weight_pat)
    lv274 = is_op("relax.add")(bias_pat, lv273)
    lv280 = is_op("relax.strided_slice")(lv274)
    lv_7 = is_op("relax.strided_slice")(lv274)
    lv281 = is_op("relax.nn.gelu")(lv_7)
    pattern = is_op("relax.multiply")(lv280, lv281)

    def callback(orig, matchings):
        inp = matchings[inp_pat]
        weight = matchings[weight_pat]
        bias = matchings[bias_pat]
        dim_out = int(weight.struct_info.shape[-1]) // 2
        weight1 = R.strided_slice(
            weight, axes=[1], begin=[0], end=[dim_out], strides=[1]
        )
        weight2 = R.strided_slice(
            weight, axes=[1], begin=[dim_out], end=[dim_out * 2], strides=[1]
        )
        bias1 = R.strided_slice(bias, axes=[0], begin=[0], end=[dim_out], strides=[1])
        bias2 = R.strided_slice(
            bias, axes=[0], begin=[dim_out], end=[dim_out * 2], strides=[1]
        )
        matmul1 = R.add(R.matmul(inp, weight1), bias1)
        matmul2 = R.add(R.matmul(inp, weight2), bias2)
        return R.multiply(matmul1, R.nn.gelu(matmul2))

    return rewrite_call(pattern, callback, f)


def rewrite_gelu(f):
    """Simplify any expanded gelu operations."""
    inp_pat = wildcard()
    lv276 = is_op("relax.divide")(inp_pat, wildcard())
    lv277 = is_op("relax.erf")(lv276)
    lv278 = is_op("relax.add")(lv277, wildcard())
    lv279 = is_op("relax.multiply")(inp_pat, lv278)
    pattern = is_op("relax.multiply")(lv279, wildcard())

    def callback(orig, matchings):
        inp = matchings[inp_pat]
        return R.nn.gelu(inp)

    return rewrite_call(pattern, callback, f)


def combine_expand_dims(f, num_branches):
    """Fuse any duplicated expand dim operations."""
    with PatternContext() as ctx:
        inp_pat = wildcard()
        split_pat = is_op("relax.split")(inp_pat)
        expand_dims_patterns = []

        for i in range(num_branches):
            tensor = is_tuple_get_item(split_pat, i)
            split_pat.used_by(tensor)
            expand_dims_patterns.append(is_op("relax.expand_dims")(tensor))

    def rewriter(matchings, bindings):
        inp = matchings[inp_pat]
        split = matchings[split_pat]
        expand = R.expand_dims(inp, [1, 2])
        sections = bindings[split].attrs.indices_or_sections
        new_split = R.split(expand, sections, -1)

        replacements = {}
        for i, expand_dims_pat in enumerate(expand_dims_patterns):
            replacements[matchings[expand_dims_pat]] = new_split[i]

        return replacements

    return rewrite_bindings(ctx, rewriter, f)


def get_rewrite_pass():
    """Compose the full set of rewriting passes."""

    @tvm.transform.module_pass(opt_level=0)
    def rewrite_passes(mod, _):
        # Remove div by 1
        mod["main"] = simplify_div(mod["main"])
        # # Remove nop transpose -> transpose
        mod["main"] = simplify_permute_dims(mod["main"])
        # Remove nop strided slice
        mod["main"] = simplify_stride_slice(mod["main"])
        # Simplify reshape / expand_dims -> permute into equivalent expand_dims
        # This is necessary for combine_expand_dims below
        mod["main"] = simplify_reshape_permute(mod["main"])
        mod["main"] = simplify_expand_dims_permute(mod["main"])

        mod["main"] = rewrite_silu(mod["main"])
        mod["main"] = rewrite_gelu(mod["main"])
        mod["main"] = rewrite_geglu(mod["main"])

        # Ignore branches with two matmuls, since one of the branches involves
        # GeLU activation which is much faster on CUTLASS but will be computed by
        # TVM if two matmuls are combined
        mod = relax.transform.CombineParallelMatmul(lambda *inp: len(inp[1]) > 2)(mod)
        # Combine individual expand_dims that follow the combined matmul + split by
        # rewriting split -> tuple_get -> expand_dims into split ->
        # combined expand_dims -> tuple_get.
        # This lets us eliminate additional kernel launches for all expand_dims.
        mod["main"] = combine_expand_dims(mod["main"], 22)
        mod["main"] = combine_expand_dims(mod["main"], 17)  # for XL
        mod["main"] = combine_expand_dims(mod["main"], 10)  # for controlnet

        return mod

    return rewrite_passes


def rewrite_attention(f):
    def BSNH_to_BSH(tensor):
        return is_op("relax.reshape")(is_op("relax.permute_dims")(tensor), wildcard())

    def BSH_to_BSNH(tensor):
        return is_op("relax.permute_dims")(is_op("relax.reshape")(tensor, wildcard()))

    Q = wildcard()
    K = wildcard()
    V = wildcard()

    Q_3D = BSNH_to_BSH(Q)
    V_3D = BSNH_to_BSH(V)
    K_3D = BSNH_to_BSH(K)

    matmul1 = is_op("relax.matmul")(Q_3D, is_op("relax.permute_dims")(K_3D))
    multiply = is_op("relax.multiply")(matmul1, is_const())
    softmax = is_op("relax.nn.softmax")(multiply)
    matmul2 = is_op("relax.matmul")(softmax, V_3D)

    pattern = BSH_to_BSNH(matmul2)

    def callback(_, matchings):
        return R.nn.attention(matchings[Q], matchings[K], matchings[V])

    return rewrite_call(pattern, callback, f)


def simplify_div(f):
    lhs_pat = wildcard()
    rhs_pat = is_const()
    pattern = is_op("relax.divide")(lhs_pat, rhs_pat)

    def is_one(v):
        if isinstance(v, relax.expr.Constant) and v.data.numpy() == 1:
            return True
        return False

    def callback(orig, matchings):
        if is_one(matchings[rhs_pat]):
            return matchings[lhs_pat]
        return orig

    return rewrite_call(pattern, callback, f)


def simplify_stride_slice(f):
    inp_pat = wildcard()
    pattern = is_op("relax.strided_slice")(inp_pat)

    def is_nop(v, begin, end, strides):
        shape = v.struct_info.shape
        for i in range(len(shape)):
            if (
                begin is None
                or end is None
                or strides is None
                or begin[i] != 0
                or end[i] != shape[i]
                or strides[i] != 1
            ):
                return False
        return True

    def callback(orig, matchings):
        inp = matchings[inp_pat]
        if hasattr(orig, "attrs") and is_nop(
            inp, orig.attrs.begin, orig.attrs.end, orig.attrs.strides
        ):
            return inp
        return orig

    return rewrite_call(pattern, callback, f)


def simplify_permute_dims(f):
    inp_pat = wildcard()
    pattern = is_op("relax.permute_dims")(is_op("relax.permute_dims")(inp_pat))

    def callback(orig, matchings):
        before = matchings[inp_pat]
        after = matchings[pattern]
        before_shape = [int(s) for s in before.struct_info.shape]
        after_shape = [int(s) for s in after.struct_info.shape]
        if before_shape == after_shape:
            return before
        return orig

    return rewrite_call(pattern, callback, f)


def simplify_reshape_permute(f):
    inp_pat = wildcard()
    shape_pat = wildcard()
    pattern = is_op("relax.permute_dims")(is_op("relax.reshape")(inp_pat, shape_pat))

    def callback(orig, matchings):
        shape = matchings[shape_pat]
        shape = [int(v) for v in shape.values]
        inp = matchings[inp_pat]

        if (
            len(inp.struct_info.shape) == 2
            and shape[0] == 1
            and shape[-2:] == [1, 1]
            and list(orig.attrs.axes) == [0, 2, 3, 1]
        ):
            return R.expand_dims(inp, [1, 2])
        return orig

    return rewrite_call(pattern, callback, f)


def combine_expand_dims(f, num_branches):
    with PatternContext() as ctx:
        inp_pat = wildcard()
        split_pat = is_op("relax.split")(inp_pat)
        expand_dims_patterns = []

        for i in range(num_branches):
            tensor = is_tuple_get_item(split_pat, i)
            split_pat.used_by(tensor)
            expand_dims_patterns.append(is_op("relax.expand_dims")(tensor))

    def rewriter(matchings, bindings):
        inp = matchings[inp_pat]
        split = matchings[split_pat]
        expand = R.expand_dims(inp, [1, 2])
        sections = bindings[split].attrs.indices_or_sections
        new_split = R.split(expand, sections, -1)

        replacements = {}
        for i, expand_dims_pat in enumerate(expand_dims_patterns):
            replacements[matchings[expand_dims_pat]] = new_split[i]

        return replacements

    return rewrite_bindings(ctx, rewriter, f)


def get_rewrite_pass(combine_matmul=False):
    @tvm.transform.module_pass(opt_level=0)
    def rewrite_passes(mod, _):
        # Remove div by 1
        mod["main"] = simplify_div(mod["main"])
        # Remove nop transpose -> transpose
        mod["main"] = simplify_permute_dims(mod["main"])
        # Remove nop strided slice
        mod["main"] = simplify_stride_slice(mod["main"])
        # Simplify reshape -> permute into equivalent expand_dims
        # This is necessary for combine_expand_dims below
        mod["main"] = simplify_reshape_permute(mod["main"])

        if combine_matmul:
            # Ignore branches with two matmuls, since one of the branches involves
            # GeLU activation which is much faster on CUTLASS but will be computed by
            # TVM if two matmuls are combined
            check = lambda *inp: len(inp[1]) > 2
            mod = relax.transform.CombineParallelMatmul(check)(mod)
            # Combine individual expand_dims that follow the combined matmul + split by
            # rewriting split -> tuple_get -> expand_dims into split -> combined expand_dims -> tuple_get.
            # This lets us eliminate additional kernel launches for all expand_dims.
            mod["main"] = combine_expand_dims(mod["main"], 22)
            mod["main"] = combine_expand_dims(mod["main"], 10)  # for controlnet

        return mod

    return rewrite_passes


def run_opt_passes(mod, params=None, fp16_input_names=None, combine_matmul=False):
    passes = [
        relax.transform.EliminateCommonSubexpr(),
        relax.transform.CanonicalizeBindings(),
        relax.transform.ConvertLayout({"relax.nn.conv2d": ["NHWC", "OHWI"]}),
        get_rewrite_pass(combine_matmul),  # error
        relax.transform.DeadCodeElimination(["main"]),
    ]

    if params:
        passes += [
            relax.transform.BindParams("main", params),
            relax.transform.FoldConstant(),
            relax.transform.ToMixedPrecision(out_dtype="float16"),
        ]
    else:
        passes += [
            relax.transform.FoldConstant(),
            # relax.transform.ToMixedPrecision(
            #     out_dtype="float16", fp16_input_names=fp16_input_names
            # ),
        ]
        """
              File "/home/ubuntu/tvm/src/relax/transform/infer_amp_utils.cc", line 28
              InternalError: Check failed: (tensor) is false: Expected TensorStructInfo, but got R.Objec
        """,

    return tvm.transform.Sequential(passes)(mod)


def offload_to_cutlass(mod, target):
    # Currently, sm86 is not supported.
    sm = int(target.arch.split("_")[1])
    print("offload_to_cutlass sm: ", sm)
    if sm > 80:
        sm = 80
    mod = partition_for_cutlass(mod)
    mod = relax.transform.RunCodegen(
        {"cutlass": {"sm": sm, "find_first_valid": False}}
    )(mod)
    return mod


def run_lower_passes(mod, target, do_tuning=True):
    passes = [relax.pipeline.get_pipeline()]

    if "cuda" in target.kind.name:
        work_dir = "logs"
        with target:
            if do_tuning:
                passes.append(
                    relax.transform.MetaScheduleTuneIRMod(
                        params={},
                        work_dir=work_dir,
                        max_trials_global=1400,
                        max_trials_per_task=50,
                    )
                )
            passes.append(relax.transform.MetaScheduleApplyDatabase(work_dir))
            passes.append(tir.transform.DefaultGPUSchedule())

    with target, tvm.transform.PassContext(opt_level=3):
        return tvm.transform.Sequential(passes)(mod)


def generate_params(params_list, param_names, dst_path):
    params_dict = {}

    for i, name in enumerate(param_names):
        params_dict[name + f"_{i}"] = tvm.nd.array(
            params_list[i].numpy().astype("float16")
        )

    tvm.runtime.save_param_dict_to_file(params_dict, dst_path)


def compile(mod_in, param_names, model_name, prefix, target, do_tuning):
    # Create an irmodule with properly named entry function.
    mod = tvm.ir.IRModule()

    mod["main"] = mod_in[model_name]
    # Apply optimization passes.
    mod = run_opt_passes(mod, combine_matmul=True, fp16_input_names=param_names)
    mod = offload_to_cutlass(mod, target)
    mod = run_lower_passes(mod, target, do_tuning=do_tuning)

    # Generate parameter optimization function
    mod = relax.transform.LiftTransformParams()(mod)

    # Compile and save library.
    ex = relax.build(mod, target)
    ex.export_library(f"{prefix}/{model_name}_no_params.so")
