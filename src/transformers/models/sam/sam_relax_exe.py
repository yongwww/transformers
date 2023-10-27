@get_image_embeddings:
  call  vm.builtin.check_tensor_info in: %0, i4, c[0], c[1] dst: %void
  call  vm.builtin.match_shape in: %0, %void, i4, i0, i1, i0, i3, i0, i1024, i0, i1024, c[1] dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[2], i0, c[3], c[4] dst: %315
  call  vm.builtin.alloc_tensor in: %315, i0, c[5], c[6] dst: %316
  call  conv2d           in: %0, %2, %316 dst: %void
  call  vm.builtin.reshape in: %3, c[7]     dst: %317
  call  vm.builtin.alloc_storage in: %vm, c[8], i0, c[9], c[4] dst: %318
  call  vm.builtin.alloc_tensor in: %318, i0, c[5], c[10] dst: %319
  call  add              in: %316, %317, %319 dst: %void
  call  vm.builtin.null_value in:              dst: %317
  call  vm.builtin.null_value in:              dst: %316
  call  vm.builtin.alloc_tensor in: %315, i0, c[11], c[12] dst: %320
  call  transpose        in: %319, %320   dst: %void
  call  vm.builtin.null_value in:              dst: %319
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[13] dst: %321
  call  add1             in: %320, %4, %321 dst: %void
  call  vm.builtin.null_value in:              dst: %320
  call  vm.builtin.alloc_tensor in: %315, i0, c[11], c[14] dst: %322
  call  layer_norm       in: %321, %5, %6, %322 dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[15], i0, c[16], c[4] dst: %323
  call  vm.builtin.alloc_tensor in: %323, i0, c[17], c[18] dst: %324
  call  pad              in: %322, %324   dst: %void
  call  vm.builtin.null_value in:              dst: %322
  call  vm.builtin.reshape in: %324, c[19]  dst: %325
  call  vm.builtin.alloc_tensor in: %315, i0, c[20], c[21] dst: %326
  call  transpose1       in: %325, %326   dst: %void
  call  vm.builtin.null_value in:              dst: %324
  call  vm.builtin.null_value in:              dst: %325
  call  vm.builtin.reshape in: %326, c[22]  dst: %327
  call  vm.builtin.alloc_tensor in: %323, i0, c[23], c[24] dst: %328
  call  transpose2       in: %7, %328     dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[8], i0, c[25], c[4] dst: %329
  call  vm.builtin.alloc_tensor in: %329, i0, c[26], c[27] dst: %330
  call  matmul           in: %327, %328, %330 dst: %void
  call  vm.builtin.null_value in:              dst: %326
  call  vm.builtin.null_value in:              dst: %327
  call  vm.builtin.null_value in:              dst: %328
  call  vm.builtin.alloc_tensor in: %323, i0, c[26], c[28] dst: %331
  call  add2             in: %330, %8, %331 dst: %void
  call  vm.builtin.null_value in:              dst: %330
  call  vm.builtin.reshape in: %331, c[29]  dst: %332
  call  vm.builtin.alloc_tensor in: %329, i0, c[30], c[31] dst: %333
  call  transpose3       in: %332, %333   dst: %void
  call  vm.builtin.null_value in:              dst: %331
  call  vm.builtin.null_value in:              dst: %332
  call  vm.builtin.reshape in: %333, c[32]  dst: %334
  call  vm.builtin.alloc_tensor in: %315, i0, c[33], c[34] dst: %335
  call  vm.builtin.alloc_tensor in: %323, i0, c[33], c[35] dst: %336
  call  vm.builtin.alloc_storage in: %vm, c[8], i0, c[36], c[4] dst: %337
  call  vm.builtin.alloc_tensor in: %337, i0, c[33], c[37] dst: %338
  call  split            in: %334, %335, %336, %338 dst: %void
  call  vm.builtin.null_value in:              dst: %333
  call  vm.builtin.null_value in:              dst: %334
  call  vm.builtin.make_tuple in: %335, %336, %338 dst: %339
  call  vm.builtin.reshape in: %335, c[38]  dst: %340
  call  vm.builtin.reshape in: %336, c[38]  dst: %341
  call  vm.builtin.reshape in: %338, c[38]  dst: %342
  call  vm.builtin.alloc_tensor in: %329, i0, c[38], c[39] dst: %343
  call  multiply         in: %340, %343   dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[8], i0, c[40], c[4] dst: %344
  call  vm.builtin.alloc_tensor in: %344, i0, c[41], c[42] dst: %345
  call  transpose4       in: %341, %345   dst: %void
  call  vm.builtin.null_value in:              dst: %336
  call  vm.builtin.null_value in:              dst: %341
  call  vm.builtin.alloc_tensor in: %323, i0, c[43], c[44] dst: %346
  call  matmul1          in: %343, %345, %346 dst: %void
  call  vm.builtin.null_value in:              dst: %343
  call  vm.builtin.null_value in:              dst: %345
  call  vm.builtin.reshape in: %11, c[45]   dst: %347
  call  vm.builtin.alloc_storage in: %vm, c[46], i0, c[47], c[4] dst: %348
  call  vm.builtin.alloc_tensor in: %348, i0, c[48], c[49] dst: %349
  call  transpose5       in: %347, %349   dst: %void
  call  vm.builtin.null_value in:              dst: %347
  call  vm.builtin.reshape in: %349, c[50]  dst: %350
  call  vm.builtin.alloc_storage in: %vm, c[46], i0, c[51], c[4] dst: %351
  call  vm.builtin.alloc_tensor in: %351, i0, c[52], c[53] dst: %352
  call  transpose6       in: %350, %352   dst: %void
  call  vm.builtin.null_value in:              dst: %349
  call  vm.builtin.null_value in:              dst: %350
  call  vm.builtin.reshape in: c[54], c[55] dst: %353
  call  vm.builtin.reshape in: %353, c[55]  dst: %354
  call  vm.builtin.null_value in:              dst: %353
  call  vm.builtin.reshape in: c[54], c[56] dst: %355
  call  vm.builtin.reshape in: %355, c[56]  dst: %356
  call  vm.builtin.null_value in:              dst: %355
  call  vm.builtin.alloc_storage in: %vm, c[57], i0, c[58], c[4] dst: %357
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[60] dst: %358
  call  subtract         in: %354, %356, %358 dst: %void
  call  vm.builtin.null_value in:              dst: %354
  call  vm.builtin.null_value in:              dst: %356
  call  vm.builtin.alloc_storage in: %vm, c[57], i0, c[61], c[4] dst: %359
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[62] dst: %360
  call  add3             in: %358, %360   dst: %void
  call  vm.builtin.null_value in:              dst: %358
  call  vm.builtin.alloc_tensor in: %348, i0, c[63], c[64] dst: %361
  call  take             in: %352, %360, %361 dst: %void
  call  vm.builtin.null_value in:              dst: %352
  call  vm.builtin.null_value in:              dst: %360
  call  vm.builtin.reshape in: %12, c[45]   dst: %362
  call  vm.builtin.alloc_tensor in: %351, i0, c[48], c[65] dst: %363
  call  transpose5       in: %362, %363   dst: %void
  call  vm.builtin.null_value in:              dst: %362
  call  vm.builtin.reshape in: %363, c[50]  dst: %364
  call  vm.builtin.alloc_storage in: %vm, c[66], i0, c[67], c[4] dst: %365
  call  vm.builtin.alloc_tensor in: %365, i0, c[52], c[68] dst: %366
  call  transpose6       in: %364, %366   dst: %void
  call  vm.builtin.null_value in:              dst: %363
  call  vm.builtin.null_value in:              dst: %364
  call  vm.builtin.reshape in: c[54], c[55] dst: %367
  call  vm.builtin.reshape in: %367, c[55]  dst: %368
  call  vm.builtin.null_value in:              dst: %367
  call  vm.builtin.reshape in: c[54], c[56] dst: %369
  call  vm.builtin.reshape in: %369, c[56]  dst: %370
  call  vm.builtin.null_value in:              dst: %369
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[69] dst: %371
  call  subtract         in: %368, %370, %371 dst: %void
  call  vm.builtin.null_value in:              dst: %368
  call  vm.builtin.null_value in:              dst: %370
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[70] dst: %372
  call  add3             in: %371, %372   dst: %void
  call  vm.builtin.null_value in:              dst: %371
  call  vm.builtin.alloc_tensor in: %351, i0, c[63], c[71] dst: %373
  call  take             in: %366, %372, %373 dst: %void
  call  vm.builtin.null_value in:              dst: %366
  call  vm.builtin.null_value in:              dst: %372
  call  vm.builtin.reshape in: %340, c[72]  dst: %374
  call  vm.builtin.alloc_tensor in: %344, i0, c[73], c[74] dst: %375
  call  einsum           in: %374, %361, %375 dst: %void
  call  vm.builtin.null_value in:              dst: %361
  call  vm.builtin.alloc_tensor in: %329, i0, c[73], c[75] dst: %376
  call  einsum1          in: %374, %373, %376 dst: %void
  call  vm.builtin.null_value in:              dst: %335
  call  vm.builtin.null_value in:              dst: %340
  call  vm.builtin.null_value in:              dst: %374
  call  vm.builtin.null_value in:              dst: %373
  call  vm.builtin.reshape in: %346, c[76]  dst: %377
  call  vm.builtin.reshape in: %375, c[77]  dst: %378
  call  vm.builtin.reshape in: %376, c[78]  dst: %379
  call  vm.builtin.alloc_tensor in: %315, i0, c[76], c[79] dst: %380
  call  add4             in: %377, %378, %380 dst: %void
  call  vm.builtin.null_value in:              dst: %346
  call  vm.builtin.null_value in:              dst: %377
  call  vm.builtin.null_value in:              dst: %375
  call  vm.builtin.null_value in:              dst: %378
  call  vm.builtin.alloc_tensor in: %323, i0, c[76], c[80] dst: %381
  call  add5             in: %380, %379, %381 dst: %void
  call  vm.builtin.null_value in:              dst: %380
  call  vm.builtin.null_value in:              dst: %376
  call  vm.builtin.null_value in:              dst: %379
  call  vm.builtin.reshape in: %381, c[43]  dst: %382
  call  vm.builtin.alloc_tensor in: %315, i0, c[43], c[81] dst: %383
  call  softmax          in: %382, %383   dst: %void
  call  vm.builtin.null_value in:              dst: %381
  call  vm.builtin.null_value in:              dst: %382
  call  vm.builtin.alloc_tensor in: %344, i0, c[38], c[82] dst: %384
  call  matmul2          in: %383, %342, %384 dst: %void
  call  vm.builtin.null_value in:              dst: %383
  call  vm.builtin.null_value in:              dst: %338
  call  vm.builtin.null_value in:              dst: %342
  call  vm.builtin.reshape in: %384, c[83]  dst: %385
  call  vm.builtin.alloc_tensor in: %337, i0, c[84], c[85] dst: %386
  call  transpose7       in: %385, %386   dst: %void
  call  vm.builtin.null_value in:              dst: %384
  call  vm.builtin.null_value in:              dst: %385
  call  vm.builtin.reshape in: %386, c[22]  dst: %387
  call  vm.builtin.alloc_tensor in: %344, i0, c[86], c[87] dst: %388
  call  transpose8       in: %9, %388     dst: %void
  call  vm.builtin.alloc_tensor in: %329, i0, c[22], c[88] dst: %389
  call  matmul3          in: %387, %388, %389 dst: %void
  call  vm.builtin.null_value in:              dst: %386
  call  vm.builtin.null_value in:              dst: %387
  call  vm.builtin.null_value in:              dst: %388
  call  vm.builtin.alloc_tensor in: %337, i0, c[22], c[89] dst: %390
  call  add6             in: %389, %10, %390 dst: %void
  call  vm.builtin.null_value in:              dst: %389
  call  vm.builtin.reshape in: %390, c[20]  dst: %391
  call  vm.builtin.alloc_tensor in: %344, i0, c[19], c[90] dst: %392
  call  transpose9       in: %391, %392   dst: %void
  call  vm.builtin.null_value in:              dst: %390
  call  vm.builtin.null_value in:              dst: %391
  call  vm.builtin.reshape in: %392, c[17]  dst: %393
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[91] dst: %394
  call  strided_slice    in: %393, %394   dst: %void
  call  vm.builtin.null_value in:              dst: %392
  call  vm.builtin.null_value in:              dst: %393
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[92] dst: %395
  call  add1             in: %321, %394, %395 dst: %void
  call  vm.builtin.null_value in:              dst: %321
  call  vm.builtin.null_value in:              dst: %394
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[93] dst: %396
  call  layer_norm       in: %395, %13, %14, %396 dst: %void
  call  vm.builtin.alloc_tensor in: %337, i0, c[94], c[95] dst: %397
  call  transpose10      in: %15, %397    dst: %void
  call  vm.builtin.alloc_tensor in: %315, i0, c[96], c[97] dst: %398
  call  matmul4          in: %396, %397, %398 dst: %void
  call  vm.builtin.null_value in:              dst: %396
  call  vm.builtin.null_value in:              dst: %397
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[98] dst: %399
  call  add7             in: %398, %16, %399 dst: %void
  call  vm.builtin.null_value in:              dst: %398
  call  vm.builtin.alloc_tensor in: %315, i0, c[96], c[99] dst: %400
  call  gelu             in: %399, %400   dst: %void
  call  vm.builtin.null_value in:              dst: %399
  call  vm.builtin.alloc_tensor in: %318, i0, c[100], c[101] dst: %401
  call  transpose11      in: %17, %401    dst: %void
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[102] dst: %402
  call  matmul5          in: %400, %401, %402 dst: %void
  call  vm.builtin.null_value in:              dst: %400
  call  vm.builtin.null_value in:              dst: %401
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[103] dst: %403
  call  add8             in: %402, %18, %403 dst: %void
  call  vm.builtin.null_value in:              dst: %402
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[104] dst: %404
  call  add1             in: %395, %403, %404 dst: %void
  call  vm.builtin.null_value in:              dst: %395
  call  vm.builtin.null_value in:              dst: %403
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[105] dst: %405
  call  layer_norm       in: %404, %19, %20, %405 dst: %void
  call  vm.builtin.alloc_tensor in: %344, i0, c[17], c[106] dst: %406
  call  pad              in: %405, %406   dst: %void
  call  vm.builtin.null_value in:              dst: %405
  call  vm.builtin.reshape in: %406, c[19]  dst: %407
  call  vm.builtin.alloc_tensor in: %329, i0, c[20], c[107] dst: %408
  call  transpose1       in: %407, %408   dst: %void
  call  vm.builtin.null_value in:              dst: %406
  call  vm.builtin.null_value in:              dst: %407
  call  vm.builtin.reshape in: %408, c[22]  dst: %409
  call  vm.builtin.alloc_tensor in: %318, i0, c[23], c[108] dst: %410
  call  transpose2       in: %21, %410    dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[26], c[109] dst: %411
  call  matmul           in: %409, %410, %411 dst: %void
  call  vm.builtin.null_value in:              dst: %408
  call  vm.builtin.null_value in:              dst: %409
  call  vm.builtin.null_value in:              dst: %410
  call  vm.builtin.alloc_tensor in: %329, i0, c[26], c[110] dst: %412
  call  add2             in: %411, %22, %412 dst: %void
  call  vm.builtin.null_value in:              dst: %411
  call  vm.builtin.reshape in: %412, c[29]  dst: %413
  call  vm.builtin.alloc_tensor in: %315, i0, c[30], c[111] dst: %414
  call  transpose3       in: %413, %414   dst: %void
  call  vm.builtin.null_value in:              dst: %412
  call  vm.builtin.null_value in:              dst: %413
  call  vm.builtin.reshape in: %414, c[32]  dst: %415
  call  vm.builtin.alloc_tensor in: %344, i0, c[33], c[112] dst: %416
  call  vm.builtin.alloc_tensor in: %329, i0, c[33], c[113] dst: %417
  call  vm.builtin.alloc_tensor in: %323, i0, c[33], c[114] dst: %418
  call  split            in: %415, %416, %417, %418 dst: %void
  call  vm.builtin.null_value in:              dst: %414
  call  vm.builtin.null_value in:              dst: %415
  call  vm.builtin.make_tuple in: %416, %417, %418 dst: %419
  call  vm.builtin.reshape in: %416, c[38]  dst: %420
  call  vm.builtin.reshape in: %417, c[38]  dst: %421
  call  vm.builtin.reshape in: %418, c[38]  dst: %422
  call  vm.builtin.alloc_tensor in: %315, i0, c[38], c[115] dst: %423
  call  multiply         in: %420, %423   dst: %void
  call  vm.builtin.alloc_tensor in: %318, i0, c[41], c[116] dst: %424
  call  transpose4       in: %421, %424   dst: %void
  call  vm.builtin.null_value in:              dst: %417
  call  vm.builtin.null_value in:              dst: %421
  call  vm.builtin.alloc_tensor in: %329, i0, c[43], c[117] dst: %425
  call  matmul1          in: %423, %424, %425 dst: %void
  call  vm.builtin.null_value in:              dst: %423
  call  vm.builtin.null_value in:              dst: %424
  call  vm.builtin.reshape in: %25, c[45]   dst: %426
  call  vm.builtin.alloc_tensor in: %365, i0, c[48], c[118] dst: %427
  call  transpose5       in: %426, %427   dst: %void
  call  vm.builtin.null_value in:              dst: %426
  call  vm.builtin.reshape in: %427, c[50]  dst: %428
  call  vm.builtin.alloc_tensor in: %348, i0, c[52], c[119] dst: %429
  call  transpose6       in: %428, %429   dst: %void
  call  vm.builtin.null_value in:              dst: %427
  call  vm.builtin.null_value in:              dst: %428
  call  vm.builtin.reshape in: c[54], c[55] dst: %430
  call  vm.builtin.reshape in: %430, c[55]  dst: %431
  call  vm.builtin.null_value in:              dst: %430
  call  vm.builtin.reshape in: c[54], c[56] dst: %432
  call  vm.builtin.reshape in: %432, c[56]  dst: %433
  call  vm.builtin.null_value in:              dst: %432
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[120] dst: %434
  call  subtract         in: %431, %433, %434 dst: %void
  call  vm.builtin.null_value in:              dst: %431
  call  vm.builtin.null_value in:              dst: %433
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[121] dst: %435
  call  add3             in: %434, %435   dst: %void
  call  vm.builtin.null_value in:              dst: %434
  call  vm.builtin.alloc_tensor in: %351, i0, c[63], c[122] dst: %436
  call  take             in: %429, %435, %436 dst: %void
  call  vm.builtin.null_value in:              dst: %429
  call  vm.builtin.null_value in:              dst: %435
  call  vm.builtin.reshape in: %26, c[45]   dst: %437
  call  vm.builtin.alloc_tensor in: %365, i0, c[48], c[123] dst: %438
  call  transpose5       in: %437, %438   dst: %void
  call  vm.builtin.null_value in:              dst: %437
  call  vm.builtin.reshape in: %438, c[50]  dst: %439
  call  vm.builtin.alloc_tensor in: %348, i0, c[52], c[124] dst: %440
  call  transpose6       in: %439, %440   dst: %void
  call  vm.builtin.null_value in:              dst: %438
  call  vm.builtin.null_value in:              dst: %439
  call  vm.builtin.reshape in: c[54], c[55] dst: %441
  call  vm.builtin.reshape in: %441, c[55]  dst: %442
  call  vm.builtin.null_value in:              dst: %441
  call  vm.builtin.reshape in: c[54], c[56] dst: %443
  call  vm.builtin.reshape in: %443, c[56]  dst: %444
  call  vm.builtin.null_value in:              dst: %443
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[125] dst: %445
  call  subtract         in: %442, %444, %445 dst: %void
  call  vm.builtin.null_value in:              dst: %442
  call  vm.builtin.null_value in:              dst: %444
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[126] dst: %446
  call  add3             in: %445, %446   dst: %void
  call  vm.builtin.null_value in:              dst: %445
  call  vm.builtin.alloc_tensor in: %365, i0, c[63], c[127] dst: %447
  call  take             in: %440, %446, %447 dst: %void
  call  vm.builtin.null_value in:              dst: %440
  call  vm.builtin.null_value in:              dst: %446
  call  vm.builtin.reshape in: %420, c[72]  dst: %448
  call  vm.builtin.alloc_tensor in: %318, i0, c[73], c[128] dst: %449
  call  einsum           in: %448, %436, %449 dst: %void
  call  vm.builtin.null_value in:              dst: %436
  call  vm.builtin.alloc_tensor in: %315, i0, c[73], c[129] dst: %450
  call  einsum1          in: %448, %447, %450 dst: %void
  call  vm.builtin.null_value in:              dst: %416
  call  vm.builtin.null_value in:              dst: %420
  call  vm.builtin.null_value in:              dst: %448
  call  vm.builtin.null_value in:              dst: %447
  call  vm.builtin.reshape in: %425, c[76]  dst: %451
  call  vm.builtin.reshape in: %449, c[77]  dst: %452
  call  vm.builtin.reshape in: %450, c[78]  dst: %453
  call  vm.builtin.alloc_tensor in: %344, i0, c[76], c[130] dst: %454
  call  add4             in: %451, %452, %454 dst: %void
  call  vm.builtin.null_value in:              dst: %425
  call  vm.builtin.null_value in:              dst: %451
  call  vm.builtin.null_value in:              dst: %449
  call  vm.builtin.null_value in:              dst: %452
  call  vm.builtin.alloc_tensor in: %329, i0, c[76], c[131] dst: %455
  call  add5             in: %454, %453, %455 dst: %void
  call  vm.builtin.null_value in:              dst: %454
  call  vm.builtin.null_value in:              dst: %450
  call  vm.builtin.null_value in:              dst: %453
  call  vm.builtin.reshape in: %455, c[43]  dst: %456
  call  vm.builtin.alloc_tensor in: %344, i0, c[43], c[132] dst: %457
  call  softmax          in: %456, %457   dst: %void
  call  vm.builtin.null_value in:              dst: %455
  call  vm.builtin.null_value in:              dst: %456
  call  vm.builtin.alloc_tensor in: %318, i0, c[38], c[133] dst: %458
  call  matmul2          in: %457, %422, %458 dst: %void
  call  vm.builtin.null_value in:              dst: %457
  call  vm.builtin.null_value in:              dst: %418
  call  vm.builtin.null_value in:              dst: %422
  call  vm.builtin.reshape in: %458, c[83]  dst: %459
  call  vm.builtin.alloc_tensor in: %329, i0, c[84], c[134] dst: %460
  call  transpose7       in: %459, %460   dst: %void
  call  vm.builtin.null_value in:              dst: %458
  call  vm.builtin.null_value in:              dst: %459
  call  vm.builtin.reshape in: %460, c[22]  dst: %461
  call  vm.builtin.alloc_tensor in: %318, i0, c[86], c[135] dst: %462
  call  transpose8       in: %23, %462    dst: %void
  call  vm.builtin.alloc_tensor in: %344, i0, c[22], c[136] dst: %463
  call  matmul3          in: %461, %462, %463 dst: %void
  call  vm.builtin.null_value in:              dst: %460
  call  vm.builtin.null_value in:              dst: %461
  call  vm.builtin.null_value in:              dst: %462
  call  vm.builtin.alloc_tensor in: %318, i0, c[22], c[137] dst: %464
  call  add6             in: %463, %24, %464 dst: %void
  call  vm.builtin.null_value in:              dst: %463
  call  vm.builtin.reshape in: %464, c[20]  dst: %465
  call  vm.builtin.alloc_tensor in: %329, i0, c[19], c[138] dst: %466
  call  transpose9       in: %465, %466   dst: %void
  call  vm.builtin.null_value in:              dst: %464
  call  vm.builtin.null_value in:              dst: %465
  call  vm.builtin.reshape in: %466, c[17]  dst: %467
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[139] dst: %468
  call  strided_slice    in: %467, %468   dst: %void
  call  vm.builtin.null_value in:              dst: %466
  call  vm.builtin.null_value in:              dst: %467
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[140] dst: %469
  call  add1             in: %404, %468, %469 dst: %void
  call  vm.builtin.null_value in:              dst: %404
  call  vm.builtin.null_value in:              dst: %468
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[141] dst: %470
  call  layer_norm       in: %469, %27, %28, %470 dst: %void
  call  vm.builtin.alloc_tensor in: %318, i0, c[94], c[142] dst: %471
  call  transpose10      in: %29, %471    dst: %void
  call  vm.builtin.alloc_tensor in: %315, i0, c[96], c[143] dst: %472
  call  matmul4          in: %470, %471, %472 dst: %void
  call  vm.builtin.null_value in:              dst: %470
  call  vm.builtin.null_value in:              dst: %471
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[144] dst: %473
  call  add7             in: %472, %30, %473 dst: %void
  call  vm.builtin.null_value in:              dst: %472
  call  vm.builtin.alloc_tensor in: %315, i0, c[96], c[145] dst: %474
  call  gelu             in: %473, %474   dst: %void
  call  vm.builtin.null_value in:              dst: %473
  call  vm.builtin.alloc_tensor in: %337, i0, c[100], c[146] dst: %475
  call  transpose11      in: %31, %475    dst: %void
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[147] dst: %476
  call  matmul5          in: %474, %475, %476 dst: %void
  call  vm.builtin.null_value in:              dst: %474
  call  vm.builtin.null_value in:              dst: %475
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[148] dst: %477
  call  add8             in: %476, %32, %477 dst: %void
  call  vm.builtin.null_value in:              dst: %476
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[149] dst: %478
  call  add1             in: %469, %477, %478 dst: %void
  call  vm.builtin.null_value in:              dst: %469
  call  vm.builtin.null_value in:              dst: %477
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[150] dst: %479
  call  layer_norm       in: %478, %33, %34, %479 dst: %void
  call  vm.builtin.alloc_tensor in: %329, i0, c[23], c[151] dst: %480
  call  transpose2       in: %35, %480    dst: %void
  call  vm.builtin.alloc_tensor in: %344, i0, c[152], c[153] dst: %481
  call  matmul6          in: %479, %480, %481 dst: %void
  call  vm.builtin.null_value in:              dst: %479
  call  vm.builtin.null_value in:              dst: %480
  call  vm.builtin.alloc_tensor in: %329, i0, c[152], c[154] dst: %482
  call  add9             in: %481, %36, %482 dst: %void
  call  vm.builtin.null_value in:              dst: %481
  call  vm.builtin.reshape in: %482, c[155] dst: %483
  call  vm.builtin.alloc_tensor in: %344, i0, c[156], c[157] dst: %484
  call  transpose12      in: %483, %484   dst: %void
  call  vm.builtin.null_value in:              dst: %482
  call  vm.builtin.null_value in:              dst: %483
  call  vm.builtin.reshape in: %484, c[158] dst: %485
  call  vm.builtin.alloc_tensor in: %337, i0, c[159], c[160] dst: %486
  call  vm.builtin.alloc_tensor in: %329, i0, c[159], c[161] dst: %487
  call  vm.builtin.alloc_tensor in: %323, i0, c[159], c[162] dst: %488
  call  split1           in: %485, %486, %487, %488 dst: %void
  call  vm.builtin.null_value in:              dst: %484
  call  vm.builtin.null_value in:              dst: %485
  call  vm.builtin.make_tuple in: %486, %487, %488 dst: %489
  call  vm.builtin.reshape in: %486, c[163] dst: %490
  call  vm.builtin.reshape in: %487, c[163] dst: %491
  call  vm.builtin.reshape in: %488, c[163] dst: %492
  call  vm.builtin.alloc_tensor in: %344, i0, c[163], c[164] dst: %493
  call  multiply3        in: %490, %493   dst: %void
  call  vm.builtin.alloc_tensor in: %315, i0, c[165], c[166] dst: %494
  call  transpose13      in: %491, %494   dst: %void
  call  vm.builtin.null_value in:              dst: %487
  call  vm.builtin.null_value in:              dst: %491
  call  vm.builtin.alloc_storage in: %vm, c[2], i0, c[167], c[4] dst: %495
  call  vm.builtin.alloc_tensor in: %495, i0, c[168], c[169] dst: %496
  call  matmul7          in: %493, %494, %496 dst: %void
  call  vm.builtin.null_value in:              dst: %493
  call  vm.builtin.null_value in:              dst: %494
  call  vm.builtin.reshape in: %39, c[170]  dst: %497
  call  vm.builtin.alloc_tensor in: %348, i0, c[171], c[172] dst: %498
  call  transpose14      in: %497, %498   dst: %void
  call  vm.builtin.null_value in:              dst: %497
  call  vm.builtin.reshape in: %498, c[173] dst: %499
  call  vm.builtin.alloc_tensor in: %351, i0, c[174], c[175] dst: %500
  call  transpose15      in: %499, %500   dst: %void
  call  vm.builtin.null_value in:              dst: %498
  call  vm.builtin.null_value in:              dst: %499
  call  vm.builtin.reshape in: c[176], c[177] dst: %501
  call  vm.builtin.reshape in: %501, c[177] dst: %502
  call  vm.builtin.null_value in:              dst: %501
  call  vm.builtin.reshape in: c[176], c[178] dst: %503
  call  vm.builtin.reshape in: %503, c[178] dst: %504
  call  vm.builtin.null_value in:              dst: %503
  call  vm.builtin.alloc_storage in: %vm, c[179], i0, c[180], c[4] dst: %505
  call  vm.builtin.alloc_tensor in: %505, i0, c[181], c[182] dst: %506
  call  subtract1        in: %502, %504, %506 dst: %void
  call  vm.builtin.null_value in:              dst: %502
  call  vm.builtin.null_value in:              dst: %504
  call  vm.builtin.alloc_storage in: %vm, c[179], i0, c[183], c[4] dst: %507
  call  vm.builtin.alloc_tensor in: %507, i0, c[181], c[184] dst: %508
  call  add10            in: %506, %508   dst: %void
  call  vm.builtin.null_value in:              dst: %506
  call  vm.builtin.alloc_storage in: %vm, c[8], i0, c[185], c[4] dst: %509
  call  vm.builtin.alloc_tensor in: %509, i0, c[186], c[187] dst: %510
  call  take1            in: %500, %508, %510 dst: %void
  call  vm.builtin.null_value in:              dst: %500
  call  vm.builtin.null_value in:              dst: %508
  call  vm.builtin.reshape in: %40, c[170]  dst: %511
  call  vm.builtin.alloc_tensor in: %365, i0, c[171], c[188] dst: %512
  call  transpose14      in: %511, %512   dst: %void
  call  vm.builtin.null_value in:              dst: %511
  call  vm.builtin.reshape in: %512, c[173] dst: %513
  call  vm.builtin.alloc_tensor in: %348, i0, c[174], c[189] dst: %514
  call  transpose15      in: %513, %514   dst: %void
  call  vm.builtin.null_value in:              dst: %512
  call  vm.builtin.null_value in:              dst: %513
  call  vm.builtin.reshape in: c[176], c[177] dst: %515
  call  vm.builtin.reshape in: %515, c[177] dst: %516
  call  vm.builtin.null_value in:              dst: %515
  call  vm.builtin.reshape in: c[176], c[178] dst: %517
  call  vm.builtin.reshape in: %517, c[178] dst: %518
  call  vm.builtin.null_value in:              dst: %517
  call  vm.builtin.alloc_tensor in: %505, i0, c[181], c[190] dst: %519
  call  subtract1        in: %516, %518, %519 dst: %void
  call  vm.builtin.null_value in:              dst: %516
  call  vm.builtin.null_value in:              dst: %518
  call  vm.builtin.alloc_tensor in: %507, i0, c[181], c[191] dst: %520
  call  add10            in: %519, %520   dst: %void
  call  vm.builtin.null_value in:              dst: %519
  call  vm.builtin.alloc_storage in: %vm, c[8], i0, c[192], c[4] dst: %521
  call  vm.builtin.alloc_tensor in: %521, i0, c[186], c[193] dst: %522
  call  take1            in: %514, %520, %522 dst: %void
  call  vm.builtin.null_value in:              dst: %514
  call  vm.builtin.null_value in:              dst: %520
  call  vm.builtin.reshape in: %490, c[194] dst: %523
  call  vm.builtin.alloc_tensor in: %329, i0, c[194], c[195] dst: %524
  call  einsum2          in: %523, %510, %524 dst: %void
  call  vm.builtin.null_value in:              dst: %510
  call  vm.builtin.alloc_tensor in: %344, i0, c[194], c[196] dst: %525
  call  einsum3          in: %523, %522, %525 dst: %void
  call  vm.builtin.null_value in:              dst: %486
  call  vm.builtin.null_value in:              dst: %490
  call  vm.builtin.null_value in:              dst: %523
  call  vm.builtin.null_value in:              dst: %522
  call  vm.builtin.reshape in: %496, c[197] dst: %526
  call  vm.builtin.reshape in: %524, c[198] dst: %527
  call  vm.builtin.reshape in: %525, c[199] dst: %528
  call  vm.builtin.alloc_tensor in: %315, i0, c[197], c[200] dst: %529
  call  add11            in: %526, %527, %529 dst: %void
  call  vm.builtin.null_value in:              dst: %496
  call  vm.builtin.null_value in:              dst: %526
  call  vm.builtin.null_value in:              dst: %524
  call  vm.builtin.null_value in:              dst: %527
  call  vm.builtin.alloc_tensor in: %495, i0, c[197], c[201] dst: %530
  call  add12            in: %529, %528, %530 dst: %void
  call  vm.builtin.null_value in:              dst: %529
  call  vm.builtin.null_value in:              dst: %525
  call  vm.builtin.null_value in:              dst: %528
  call  vm.builtin.reshape in: %530, c[168] dst: %531
  call  vm.builtin.alloc_tensor in: %315, i0, c[168], c[202] dst: %532
  call  softmax1         in: %531, %532   dst: %void
  call  vm.builtin.null_value in:              dst: %530
  call  vm.builtin.null_value in:              dst: %531
  call  vm.builtin.alloc_tensor in: %337, i0, c[163], c[203] dst: %533
  call  matmul8          in: %532, %492, %533 dst: %void
  call  vm.builtin.null_value in:              dst: %532
  call  vm.builtin.null_value in:              dst: %488
  call  vm.builtin.null_value in:              dst: %492
  call  vm.builtin.reshape in: %533, c[204] dst: %534
  call  vm.builtin.alloc_tensor in: %329, i0, c[205], c[206] dst: %535
  call  transpose16      in: %534, %535   dst: %void
  call  vm.builtin.null_value in:              dst: %533
  call  vm.builtin.null_value in:              dst: %534
  call  vm.builtin.reshape in: %535, c[11]  dst: %536
  call  vm.builtin.alloc_tensor in: %337, i0, c[86], c[207] dst: %537
  call  transpose8       in: %37, %537    dst: %void
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[208] dst: %538
  call  matmul9          in: %536, %537, %538 dst: %void
  call  vm.builtin.null_value in:              dst: %535
  call  vm.builtin.null_value in:              dst: %536
  call  vm.builtin.null_value in:              dst: %537
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[209] dst: %539
  call  add8             in: %538, %38, %539 dst: %void
  call  vm.builtin.null_value in:              dst: %538
  call  vm.builtin.alloc_tensor in: %329, i0, c[11], c[210] dst: %540
  call  add1             in: %478, %539, %540 dst: %void
  call  vm.builtin.null_value in:              dst: %478
  call  vm.builtin.null_value in:              dst: %539
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[211] dst: %541
  call  layer_norm       in: %540, %41, %42, %541 dst: %void
  call  vm.builtin.alloc_tensor in: %337, i0, c[94], c[212] dst: %542
  call  transpose10      in: %43, %542    dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[213] dst: %543
  call  matmul4          in: %541, %542, %543 dst: %void
  call  vm.builtin.null_value in:              dst: %541
  call  vm.builtin.null_value in:              dst: %542
  call  vm.builtin.alloc_tensor in: %495, i0, c[96], c[214] dst: %544
  call  add7             in: %543, %44, %544 dst: %void
  call  vm.builtin.null_value in:              dst: %543
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[215] dst: %545
  call  gelu             in: %544, %545   dst: %void
  call  vm.builtin.null_value in:              dst: %544
  call  vm.builtin.alloc_tensor in: %318, i0, c[100], c[216] dst: %546
  call  transpose11      in: %45, %546    dst: %void
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[217] dst: %547
  call  matmul5          in: %545, %546, %547 dst: %void
  call  vm.builtin.null_value in:              dst: %545
  call  vm.builtin.null_value in:              dst: %546
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[218] dst: %548
  call  add8             in: %547, %46, %548 dst: %void
  call  vm.builtin.null_value in:              dst: %547
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[219] dst: %549
  call  add1             in: %540, %548, %549 dst: %void
  call  vm.builtin.null_value in:              dst: %540
  call  vm.builtin.null_value in:              dst: %548
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[220] dst: %550
  call  layer_norm       in: %549, %47, %48, %550 dst: %void
  call  vm.builtin.alloc_tensor in: %344, i0, c[17], c[221] dst: %551
  call  pad              in: %550, %551   dst: %void
  call  vm.builtin.null_value in:              dst: %550
  call  vm.builtin.reshape in: %551, c[19]  dst: %552
  call  vm.builtin.alloc_tensor in: %318, i0, c[20], c[222] dst: %553
  call  transpose1       in: %552, %553   dst: %void
  call  vm.builtin.null_value in:              dst: %551
  call  vm.builtin.null_value in:              dst: %552
  call  vm.builtin.reshape in: %553, c[22]  dst: %554
  call  vm.builtin.alloc_tensor in: %329, i0, c[23], c[223] dst: %555
  call  transpose2       in: %49, %555    dst: %void
  call  vm.builtin.alloc_tensor in: %344, i0, c[26], c[224] dst: %556
  call  matmul           in: %554, %555, %556 dst: %void
  call  vm.builtin.null_value in:              dst: %553
  call  vm.builtin.null_value in:              dst: %554
  call  vm.builtin.null_value in:              dst: %555
  call  vm.builtin.alloc_tensor in: %329, i0, c[26], c[225] dst: %557
  call  add2             in: %556, %50, %557 dst: %void
  call  vm.builtin.null_value in:              dst: %556
  call  vm.builtin.reshape in: %557, c[29]  dst: %558
  call  vm.builtin.alloc_tensor in: %344, i0, c[30], c[226] dst: %559
  call  transpose3       in: %558, %559   dst: %void
  call  vm.builtin.null_value in:              dst: %557
  call  vm.builtin.null_value in:              dst: %558
  call  vm.builtin.reshape in: %559, c[32]  dst: %560
  call  vm.builtin.alloc_tensor in: %318, i0, c[33], c[227] dst: %561
  call  vm.builtin.alloc_tensor in: %329, i0, c[33], c[228] dst: %562
  call  vm.builtin.alloc_tensor in: %323, i0, c[33], c[229] dst: %563
  call  split            in: %560, %561, %562, %563 dst: %void
  call  vm.builtin.null_value in:              dst: %559
  call  vm.builtin.null_value in:              dst: %560
  call  vm.builtin.make_tuple in: %561, %562, %563 dst: %564
  call  vm.builtin.reshape in: %561, c[38]  dst: %565
  call  vm.builtin.reshape in: %562, c[38]  dst: %566
  call  vm.builtin.reshape in: %563, c[38]  dst: %567
  call  vm.builtin.alloc_tensor in: %344, i0, c[38], c[230] dst: %568
  call  multiply         in: %565, %568   dst: %void
  call  vm.builtin.alloc_tensor in: %521, i0, c[41], c[231] dst: %569
  call  transpose4       in: %566, %569   dst: %void
  call  vm.builtin.null_value in:              dst: %562
  call  vm.builtin.null_value in:              dst: %566
  call  vm.builtin.alloc_tensor in: %329, i0, c[43], c[232] dst: %570
  call  matmul1          in: %568, %569, %570 dst: %void
  call  vm.builtin.null_value in:              dst: %568
  call  vm.builtin.null_value in:              dst: %569
  call  vm.builtin.reshape in: %53, c[45]   dst: %571
  call  vm.builtin.alloc_tensor in: %351, i0, c[48], c[233] dst: %572
  call  transpose5       in: %571, %572   dst: %void
  call  vm.builtin.null_value in:              dst: %571
  call  vm.builtin.reshape in: %572, c[50]  dst: %573
  call  vm.builtin.alloc_tensor in: %365, i0, c[52], c[234] dst: %574
  call  transpose6       in: %573, %574   dst: %void
  call  vm.builtin.null_value in:              dst: %572
  call  vm.builtin.null_value in:              dst: %573
  call  vm.builtin.reshape in: c[54], c[55] dst: %575
  call  vm.builtin.reshape in: %575, c[55]  dst: %576
  call  vm.builtin.null_value in:              dst: %575
  call  vm.builtin.reshape in: c[54], c[56] dst: %577
  call  vm.builtin.reshape in: %577, c[56]  dst: %578
  call  vm.builtin.null_value in:              dst: %577
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[235] dst: %579
  call  subtract         in: %576, %578, %579 dst: %void
  call  vm.builtin.null_value in:              dst: %576
  call  vm.builtin.null_value in:              dst: %578
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[236] dst: %580
  call  add3             in: %579, %580   dst: %void
  call  vm.builtin.null_value in:              dst: %579
  call  vm.builtin.alloc_tensor in: %348, i0, c[63], c[237] dst: %581
  call  take             in: %574, %580, %581 dst: %void
  call  vm.builtin.null_value in:              dst: %574
  call  vm.builtin.null_value in:              dst: %580
  call  vm.builtin.reshape in: %54, c[45]   dst: %582
  call  vm.builtin.alloc_tensor in: %351, i0, c[48], c[238] dst: %583
  call  transpose5       in: %582, %583   dst: %void
  call  vm.builtin.null_value in:              dst: %582
  call  vm.builtin.reshape in: %583, c[50]  dst: %584
  call  vm.builtin.alloc_tensor in: %365, i0, c[52], c[239] dst: %585
  call  transpose6       in: %584, %585   dst: %void
  call  vm.builtin.null_value in:              dst: %583
  call  vm.builtin.null_value in:              dst: %584
  call  vm.builtin.reshape in: c[54], c[55] dst: %586
  call  vm.builtin.reshape in: %586, c[55]  dst: %587
  call  vm.builtin.null_value in:              dst: %586
  call  vm.builtin.reshape in: c[54], c[56] dst: %588
  call  vm.builtin.reshape in: %588, c[56]  dst: %589
  call  vm.builtin.null_value in:              dst: %588
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[240] dst: %590
  call  subtract         in: %587, %589, %590 dst: %void
  call  vm.builtin.null_value in:              dst: %587
  call  vm.builtin.null_value in:              dst: %589
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[241] dst: %591
  call  add3             in: %590, %591   dst: %void
  call  vm.builtin.null_value in:              dst: %590
  call  vm.builtin.alloc_tensor in: %351, i0, c[63], c[242] dst: %592
  call  take             in: %585, %591, %592 dst: %void
  call  vm.builtin.null_value in:              dst: %585
  call  vm.builtin.null_value in:              dst: %591
  call  vm.builtin.reshape in: %565, c[72]  dst: %593
  call  vm.builtin.alloc_tensor in: %521, i0, c[73], c[243] dst: %594
  call  einsum           in: %593, %581, %594 dst: %void
  call  vm.builtin.null_value in:              dst: %581
  call  vm.builtin.alloc_tensor in: %344, i0, c[73], c[244] dst: %595
  call  einsum1          in: %593, %592, %595 dst: %void
  call  vm.builtin.null_value in:              dst: %561
  call  vm.builtin.null_value in:              dst: %565
  call  vm.builtin.null_value in:              dst: %593
  call  vm.builtin.null_value in:              dst: %592
  call  vm.builtin.reshape in: %570, c[76]  dst: %596
  call  vm.builtin.reshape in: %594, c[77]  dst: %597
  call  vm.builtin.reshape in: %595, c[78]  dst: %598
  call  vm.builtin.alloc_tensor in: %318, i0, c[76], c[245] dst: %599
  call  add4             in: %596, %597, %599 dst: %void
  call  vm.builtin.null_value in:              dst: %570
  call  vm.builtin.null_value in:              dst: %596
  call  vm.builtin.null_value in:              dst: %594
  call  vm.builtin.null_value in:              dst: %597
  call  vm.builtin.alloc_tensor in: %329, i0, c[76], c[246] dst: %600
  call  add5             in: %599, %598, %600 dst: %void
  call  vm.builtin.null_value in:              dst: %599
  call  vm.builtin.null_value in:              dst: %595
  call  vm.builtin.null_value in:              dst: %598
  call  vm.builtin.reshape in: %600, c[43]  dst: %601
  call  vm.builtin.alloc_tensor in: %318, i0, c[43], c[247] dst: %602
  call  softmax          in: %601, %602   dst: %void
  call  vm.builtin.null_value in:              dst: %600
  call  vm.builtin.null_value in:              dst: %601
  call  vm.builtin.alloc_tensor in: %521, i0, c[38], c[248] dst: %603
  call  matmul2          in: %602, %567, %603 dst: %void
  call  vm.builtin.null_value in:              dst: %602
  call  vm.builtin.null_value in:              dst: %563
  call  vm.builtin.null_value in:              dst: %567
  call  vm.builtin.reshape in: %603, c[83]  dst: %604
  call  vm.builtin.alloc_tensor in: %344, i0, c[84], c[249] dst: %605
  call  transpose7       in: %604, %605   dst: %void
  call  vm.builtin.null_value in:              dst: %603
  call  vm.builtin.null_value in:              dst: %604
  call  vm.builtin.reshape in: %605, c[22]  dst: %606
  call  vm.builtin.alloc_tensor in: %521, i0, c[86], c[250] dst: %607
  call  transpose8       in: %51, %607    dst: %void
  call  vm.builtin.alloc_tensor in: %329, i0, c[22], c[251] dst: %608
  call  matmul3          in: %606, %607, %608 dst: %void
  call  vm.builtin.null_value in:              dst: %605
  call  vm.builtin.null_value in:              dst: %606
  call  vm.builtin.null_value in:              dst: %607
  call  vm.builtin.alloc_tensor in: %521, i0, c[22], c[252] dst: %609
  call  add6             in: %608, %52, %609 dst: %void
  call  vm.builtin.null_value in:              dst: %608
  call  vm.builtin.reshape in: %609, c[20]  dst: %610
  call  vm.builtin.alloc_tensor in: %318, i0, c[19], c[253] dst: %611
  call  transpose9       in: %610, %611   dst: %void
  call  vm.builtin.null_value in:              dst: %609
  call  vm.builtin.null_value in:              dst: %610
  call  vm.builtin.reshape in: %611, c[17]  dst: %612
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[254] dst: %613
  call  strided_slice    in: %612, %613   dst: %void
  call  vm.builtin.null_value in:              dst: %611
  call  vm.builtin.null_value in:              dst: %612
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[255] dst: %614
  call  add1             in: %549, %613, %614 dst: %void
  call  vm.builtin.null_value in:              dst: %549
  call  vm.builtin.null_value in:              dst: %613
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[256] dst: %615
  call  layer_norm       in: %614, %55, %56, %615 dst: %void
  call  vm.builtin.alloc_tensor in: %521, i0, c[94], c[257] dst: %616
  call  transpose10      in: %57, %616    dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[258] dst: %617
  call  matmul4          in: %615, %616, %617 dst: %void
  call  vm.builtin.null_value in:              dst: %615
  call  vm.builtin.null_value in:              dst: %616
  call  vm.builtin.alloc_tensor in: %315, i0, c[96], c[259] dst: %618
  call  add7             in: %617, %58, %618 dst: %void
  call  vm.builtin.null_value in:              dst: %617
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[260] dst: %619
  call  gelu             in: %618, %619   dst: %void
  call  vm.builtin.null_value in:              dst: %618
  call  vm.builtin.alloc_tensor in: %337, i0, c[100], c[261] dst: %620
  call  transpose11      in: %59, %620    dst: %void
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[262] dst: %621
  call  matmul5          in: %619, %620, %621 dst: %void
  call  vm.builtin.null_value in:              dst: %619
  call  vm.builtin.null_value in:              dst: %620
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[263] dst: %622
  call  add8             in: %621, %60, %622 dst: %void
  call  vm.builtin.null_value in:              dst: %621
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[264] dst: %623
  call  add1             in: %614, %622, %623 dst: %void
  call  vm.builtin.null_value in:              dst: %614
  call  vm.builtin.null_value in:              dst: %622
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[265] dst: %624
  call  layer_norm       in: %623, %61, %62, %624 dst: %void
  call  vm.builtin.alloc_tensor in: %329, i0, c[17], c[266] dst: %625
  call  pad              in: %624, %625   dst: %void
  call  vm.builtin.null_value in:              dst: %624
  call  vm.builtin.reshape in: %625, c[19]  dst: %626
  call  vm.builtin.alloc_tensor in: %337, i0, c[20], c[267] dst: %627
  call  transpose1       in: %626, %627   dst: %void
  call  vm.builtin.null_value in:              dst: %625
  call  vm.builtin.null_value in:              dst: %626
  call  vm.builtin.reshape in: %627, c[22]  dst: %628
  call  vm.builtin.alloc_tensor in: %318, i0, c[23], c[268] dst: %629
  call  transpose2       in: %63, %629    dst: %void
  call  vm.builtin.alloc_tensor in: %344, i0, c[26], c[269] dst: %630
  call  matmul           in: %628, %629, %630 dst: %void
  call  vm.builtin.null_value in:              dst: %627
  call  vm.builtin.null_value in:              dst: %628
  call  vm.builtin.null_value in:              dst: %629
  call  vm.builtin.alloc_tensor in: %329, i0, c[26], c[270] dst: %631
  call  add2             in: %630, %64, %631 dst: %void
  call  vm.builtin.null_value in:              dst: %630
  call  vm.builtin.reshape in: %631, c[29]  dst: %632
  call  vm.builtin.alloc_tensor in: %318, i0, c[30], c[271] dst: %633
  call  transpose3       in: %632, %633   dst: %void
  call  vm.builtin.null_value in:              dst: %631
  call  vm.builtin.null_value in:              dst: %632
  call  vm.builtin.reshape in: %633, c[32]  dst: %634
  call  vm.builtin.alloc_tensor in: %337, i0, c[33], c[272] dst: %635
  call  vm.builtin.alloc_tensor in: %344, i0, c[33], c[273] dst: %636
  call  vm.builtin.alloc_tensor in: %329, i0, c[33], c[274] dst: %637
  call  split            in: %634, %635, %636, %637 dst: %void
  call  vm.builtin.null_value in:              dst: %633
  call  vm.builtin.null_value in:              dst: %634
  call  vm.builtin.make_tuple in: %635, %636, %637 dst: %638
  call  vm.builtin.reshape in: %635, c[38]  dst: %639
  call  vm.builtin.reshape in: %636, c[38]  dst: %640
  call  vm.builtin.reshape in: %637, c[38]  dst: %641
  call  vm.builtin.alloc_tensor in: %318, i0, c[38], c[275] dst: %642
  call  multiply         in: %639, %642   dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[41], c[276] dst: %643
  call  transpose4       in: %640, %643   dst: %void
  call  vm.builtin.null_value in:              dst: %636
  call  vm.builtin.null_value in:              dst: %640
  call  vm.builtin.alloc_tensor in: %344, i0, c[43], c[277] dst: %644
  call  matmul1          in: %642, %643, %644 dst: %void
  call  vm.builtin.null_value in:              dst: %642
  call  vm.builtin.null_value in:              dst: %643
  call  vm.builtin.reshape in: %67, c[45]   dst: %645
  call  vm.builtin.alloc_tensor in: %365, i0, c[48], c[278] dst: %646
  call  transpose5       in: %645, %646   dst: %void
  call  vm.builtin.null_value in:              dst: %645
  call  vm.builtin.reshape in: %646, c[50]  dst: %647
  call  vm.builtin.alloc_tensor in: %348, i0, c[52], c[279] dst: %648
  call  transpose6       in: %647, %648   dst: %void
  call  vm.builtin.null_value in:              dst: %646
  call  vm.builtin.null_value in:              dst: %647
  call  vm.builtin.reshape in: c[54], c[55] dst: %649
  call  vm.builtin.reshape in: %649, c[55]  dst: %650
  call  vm.builtin.null_value in:              dst: %649
  call  vm.builtin.reshape in: c[54], c[56] dst: %651
  call  vm.builtin.reshape in: %651, c[56]  dst: %652
  call  vm.builtin.null_value in:              dst: %651
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[280] dst: %653
  call  subtract         in: %650, %652, %653 dst: %void
  call  vm.builtin.null_value in:              dst: %650
  call  vm.builtin.null_value in:              dst: %652
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[281] dst: %654
  call  add3             in: %653, %654   dst: %void
  call  vm.builtin.null_value in:              dst: %653
  call  vm.builtin.alloc_tensor in: %351, i0, c[63], c[282] dst: %655
  call  take             in: %648, %654, %655 dst: %void
  call  vm.builtin.null_value in:              dst: %648
  call  vm.builtin.null_value in:              dst: %654
  call  vm.builtin.reshape in: %68, c[45]   dst: %656
  call  vm.builtin.alloc_tensor in: %365, i0, c[48], c[283] dst: %657
  call  transpose5       in: %656, %657   dst: %void
  call  vm.builtin.null_value in:              dst: %656
  call  vm.builtin.reshape in: %657, c[50]  dst: %658
  call  vm.builtin.alloc_tensor in: %348, i0, c[52], c[284] dst: %659
  call  transpose6       in: %658, %659   dst: %void
  call  vm.builtin.null_value in:              dst: %657
  call  vm.builtin.null_value in:              dst: %658
  call  vm.builtin.reshape in: c[54], c[55] dst: %660
  call  vm.builtin.reshape in: %660, c[55]  dst: %661
  call  vm.builtin.null_value in:              dst: %660
  call  vm.builtin.reshape in: c[54], c[56] dst: %662
  call  vm.builtin.reshape in: %662, c[56]  dst: %663
  call  vm.builtin.null_value in:              dst: %662
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[285] dst: %664
  call  subtract         in: %661, %663, %664 dst: %void
  call  vm.builtin.null_value in:              dst: %661
  call  vm.builtin.null_value in:              dst: %663
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[286] dst: %665
  call  add3             in: %664, %665   dst: %void
  call  vm.builtin.null_value in:              dst: %664
  call  vm.builtin.alloc_tensor in: %365, i0, c[63], c[287] dst: %666
  call  take             in: %659, %665, %666 dst: %void
  call  vm.builtin.null_value in:              dst: %659
  call  vm.builtin.null_value in:              dst: %665
  call  vm.builtin.reshape in: %639, c[72]  dst: %667
  call  vm.builtin.alloc_tensor in: %318, i0, c[73], c[288] dst: %668
  call  einsum           in: %667, %655, %668 dst: %void
  call  vm.builtin.null_value in:              dst: %655
  call  vm.builtin.alloc_tensor in: %323, i0, c[73], c[289] dst: %669
  call  einsum1          in: %667, %666, %669 dst: %void
  call  vm.builtin.null_value in:              dst: %635
  call  vm.builtin.null_value in:              dst: %639
  call  vm.builtin.null_value in:              dst: %667
  call  vm.builtin.null_value in:              dst: %666
  call  vm.builtin.reshape in: %644, c[76]  dst: %670
  call  vm.builtin.reshape in: %668, c[77]  dst: %671
  call  vm.builtin.reshape in: %669, c[78]  dst: %672
  call  vm.builtin.alloc_tensor in: %337, i0, c[76], c[290] dst: %673
  call  add4             in: %670, %671, %673 dst: %void
  call  vm.builtin.null_value in:              dst: %644
  call  vm.builtin.null_value in:              dst: %670
  call  vm.builtin.null_value in:              dst: %668
  call  vm.builtin.null_value in:              dst: %671
  call  vm.builtin.alloc_tensor in: %344, i0, c[76], c[291] dst: %674
  call  add5             in: %673, %672, %674 dst: %void
  call  vm.builtin.null_value in:              dst: %673
  call  vm.builtin.null_value in:              dst: %669
  call  vm.builtin.null_value in:              dst: %672
  call  vm.builtin.reshape in: %674, c[43]  dst: %675
  call  vm.builtin.alloc_tensor in: %318, i0, c[43], c[292] dst: %676
  call  softmax          in: %675, %676   dst: %void
  call  vm.builtin.null_value in:              dst: %674
  call  vm.builtin.null_value in:              dst: %675
  call  vm.builtin.alloc_tensor in: %337, i0, c[38], c[293] dst: %677
  call  matmul2          in: %676, %641, %677 dst: %void
  call  vm.builtin.null_value in:              dst: %676
  call  vm.builtin.null_value in:              dst: %637
  call  vm.builtin.null_value in:              dst: %641
  call  vm.builtin.reshape in: %677, c[83]  dst: %678
  call  vm.builtin.alloc_tensor in: %344, i0, c[84], c[294] dst: %679
  call  transpose7       in: %678, %679   dst: %void
  call  vm.builtin.null_value in:              dst: %677
  call  vm.builtin.null_value in:              dst: %678
  call  vm.builtin.reshape in: %679, c[22]  dst: %680
  call  vm.builtin.alloc_tensor in: %509, i0, c[86], c[295] dst: %681
  call  transpose8       in: %65, %681    dst: %void
  call  vm.builtin.alloc_tensor in: %318, i0, c[22], c[296] dst: %682
  call  matmul3          in: %680, %681, %682 dst: %void
  call  vm.builtin.null_value in:              dst: %679
  call  vm.builtin.null_value in:              dst: %680
  call  vm.builtin.null_value in:              dst: %681
  call  vm.builtin.alloc_tensor in: %329, i0, c[22], c[297] dst: %683
  call  add6             in: %682, %66, %683 dst: %void
  call  vm.builtin.null_value in:              dst: %682
  call  vm.builtin.reshape in: %683, c[20]  dst: %684
  call  vm.builtin.alloc_tensor in: %337, i0, c[19], c[298] dst: %685
  call  transpose9       in: %684, %685   dst: %void
  call  vm.builtin.null_value in:              dst: %683
  call  vm.builtin.null_value in:              dst: %684
  call  vm.builtin.reshape in: %685, c[17]  dst: %686
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[299] dst: %687
  call  strided_slice    in: %686, %687   dst: %void
  call  vm.builtin.null_value in:              dst: %685
  call  vm.builtin.null_value in:              dst: %686
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[300] dst: %688
  call  add1             in: %623, %687, %688 dst: %void
  call  vm.builtin.null_value in:              dst: %623
  call  vm.builtin.null_value in:              dst: %687
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[301] dst: %689
  call  layer_norm       in: %688, %69, %70, %689 dst: %void
  call  vm.builtin.alloc_tensor in: %329, i0, c[94], c[302] dst: %690
  call  transpose10      in: %71, %690    dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[303] dst: %691
  call  matmul4          in: %689, %690, %691 dst: %void
  call  vm.builtin.null_value in:              dst: %689
  call  vm.builtin.null_value in:              dst: %690
  call  vm.builtin.alloc_tensor in: %495, i0, c[96], c[304] dst: %692
  call  add7             in: %691, %72, %692 dst: %void
  call  vm.builtin.null_value in:              dst: %691
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[305] dst: %693
  call  gelu             in: %692, %693   dst: %void
  call  vm.builtin.null_value in:              dst: %692
  call  vm.builtin.alloc_tensor in: %521, i0, c[100], c[306] dst: %694
  call  transpose11      in: %73, %694    dst: %void
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[307] dst: %695
  call  matmul5          in: %693, %694, %695 dst: %void
  call  vm.builtin.null_value in:              dst: %693
  call  vm.builtin.null_value in:              dst: %694
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[308] dst: %696
  call  add8             in: %695, %74, %696 dst: %void
  call  vm.builtin.null_value in:              dst: %695
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[309] dst: %697
  call  add1             in: %688, %696, %697 dst: %void
  call  vm.builtin.null_value in:              dst: %688
  call  vm.builtin.null_value in:              dst: %696
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[310] dst: %698
  call  layer_norm       in: %697, %75, %76, %698 dst: %void
  call  vm.builtin.alloc_tensor in: %329, i0, c[23], c[311] dst: %699
  call  transpose2       in: %77, %699    dst: %void
  call  vm.builtin.alloc_tensor in: %337, i0, c[152], c[312] dst: %700
  call  matmul6          in: %698, %699, %700 dst: %void
  call  vm.builtin.null_value in:              dst: %698
  call  vm.builtin.null_value in:              dst: %699
  call  vm.builtin.alloc_tensor in: %318, i0, c[152], c[313] dst: %701
  call  add9             in: %700, %78, %701 dst: %void
  call  vm.builtin.null_value in:              dst: %700
  call  vm.builtin.reshape in: %701, c[155] dst: %702
  call  vm.builtin.alloc_tensor in: %329, i0, c[156], c[314] dst: %703
  call  transpose12      in: %702, %703   dst: %void
  call  vm.builtin.null_value in:              dst: %701
  call  vm.builtin.null_value in:              dst: %702
  call  vm.builtin.reshape in: %703, c[158] dst: %704
  call  vm.builtin.alloc_tensor in: %521, i0, c[159], c[315] dst: %705
  call  vm.builtin.alloc_tensor in: %337, i0, c[159], c[316] dst: %706
  call  vm.builtin.alloc_tensor in: %318, i0, c[159], c[317] dst: %707
  call  split1           in: %704, %705, %706, %707 dst: %void
  call  vm.builtin.null_value in:              dst: %703
  call  vm.builtin.null_value in:              dst: %704
  call  vm.builtin.make_tuple in: %705, %706, %707 dst: %708
  call  vm.builtin.reshape in: %705, c[163] dst: %709
  call  vm.builtin.reshape in: %706, c[163] dst: %710
  call  vm.builtin.reshape in: %707, c[163] dst: %711
  call  vm.builtin.alloc_tensor in: %329, i0, c[163], c[318] dst: %712
  call  multiply3        in: %709, %712   dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[165], c[319] dst: %713
  call  transpose13      in: %710, %713   dst: %void
  call  vm.builtin.null_value in:              dst: %706
  call  vm.builtin.null_value in:              dst: %710
  call  vm.builtin.alloc_tensor in: %315, i0, c[168], c[320] dst: %714
  call  matmul7          in: %712, %713, %714 dst: %void
  call  vm.builtin.null_value in:              dst: %712
  call  vm.builtin.null_value in:              dst: %713
  call  vm.builtin.reshape in: %81, c[170]  dst: %715
  call  vm.builtin.alloc_tensor in: %348, i0, c[171], c[321] dst: %716
  call  transpose14      in: %715, %716   dst: %void
  call  vm.builtin.null_value in:              dst: %715
  call  vm.builtin.reshape in: %716, c[173] dst: %717
  call  vm.builtin.alloc_tensor in: %351, i0, c[174], c[322] dst: %718
  call  transpose15      in: %717, %718   dst: %void
  call  vm.builtin.null_value in:              dst: %716
  call  vm.builtin.null_value in:              dst: %717
  call  vm.builtin.reshape in: c[176], c[177] dst: %719
  call  vm.builtin.reshape in: %719, c[177] dst: %720
  call  vm.builtin.null_value in:              dst: %719
  call  vm.builtin.reshape in: c[176], c[178] dst: %721
  call  vm.builtin.reshape in: %721, c[178] dst: %722
  call  vm.builtin.null_value in:              dst: %721
  call  vm.builtin.alloc_tensor in: %505, i0, c[181], c[323] dst: %723
  call  subtract1        in: %720, %722, %723 dst: %void
  call  vm.builtin.null_value in:              dst: %720
  call  vm.builtin.null_value in:              dst: %722
  call  vm.builtin.alloc_tensor in: %507, i0, c[181], c[324] dst: %724
  call  add10            in: %723, %724   dst: %void
  call  vm.builtin.null_value in:              dst: %723
  call  vm.builtin.alloc_tensor in: %509, i0, c[186], c[325] dst: %725
  call  take1            in: %718, %724, %725 dst: %void
  call  vm.builtin.null_value in:              dst: %718
  call  vm.builtin.null_value in:              dst: %724
  call  vm.builtin.reshape in: %82, c[170]  dst: %726
  call  vm.builtin.alloc_tensor in: %365, i0, c[171], c[326] dst: %727
  call  transpose14      in: %726, %727   dst: %void
  call  vm.builtin.null_value in:              dst: %726
  call  vm.builtin.reshape in: %727, c[173] dst: %728
  call  vm.builtin.alloc_tensor in: %348, i0, c[174], c[327] dst: %729
  call  transpose15      in: %728, %729   dst: %void
  call  vm.builtin.null_value in:              dst: %727
  call  vm.builtin.null_value in:              dst: %728
  call  vm.builtin.reshape in: c[176], c[177] dst: %730
  call  vm.builtin.reshape in: %730, c[177] dst: %731
  call  vm.builtin.null_value in:              dst: %730
  call  vm.builtin.reshape in: c[176], c[178] dst: %732
  call  vm.builtin.reshape in: %732, c[178] dst: %733
  call  vm.builtin.null_value in:              dst: %732
  call  vm.builtin.alloc_tensor in: %505, i0, c[181], c[328] dst: %734
  call  subtract1        in: %731, %733, %734 dst: %void
  call  vm.builtin.null_value in:              dst: %731
  call  vm.builtin.null_value in:              dst: %733
  call  vm.builtin.alloc_tensor in: %507, i0, c[181], c[329] dst: %735
  call  add10            in: %734, %735   dst: %void
  call  vm.builtin.null_value in:              dst: %734
  call  vm.builtin.alloc_storage in: %vm, c[66], i0, c[330], c[4] dst: %736
  call  vm.builtin.alloc_tensor in: %736, i0, c[186], c[331] dst: %737
  call  take1            in: %729, %735, %737 dst: %void
  call  vm.builtin.null_value in:              dst: %729
  call  vm.builtin.null_value in:              dst: %735
  call  vm.builtin.reshape in: %709, c[194] dst: %738
  call  vm.builtin.alloc_tensor in: %337, i0, c[194], c[332] dst: %739
  call  einsum2          in: %738, %725, %739 dst: %void
  call  vm.builtin.null_value in:              dst: %725
  call  vm.builtin.alloc_tensor in: %329, i0, c[194], c[333] dst: %740
  call  einsum3          in: %738, %737, %740 dst: %void
  call  vm.builtin.null_value in:              dst: %705
  call  vm.builtin.null_value in:              dst: %709
  call  vm.builtin.null_value in:              dst: %738
  call  vm.builtin.null_value in:              dst: %737
  call  vm.builtin.reshape in: %714, c[197] dst: %741
  call  vm.builtin.reshape in: %739, c[198] dst: %742
  call  vm.builtin.reshape in: %740, c[199] dst: %743
  call  vm.builtin.alloc_tensor in: %495, i0, c[197], c[334] dst: %744
  call  add11            in: %741, %742, %744 dst: %void
  call  vm.builtin.null_value in:              dst: %714
  call  vm.builtin.null_value in:              dst: %741
  call  vm.builtin.null_value in:              dst: %739
  call  vm.builtin.null_value in:              dst: %742
  call  vm.builtin.alloc_tensor in: %315, i0, c[197], c[335] dst: %745
  call  add12            in: %744, %743, %745 dst: %void
  call  vm.builtin.null_value in:              dst: %744
  call  vm.builtin.null_value in:              dst: %740
  call  vm.builtin.null_value in:              dst: %743
  call  vm.builtin.reshape in: %745, c[168] dst: %746
  call  vm.builtin.alloc_tensor in: %495, i0, c[168], c[336] dst: %747
  call  softmax1         in: %746, %747   dst: %void
  call  vm.builtin.null_value in:              dst: %745
  call  vm.builtin.null_value in:              dst: %746
  call  vm.builtin.alloc_tensor in: %521, i0, c[163], c[337] dst: %748
  call  matmul8          in: %747, %711, %748 dst: %void
  call  vm.builtin.null_value in:              dst: %747
  call  vm.builtin.null_value in:              dst: %707
  call  vm.builtin.null_value in:              dst: %711
  call  vm.builtin.reshape in: %748, c[204] dst: %749
  call  vm.builtin.alloc_tensor in: %337, i0, c[205], c[338] dst: %750
  call  transpose16      in: %749, %750   dst: %void
  call  vm.builtin.null_value in:              dst: %748
  call  vm.builtin.null_value in:              dst: %749
  call  vm.builtin.reshape in: %750, c[11]  dst: %751
  call  vm.builtin.alloc_tensor in: %509, i0, c[86], c[339] dst: %752
  call  transpose8       in: %79, %752    dst: %void
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[340] dst: %753
  call  matmul9          in: %751, %752, %753 dst: %void
  call  vm.builtin.null_value in:              dst: %750
  call  vm.builtin.null_value in:              dst: %751
  call  vm.builtin.null_value in:              dst: %752
  call  vm.builtin.alloc_tensor in: %329, i0, c[11], c[341] dst: %754
  call  add8             in: %753, %80, %754 dst: %void
  call  vm.builtin.null_value in:              dst: %753
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[342] dst: %755
  call  add1             in: %697, %754, %755 dst: %void
  call  vm.builtin.null_value in:              dst: %697
  call  vm.builtin.null_value in:              dst: %754
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[343] dst: %756
  call  layer_norm       in: %755, %83, %84, %756 dst: %void
  call  vm.builtin.alloc_tensor in: %337, i0, c[94], c[344] dst: %757
  call  transpose10      in: %85, %757    dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[345] dst: %758
  call  matmul4          in: %756, %757, %758 dst: %void
  call  vm.builtin.null_value in:              dst: %756
  call  vm.builtin.null_value in:              dst: %757
  call  vm.builtin.alloc_tensor in: %315, i0, c[96], c[346] dst: %759
  call  add7             in: %758, %86, %759 dst: %void
  call  vm.builtin.null_value in:              dst: %758
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[347] dst: %760
  call  gelu             in: %759, %760   dst: %void
  call  vm.builtin.null_value in:              dst: %759
  call  vm.builtin.alloc_tensor in: %344, i0, c[100], c[348] dst: %761
  call  transpose11      in: %87, %761    dst: %void
  call  vm.builtin.alloc_tensor in: %329, i0, c[11], c[349] dst: %762
  call  matmul5          in: %760, %761, %762 dst: %void
  call  vm.builtin.null_value in:              dst: %760
  call  vm.builtin.null_value in:              dst: %761
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[350] dst: %763
  call  add8             in: %762, %88, %763 dst: %void
  call  vm.builtin.null_value in:              dst: %762
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[351] dst: %764
  call  add1             in: %755, %763, %764 dst: %void
  call  vm.builtin.null_value in:              dst: %755
  call  vm.builtin.null_value in:              dst: %763
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[352] dst: %765
  call  layer_norm       in: %764, %89, %90, %765 dst: %void
  call  vm.builtin.alloc_tensor in: %344, i0, c[17], c[353] dst: %766
  call  pad              in: %765, %766   dst: %void
  call  vm.builtin.null_value in:              dst: %765
  call  vm.builtin.reshape in: %766, c[19]  dst: %767
  call  vm.builtin.alloc_tensor in: %521, i0, c[20], c[354] dst: %768
  call  transpose1       in: %767, %768   dst: %void
  call  vm.builtin.null_value in:              dst: %766
  call  vm.builtin.null_value in:              dst: %767
  call  vm.builtin.reshape in: %768, c[22]  dst: %769
  call  vm.builtin.alloc_tensor in: %329, i0, c[23], c[355] dst: %770
  call  transpose2       in: %91, %770    dst: %void
  call  vm.builtin.alloc_tensor in: %318, i0, c[26], c[356] dst: %771
  call  matmul           in: %769, %770, %771 dst: %void
  call  vm.builtin.null_value in:              dst: %768
  call  vm.builtin.null_value in:              dst: %769
  call  vm.builtin.null_value in:              dst: %770
  call  vm.builtin.alloc_tensor in: %344, i0, c[26], c[357] dst: %772
  call  add2             in: %771, %92, %772 dst: %void
  call  vm.builtin.null_value in:              dst: %771
  call  vm.builtin.reshape in: %772, c[29]  dst: %773
  call  vm.builtin.alloc_tensor in: %329, i0, c[30], c[358] dst: %774
  call  transpose3       in: %773, %774   dst: %void
  call  vm.builtin.null_value in:              dst: %772
  call  vm.builtin.null_value in:              dst: %773
  call  vm.builtin.reshape in: %774, c[32]  dst: %775
  call  vm.builtin.alloc_tensor in: %521, i0, c[33], c[359] dst: %776
  call  vm.builtin.alloc_tensor in: %318, i0, c[33], c[360] dst: %777
  call  vm.builtin.alloc_tensor in: %344, i0, c[33], c[361] dst: %778
  call  split            in: %775, %776, %777, %778 dst: %void
  call  vm.builtin.null_value in:              dst: %774
  call  vm.builtin.null_value in:              dst: %775
  call  vm.builtin.make_tuple in: %776, %777, %778 dst: %779
  call  vm.builtin.reshape in: %776, c[38]  dst: %780
  call  vm.builtin.reshape in: %777, c[38]  dst: %781
  call  vm.builtin.reshape in: %778, c[38]  dst: %782
  call  vm.builtin.alloc_tensor in: %329, i0, c[38], c[362] dst: %783
  call  multiply         in: %780, %783   dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[41], c[363] dst: %784
  call  transpose4       in: %781, %784   dst: %void
  call  vm.builtin.null_value in:              dst: %777
  call  vm.builtin.null_value in:              dst: %781
  call  vm.builtin.alloc_tensor in: %318, i0, c[43], c[364] dst: %785
  call  matmul1          in: %783, %784, %785 dst: %void
  call  vm.builtin.null_value in:              dst: %783
  call  vm.builtin.null_value in:              dst: %784
  call  vm.builtin.reshape in: %95, c[45]   dst: %786
  call  vm.builtin.alloc_tensor in: %351, i0, c[48], c[365] dst: %787
  call  transpose5       in: %786, %787   dst: %void
  call  vm.builtin.null_value in:              dst: %786
  call  vm.builtin.reshape in: %787, c[50]  dst: %788
  call  vm.builtin.alloc_tensor in: %365, i0, c[52], c[366] dst: %789
  call  transpose6       in: %788, %789   dst: %void
  call  vm.builtin.null_value in:              dst: %787
  call  vm.builtin.null_value in:              dst: %788
  call  vm.builtin.reshape in: c[54], c[55] dst: %790
  call  vm.builtin.reshape in: %790, c[55]  dst: %791
  call  vm.builtin.null_value in:              dst: %790
  call  vm.builtin.reshape in: c[54], c[56] dst: %792
  call  vm.builtin.reshape in: %792, c[56]  dst: %793
  call  vm.builtin.null_value in:              dst: %792
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[367] dst: %794
  call  subtract         in: %791, %793, %794 dst: %void
  call  vm.builtin.null_value in:              dst: %791
  call  vm.builtin.null_value in:              dst: %793
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[368] dst: %795
  call  add3             in: %794, %795   dst: %void
  call  vm.builtin.null_value in:              dst: %794
  call  vm.builtin.alloc_tensor in: %348, i0, c[63], c[369] dst: %796
  call  take             in: %789, %795, %796 dst: %void
  call  vm.builtin.null_value in:              dst: %789
  call  vm.builtin.null_value in:              dst: %795
  call  vm.builtin.reshape in: %96, c[45]   dst: %797
  call  vm.builtin.alloc_tensor in: %351, i0, c[48], c[370] dst: %798
  call  transpose5       in: %797, %798   dst: %void
  call  vm.builtin.null_value in:              dst: %797
  call  vm.builtin.reshape in: %798, c[50]  dst: %799
  call  vm.builtin.alloc_tensor in: %365, i0, c[52], c[371] dst: %800
  call  transpose6       in: %799, %800   dst: %void
  call  vm.builtin.null_value in:              dst: %798
  call  vm.builtin.null_value in:              dst: %799
  call  vm.builtin.reshape in: c[54], c[55] dst: %801
  call  vm.builtin.reshape in: %801, c[55]  dst: %802
  call  vm.builtin.null_value in:              dst: %801
  call  vm.builtin.reshape in: c[54], c[56] dst: %803
  call  vm.builtin.reshape in: %803, c[56]  dst: %804
  call  vm.builtin.null_value in:              dst: %803
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[372] dst: %805
  call  subtract         in: %802, %804, %805 dst: %void
  call  vm.builtin.null_value in:              dst: %802
  call  vm.builtin.null_value in:              dst: %804
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[373] dst: %806
  call  add3             in: %805, %806   dst: %void
  call  vm.builtin.null_value in:              dst: %805
  call  vm.builtin.alloc_tensor in: %351, i0, c[63], c[374] dst: %807
  call  take             in: %800, %806, %807 dst: %void
  call  vm.builtin.null_value in:              dst: %800
  call  vm.builtin.null_value in:              dst: %806
  call  vm.builtin.reshape in: %780, c[72]  dst: %808
  call  vm.builtin.alloc_tensor in: %329, i0, c[73], c[375] dst: %809
  call  einsum           in: %808, %796, %809 dst: %void
  call  vm.builtin.null_value in:              dst: %796
  call  vm.builtin.alloc_tensor in: %323, i0, c[73], c[376] dst: %810
  call  einsum1          in: %808, %807, %810 dst: %void
  call  vm.builtin.null_value in:              dst: %776
  call  vm.builtin.null_value in:              dst: %780
  call  vm.builtin.null_value in:              dst: %808
  call  vm.builtin.null_value in:              dst: %807
  call  vm.builtin.reshape in: %785, c[76]  dst: %811
  call  vm.builtin.reshape in: %809, c[77]  dst: %812
  call  vm.builtin.reshape in: %810, c[78]  dst: %813
  call  vm.builtin.alloc_tensor in: %521, i0, c[76], c[377] dst: %814
  call  add4             in: %811, %812, %814 dst: %void
  call  vm.builtin.null_value in:              dst: %785
  call  vm.builtin.null_value in:              dst: %811
  call  vm.builtin.null_value in:              dst: %809
  call  vm.builtin.null_value in:              dst: %812
  call  vm.builtin.alloc_tensor in: %318, i0, c[76], c[378] dst: %815
  call  add5             in: %814, %813, %815 dst: %void
  call  vm.builtin.null_value in:              dst: %814
  call  vm.builtin.null_value in:              dst: %810
  call  vm.builtin.null_value in:              dst: %813
  call  vm.builtin.reshape in: %815, c[43]  dst: %816
  call  vm.builtin.alloc_tensor in: %329, i0, c[43], c[379] dst: %817
  call  softmax          in: %816, %817   dst: %void
  call  vm.builtin.null_value in:              dst: %815
  call  vm.builtin.null_value in:              dst: %816
  call  vm.builtin.alloc_tensor in: %521, i0, c[38], c[380] dst: %818
  call  matmul2          in: %817, %782, %818 dst: %void
  call  vm.builtin.null_value in:              dst: %817
  call  vm.builtin.null_value in:              dst: %778
  call  vm.builtin.null_value in:              dst: %782
  call  vm.builtin.reshape in: %818, c[83]  dst: %819
  call  vm.builtin.alloc_tensor in: %318, i0, c[84], c[381] dst: %820
  call  transpose7       in: %819, %820   dst: %void
  call  vm.builtin.null_value in:              dst: %818
  call  vm.builtin.null_value in:              dst: %819
  call  vm.builtin.reshape in: %820, c[22]  dst: %821
  call  vm.builtin.alloc_tensor in: %509, i0, c[86], c[382] dst: %822
  call  transpose8       in: %93, %822    dst: %void
  call  vm.builtin.alloc_tensor in: %329, i0, c[22], c[383] dst: %823
  call  matmul3          in: %821, %822, %823 dst: %void
  call  vm.builtin.null_value in:              dst: %820
  call  vm.builtin.null_value in:              dst: %821
  call  vm.builtin.null_value in:              dst: %822
  call  vm.builtin.alloc_tensor in: %344, i0, c[22], c[384] dst: %824
  call  add6             in: %823, %94, %824 dst: %void
  call  vm.builtin.null_value in:              dst: %823
  call  vm.builtin.reshape in: %824, c[20]  dst: %825
  call  vm.builtin.alloc_tensor in: %521, i0, c[19], c[385] dst: %826
  call  transpose9       in: %825, %826   dst: %void
  call  vm.builtin.null_value in:              dst: %824
  call  vm.builtin.null_value in:              dst: %825
  call  vm.builtin.reshape in: %826, c[17]  dst: %827
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[386] dst: %828
  call  strided_slice    in: %827, %828   dst: %void
  call  vm.builtin.null_value in:              dst: %826
  call  vm.builtin.null_value in:              dst: %827
  call  vm.builtin.alloc_tensor in: %329, i0, c[11], c[387] dst: %829
  call  add1             in: %764, %828, %829 dst: %void
  call  vm.builtin.null_value in:              dst: %764
  call  vm.builtin.null_value in:              dst: %828
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[388] dst: %830
  call  layer_norm       in: %829, %97, %98, %830 dst: %void
  call  vm.builtin.alloc_tensor in: %521, i0, c[94], c[389] dst: %831
  call  transpose10      in: %99, %831    dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[390] dst: %832
  call  matmul4          in: %830, %831, %832 dst: %void
  call  vm.builtin.null_value in:              dst: %830
  call  vm.builtin.null_value in:              dst: %831
  call  vm.builtin.alloc_tensor in: %495, i0, c[96], c[391] dst: %833
  call  add7             in: %832, %100, %833 dst: %void
  call  vm.builtin.null_value in:              dst: %832
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[392] dst: %834
  call  gelu             in: %833, %834   dst: %void
  call  vm.builtin.null_value in:              dst: %833
  call  vm.builtin.alloc_tensor in: %337, i0, c[100], c[393] dst: %835
  call  transpose11      in: %101, %835   dst: %void
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[394] dst: %836
  call  matmul5          in: %834, %835, %836 dst: %void
  call  vm.builtin.null_value in:              dst: %834
  call  vm.builtin.null_value in:              dst: %835
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[395] dst: %837
  call  add8             in: %836, %102, %837 dst: %void
  call  vm.builtin.null_value in:              dst: %836
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[396] dst: %838
  call  add1             in: %829, %837, %838 dst: %void
  call  vm.builtin.null_value in:              dst: %829
  call  vm.builtin.null_value in:              dst: %837
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[397] dst: %839
  call  layer_norm       in: %838, %103, %104, %839 dst: %void
  call  vm.builtin.alloc_tensor in: %318, i0, c[17], c[398] dst: %840
  call  pad              in: %839, %840   dst: %void
  call  vm.builtin.null_value in:              dst: %839
  call  vm.builtin.reshape in: %840, c[19]  dst: %841
  call  vm.builtin.alloc_tensor in: %329, i0, c[20], c[399] dst: %842
  call  transpose1       in: %841, %842   dst: %void
  call  vm.builtin.null_value in:              dst: %840
  call  vm.builtin.null_value in:              dst: %841
  call  vm.builtin.reshape in: %842, c[22]  dst: %843
  call  vm.builtin.alloc_tensor in: %344, i0, c[23], c[400] dst: %844
  call  transpose2       in: %105, %844   dst: %void
  call  vm.builtin.alloc_tensor in: %337, i0, c[26], c[401] dst: %845
  call  matmul           in: %843, %844, %845 dst: %void
  call  vm.builtin.null_value in:              dst: %842
  call  vm.builtin.null_value in:              dst: %843
  call  vm.builtin.null_value in:              dst: %844
  call  vm.builtin.alloc_tensor in: %318, i0, c[26], c[402] dst: %846
  call  add2             in: %845, %106, %846 dst: %void
  call  vm.builtin.null_value in:              dst: %845
  call  vm.builtin.reshape in: %846, c[29]  dst: %847
  call  vm.builtin.alloc_tensor in: %329, i0, c[30], c[403] dst: %848
  call  transpose3       in: %847, %848   dst: %void
  call  vm.builtin.null_value in:              dst: %846
  call  vm.builtin.null_value in:              dst: %847
  call  vm.builtin.reshape in: %848, c[32]  dst: %849
  call  vm.builtin.alloc_tensor in: %344, i0, c[33], c[404] dst: %850
  call  vm.builtin.alloc_tensor in: %337, i0, c[33], c[405] dst: %851
  call  vm.builtin.alloc_tensor in: %318, i0, c[33], c[406] dst: %852
  call  split            in: %849, %850, %851, %852 dst: %void
  call  vm.builtin.null_value in:              dst: %848
  call  vm.builtin.null_value in:              dst: %849
  call  vm.builtin.make_tuple in: %850, %851, %852 dst: %853
  call  vm.builtin.reshape in: %850, c[38]  dst: %854
  call  vm.builtin.reshape in: %851, c[38]  dst: %855
  call  vm.builtin.reshape in: %852, c[38]  dst: %856
  call  vm.builtin.alloc_tensor in: %329, i0, c[38], c[407] dst: %857
  call  multiply         in: %854, %857   dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[41], c[408] dst: %858
  call  transpose4       in: %855, %858   dst: %void
  call  vm.builtin.null_value in:              dst: %851
  call  vm.builtin.null_value in:              dst: %855
  call  vm.builtin.alloc_tensor in: %337, i0, c[43], c[409] dst: %859
  call  matmul1          in: %857, %858, %859 dst: %void
  call  vm.builtin.null_value in:              dst: %857
  call  vm.builtin.null_value in:              dst: %858
  call  vm.builtin.reshape in: %109, c[45]  dst: %860
  call  vm.builtin.alloc_tensor in: %365, i0, c[48], c[410] dst: %861
  call  transpose5       in: %860, %861   dst: %void
  call  vm.builtin.null_value in:              dst: %860
  call  vm.builtin.reshape in: %861, c[50]  dst: %862
  call  vm.builtin.alloc_tensor in: %348, i0, c[52], c[411] dst: %863
  call  transpose6       in: %862, %863   dst: %void
  call  vm.builtin.null_value in:              dst: %861
  call  vm.builtin.null_value in:              dst: %862
  call  vm.builtin.reshape in: c[54], c[55] dst: %864
  call  vm.builtin.reshape in: %864, c[55]  dst: %865
  call  vm.builtin.null_value in:              dst: %864
  call  vm.builtin.reshape in: c[54], c[56] dst: %866
  call  vm.builtin.reshape in: %866, c[56]  dst: %867
  call  vm.builtin.null_value in:              dst: %866
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[412] dst: %868
  call  subtract         in: %865, %867, %868 dst: %void
  call  vm.builtin.null_value in:              dst: %865
  call  vm.builtin.null_value in:              dst: %867
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[413] dst: %869
  call  add3             in: %868, %869   dst: %void
  call  vm.builtin.null_value in:              dst: %868
  call  vm.builtin.alloc_tensor in: %351, i0, c[63], c[414] dst: %870
  call  take             in: %863, %869, %870 dst: %void
  call  vm.builtin.null_value in:              dst: %863
  call  vm.builtin.null_value in:              dst: %869
  call  vm.builtin.reshape in: %110, c[45]  dst: %871
  call  vm.builtin.alloc_tensor in: %365, i0, c[48], c[415] dst: %872
  call  transpose5       in: %871, %872   dst: %void
  call  vm.builtin.null_value in:              dst: %871
  call  vm.builtin.reshape in: %872, c[50]  dst: %873
  call  vm.builtin.alloc_tensor in: %348, i0, c[52], c[416] dst: %874
  call  transpose6       in: %873, %874   dst: %void
  call  vm.builtin.null_value in:              dst: %872
  call  vm.builtin.null_value in:              dst: %873
  call  vm.builtin.reshape in: c[54], c[55] dst: %875
  call  vm.builtin.reshape in: %875, c[55]  dst: %876
  call  vm.builtin.null_value in:              dst: %875
  call  vm.builtin.reshape in: c[54], c[56] dst: %877
  call  vm.builtin.reshape in: %877, c[56]  dst: %878
  call  vm.builtin.null_value in:              dst: %877
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[417] dst: %879
  call  subtract         in: %876, %878, %879 dst: %void
  call  vm.builtin.null_value in:              dst: %876
  call  vm.builtin.null_value in:              dst: %878
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[418] dst: %880
  call  add3             in: %879, %880   dst: %void
  call  vm.builtin.null_value in:              dst: %879
  call  vm.builtin.alloc_tensor in: %365, i0, c[63], c[419] dst: %881
  call  take             in: %874, %880, %881 dst: %void
  call  vm.builtin.null_value in:              dst: %874
  call  vm.builtin.null_value in:              dst: %880
  call  vm.builtin.reshape in: %854, c[72]  dst: %882
  call  vm.builtin.alloc_tensor in: %329, i0, c[73], c[420] dst: %883
  call  einsum           in: %882, %870, %883 dst: %void
  call  vm.builtin.null_value in:              dst: %870
  call  vm.builtin.alloc_tensor in: %323, i0, c[73], c[421] dst: %884
  call  einsum1          in: %882, %881, %884 dst: %void
  call  vm.builtin.null_value in:              dst: %850
  call  vm.builtin.null_value in:              dst: %854
  call  vm.builtin.null_value in:              dst: %882
  call  vm.builtin.null_value in:              dst: %881
  call  vm.builtin.reshape in: %859, c[76]  dst: %885
  call  vm.builtin.reshape in: %883, c[77]  dst: %886
  call  vm.builtin.reshape in: %884, c[78]  dst: %887
  call  vm.builtin.alloc_tensor in: %344, i0, c[76], c[422] dst: %888
  call  add4             in: %885, %886, %888 dst: %void
  call  vm.builtin.null_value in:              dst: %859
  call  vm.builtin.null_value in:              dst: %885
  call  vm.builtin.null_value in:              dst: %883
  call  vm.builtin.null_value in:              dst: %886
  call  vm.builtin.alloc_tensor in: %337, i0, c[76], c[423] dst: %889
  call  add5             in: %888, %887, %889 dst: %void
  call  vm.builtin.null_value in:              dst: %888
  call  vm.builtin.null_value in:              dst: %884
  call  vm.builtin.null_value in:              dst: %887
  call  vm.builtin.reshape in: %889, c[43]  dst: %890
  call  vm.builtin.alloc_tensor in: %329, i0, c[43], c[424] dst: %891
  call  softmax          in: %890, %891   dst: %void
  call  vm.builtin.null_value in:              dst: %889
  call  vm.builtin.null_value in:              dst: %890
  call  vm.builtin.alloc_tensor in: %344, i0, c[38], c[425] dst: %892
  call  matmul2          in: %891, %856, %892 dst: %void
  call  vm.builtin.null_value in:              dst: %891
  call  vm.builtin.null_value in:              dst: %852
  call  vm.builtin.null_value in:              dst: %856
  call  vm.builtin.reshape in: %892, c[83]  dst: %893
  call  vm.builtin.alloc_tensor in: %337, i0, c[84], c[426] dst: %894
  call  transpose7       in: %893, %894   dst: %void
  call  vm.builtin.null_value in:              dst: %892
  call  vm.builtin.null_value in:              dst: %893
  call  vm.builtin.reshape in: %894, c[22]  dst: %895
  call  vm.builtin.alloc_tensor in: %509, i0, c[86], c[427] dst: %896
  call  transpose8       in: %107, %896   dst: %void
  call  vm.builtin.alloc_tensor in: %329, i0, c[22], c[428] dst: %897
  call  matmul3          in: %895, %896, %897 dst: %void
  call  vm.builtin.null_value in:              dst: %894
  call  vm.builtin.null_value in:              dst: %895
  call  vm.builtin.null_value in:              dst: %896
  call  vm.builtin.alloc_tensor in: %318, i0, c[22], c[429] dst: %898
  call  add6             in: %897, %108, %898 dst: %void
  call  vm.builtin.null_value in:              dst: %897
  call  vm.builtin.reshape in: %898, c[20]  dst: %899
  call  vm.builtin.alloc_tensor in: %344, i0, c[19], c[430] dst: %900
  call  transpose9       in: %899, %900   dst: %void
  call  vm.builtin.null_value in:              dst: %898
  call  vm.builtin.null_value in:              dst: %899
  call  vm.builtin.reshape in: %900, c[17]  dst: %901
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[431] dst: %902
  call  strided_slice    in: %901, %902   dst: %void
  call  vm.builtin.null_value in:              dst: %900
  call  vm.builtin.null_value in:              dst: %901
  call  vm.builtin.alloc_tensor in: %329, i0, c[11], c[432] dst: %903
  call  add1             in: %838, %902, %903 dst: %void
  call  vm.builtin.null_value in:              dst: %838
  call  vm.builtin.null_value in:              dst: %902
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[433] dst: %904
  call  layer_norm       in: %903, %111, %112, %904 dst: %void
  call  vm.builtin.alloc_tensor in: %344, i0, c[94], c[434] dst: %905
  call  transpose10      in: %113, %905   dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[435] dst: %906
  call  matmul4          in: %904, %905, %906 dst: %void
  call  vm.builtin.null_value in:              dst: %904
  call  vm.builtin.null_value in:              dst: %905
  call  vm.builtin.alloc_tensor in: %315, i0, c[96], c[436] dst: %907
  call  add7             in: %906, %114, %907 dst: %void
  call  vm.builtin.null_value in:              dst: %906
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[437] dst: %908
  call  gelu             in: %907, %908   dst: %void
  call  vm.builtin.null_value in:              dst: %907
  call  vm.builtin.alloc_tensor in: %521, i0, c[100], c[438] dst: %909
  call  transpose11      in: %115, %909   dst: %void
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[439] dst: %910
  call  matmul5          in: %908, %909, %910 dst: %void
  call  vm.builtin.null_value in:              dst: %908
  call  vm.builtin.null_value in:              dst: %909
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[440] dst: %911
  call  add8             in: %910, %116, %911 dst: %void
  call  vm.builtin.null_value in:              dst: %910
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[441] dst: %912
  call  add1             in: %903, %911, %912 dst: %void
  call  vm.builtin.null_value in:              dst: %903
  call  vm.builtin.null_value in:              dst: %911
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[442] dst: %913
  call  layer_norm       in: %912, %117, %118, %913 dst: %void
  call  vm.builtin.alloc_tensor in: %337, i0, c[23], c[443] dst: %914
  call  transpose2       in: %119, %914   dst: %void
  call  vm.builtin.alloc_tensor in: %329, i0, c[152], c[444] dst: %915
  call  matmul6          in: %913, %914, %915 dst: %void
  call  vm.builtin.null_value in:              dst: %913
  call  vm.builtin.null_value in:              dst: %914
  call  vm.builtin.alloc_tensor in: %318, i0, c[152], c[445] dst: %916
  call  add9             in: %915, %120, %916 dst: %void
  call  vm.builtin.null_value in:              dst: %915
  call  vm.builtin.reshape in: %916, c[155] dst: %917
  call  vm.builtin.alloc_tensor in: %521, i0, c[156], c[446] dst: %918
  call  transpose12      in: %917, %918   dst: %void
  call  vm.builtin.null_value in:              dst: %916
  call  vm.builtin.null_value in:              dst: %917
  call  vm.builtin.reshape in: %918, c[158] dst: %919
  call  vm.builtin.alloc_tensor in: %337, i0, c[159], c[447] dst: %920
  call  vm.builtin.alloc_tensor in: %329, i0, c[159], c[448] dst: %921
  call  vm.builtin.alloc_tensor in: %318, i0, c[159], c[449] dst: %922
  call  split1           in: %919, %920, %921, %922 dst: %void
  call  vm.builtin.null_value in:              dst: %918
  call  vm.builtin.null_value in:              dst: %919
  call  vm.builtin.make_tuple in: %920, %921, %922 dst: %923
  call  vm.builtin.reshape in: %920, c[163] dst: %924
  call  vm.builtin.reshape in: %921, c[163] dst: %925
  call  vm.builtin.reshape in: %922, c[163] dst: %926
  call  vm.builtin.alloc_tensor in: %521, i0, c[163], c[450] dst: %927
  call  multiply3        in: %924, %927   dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[165], c[451] dst: %928
  call  transpose13      in: %925, %928   dst: %void
  call  vm.builtin.null_value in:              dst: %921
  call  vm.builtin.null_value in:              dst: %925
  call  vm.builtin.alloc_tensor in: %495, i0, c[168], c[452] dst: %929
  call  matmul7          in: %927, %928, %929 dst: %void
  call  vm.builtin.null_value in:              dst: %927
  call  vm.builtin.null_value in:              dst: %928
  call  vm.builtin.reshape in: %123, c[170] dst: %930
  call  vm.builtin.alloc_tensor in: %348, i0, c[171], c[453] dst: %931
  call  transpose14      in: %930, %931   dst: %void
  call  vm.builtin.null_value in:              dst: %930
  call  vm.builtin.reshape in: %931, c[173] dst: %932
  call  vm.builtin.alloc_tensor in: %351, i0, c[174], c[454] dst: %933
  call  transpose15      in: %932, %933   dst: %void
  call  vm.builtin.null_value in:              dst: %931
  call  vm.builtin.null_value in:              dst: %932
  call  vm.builtin.reshape in: c[176], c[177] dst: %934
  call  vm.builtin.reshape in: %934, c[177] dst: %935
  call  vm.builtin.null_value in:              dst: %934
  call  vm.builtin.reshape in: c[176], c[178] dst: %936
  call  vm.builtin.reshape in: %936, c[178] dst: %937
  call  vm.builtin.null_value in:              dst: %936
  call  vm.builtin.alloc_tensor in: %505, i0, c[181], c[455] dst: %938
  call  subtract1        in: %935, %937, %938 dst: %void
  call  vm.builtin.null_value in:              dst: %935
  call  vm.builtin.null_value in:              dst: %937
  call  vm.builtin.alloc_tensor in: %507, i0, c[181], c[456] dst: %939
  call  add10            in: %938, %939   dst: %void
  call  vm.builtin.null_value in:              dst: %938
  call  vm.builtin.alloc_tensor in: %736, i0, c[186], c[457] dst: %940
  call  take1            in: %933, %939, %940 dst: %void
  call  vm.builtin.null_value in:              dst: %933
  call  vm.builtin.null_value in:              dst: %939
  call  vm.builtin.reshape in: %124, c[170] dst: %941
  call  vm.builtin.alloc_tensor in: %365, i0, c[171], c[458] dst: %942
  call  transpose14      in: %941, %942   dst: %void
  call  vm.builtin.null_value in:              dst: %941
  call  vm.builtin.reshape in: %942, c[173] dst: %943
  call  vm.builtin.alloc_tensor in: %348, i0, c[174], c[459] dst: %944
  call  transpose15      in: %943, %944   dst: %void
  call  vm.builtin.null_value in:              dst: %942
  call  vm.builtin.null_value in:              dst: %943
  call  vm.builtin.reshape in: c[176], c[177] dst: %945
  call  vm.builtin.reshape in: %945, c[177] dst: %946
  call  vm.builtin.null_value in:              dst: %945
  call  vm.builtin.reshape in: c[176], c[178] dst: %947
  call  vm.builtin.reshape in: %947, c[178] dst: %948
  call  vm.builtin.null_value in:              dst: %947
  call  vm.builtin.alloc_tensor in: %505, i0, c[181], c[460] dst: %949
  call  subtract1        in: %946, %948, %949 dst: %void
  call  vm.builtin.null_value in:              dst: %946
  call  vm.builtin.null_value in:              dst: %948
  call  vm.builtin.alloc_tensor in: %507, i0, c[181], c[461] dst: %950
  call  add10            in: %949, %950   dst: %void
  call  vm.builtin.null_value in:              dst: %949
  call  vm.builtin.alloc_tensor in: %509, i0, c[186], c[462] dst: %951
  call  take1            in: %944, %950, %951 dst: %void
  call  vm.builtin.null_value in:              dst: %944
  call  vm.builtin.null_value in:              dst: %950
  call  vm.builtin.reshape in: %924, c[194] dst: %952
  call  vm.builtin.alloc_tensor in: %329, i0, c[194], c[463] dst: %953
  call  einsum2          in: %952, %940, %953 dst: %void
  call  vm.builtin.null_value in:              dst: %940
  call  vm.builtin.alloc_tensor in: %521, i0, c[194], c[464] dst: %954
  call  einsum3          in: %952, %951, %954 dst: %void
  call  vm.builtin.null_value in:              dst: %920
  call  vm.builtin.null_value in:              dst: %924
  call  vm.builtin.null_value in:              dst: %952
  call  vm.builtin.null_value in:              dst: %951
  call  vm.builtin.reshape in: %929, c[197] dst: %955
  call  vm.builtin.reshape in: %953, c[198] dst: %956
  call  vm.builtin.reshape in: %954, c[199] dst: %957
  call  vm.builtin.alloc_tensor in: %315, i0, c[197], c[465] dst: %958
  call  add11            in: %955, %956, %958 dst: %void
  call  vm.builtin.null_value in:              dst: %929
  call  vm.builtin.null_value in:              dst: %955
  call  vm.builtin.null_value in:              dst: %953
  call  vm.builtin.null_value in:              dst: %956
  call  vm.builtin.alloc_tensor in: %495, i0, c[197], c[466] dst: %959
  call  add12            in: %958, %957, %959 dst: %void
  call  vm.builtin.null_value in:              dst: %958
  call  vm.builtin.null_value in:              dst: %954
  call  vm.builtin.null_value in:              dst: %957
  call  vm.builtin.reshape in: %959, c[168] dst: %960
  call  vm.builtin.alloc_tensor in: %315, i0, c[168], c[467] dst: %961
  call  softmax1         in: %960, %961   dst: %void
  call  vm.builtin.null_value in:              dst: %959
  call  vm.builtin.null_value in:              dst: %960
  call  vm.builtin.alloc_tensor in: %337, i0, c[163], c[468] dst: %962
  call  matmul8          in: %961, %926, %962 dst: %void
  call  vm.builtin.null_value in:              dst: %961
  call  vm.builtin.null_value in:              dst: %922
  call  vm.builtin.null_value in:              dst: %926
  call  vm.builtin.reshape in: %962, c[204] dst: %963
  call  vm.builtin.alloc_tensor in: %329, i0, c[205], c[469] dst: %964
  call  transpose16      in: %963, %964   dst: %void
  call  vm.builtin.null_value in:              dst: %962
  call  vm.builtin.null_value in:              dst: %963
  call  vm.builtin.reshape in: %964, c[11]  dst: %965
  call  vm.builtin.alloc_tensor in: %509, i0, c[86], c[470] dst: %966
  call  transpose8       in: %121, %966   dst: %void
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[471] dst: %967
  call  matmul9          in: %965, %966, %967 dst: %void
  call  vm.builtin.null_value in:              dst: %964
  call  vm.builtin.null_value in:              dst: %965
  call  vm.builtin.null_value in:              dst: %966
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[472] dst: %968
  call  add8             in: %967, %122, %968 dst: %void
  call  vm.builtin.null_value in:              dst: %967
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[473] dst: %969
  call  add1             in: %912, %968, %969 dst: %void
  call  vm.builtin.null_value in:              dst: %912
  call  vm.builtin.null_value in:              dst: %968
  call  vm.builtin.alloc_tensor in: %329, i0, c[11], c[474] dst: %970
  call  layer_norm       in: %969, %125, %126, %970 dst: %void
  call  vm.builtin.alloc_tensor in: %521, i0, c[94], c[475] dst: %971
  call  transpose10      in: %127, %971   dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[476] dst: %972
  call  matmul4          in: %970, %971, %972 dst: %void
  call  vm.builtin.null_value in:              dst: %970
  call  vm.builtin.null_value in:              dst: %971
  call  vm.builtin.alloc_tensor in: %495, i0, c[96], c[477] dst: %973
  call  add7             in: %972, %128, %973 dst: %void
  call  vm.builtin.null_value in:              dst: %972
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[478] dst: %974
  call  gelu             in: %973, %974   dst: %void
  call  vm.builtin.null_value in:              dst: %973
  call  vm.builtin.alloc_tensor in: %344, i0, c[100], c[479] dst: %975
  call  transpose11      in: %129, %975   dst: %void
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[480] dst: %976
  call  matmul5          in: %974, %975, %976 dst: %void
  call  vm.builtin.null_value in:              dst: %974
  call  vm.builtin.null_value in:              dst: %975
  call  vm.builtin.alloc_tensor in: %329, i0, c[11], c[481] dst: %977
  call  add8             in: %976, %130, %977 dst: %void
  call  vm.builtin.null_value in:              dst: %976
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[482] dst: %978
  call  add1             in: %969, %977, %978 dst: %void
  call  vm.builtin.null_value in:              dst: %969
  call  vm.builtin.null_value in:              dst: %977
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[483] dst: %979
  call  layer_norm       in: %978, %131, %132, %979 dst: %void
  call  vm.builtin.alloc_tensor in: %318, i0, c[17], c[484] dst: %980
  call  pad              in: %979, %980   dst: %void
  call  vm.builtin.null_value in:              dst: %979
  call  vm.builtin.reshape in: %980, c[19]  dst: %981
  call  vm.builtin.alloc_tensor in: %337, i0, c[20], c[485] dst: %982
  call  transpose1       in: %981, %982   dst: %void
  call  vm.builtin.null_value in:              dst: %980
  call  vm.builtin.null_value in:              dst: %981
  call  vm.builtin.reshape in: %982, c[22]  dst: %983
  call  vm.builtin.alloc_tensor in: %329, i0, c[23], c[486] dst: %984
  call  transpose2       in: %133, %984   dst: %void
  call  vm.builtin.alloc_tensor in: %344, i0, c[26], c[487] dst: %985
  call  matmul           in: %983, %984, %985 dst: %void
  call  vm.builtin.null_value in:              dst: %982
  call  vm.builtin.null_value in:              dst: %983
  call  vm.builtin.null_value in:              dst: %984
  call  vm.builtin.alloc_tensor in: %318, i0, c[26], c[488] dst: %986
  call  add2             in: %985, %134, %986 dst: %void
  call  vm.builtin.null_value in:              dst: %985
  call  vm.builtin.reshape in: %986, c[29]  dst: %987
  call  vm.builtin.alloc_tensor in: %337, i0, c[30], c[489] dst: %988
  call  transpose3       in: %987, %988   dst: %void
  call  vm.builtin.null_value in:              dst: %986
  call  vm.builtin.null_value in:              dst: %987
  call  vm.builtin.reshape in: %988, c[32]  dst: %989
  call  vm.builtin.alloc_tensor in: %329, i0, c[33], c[490] dst: %990
  call  vm.builtin.alloc_tensor in: %344, i0, c[33], c[491] dst: %991
  call  vm.builtin.alloc_tensor in: %318, i0, c[33], c[492] dst: %992
  call  split            in: %989, %990, %991, %992 dst: %void
  call  vm.builtin.null_value in:              dst: %988
  call  vm.builtin.null_value in:              dst: %989
  call  vm.builtin.make_tuple in: %990, %991, %992 dst: %993
  call  vm.builtin.reshape in: %990, c[38]  dst: %994
  call  vm.builtin.reshape in: %991, c[38]  dst: %995
  call  vm.builtin.reshape in: %992, c[38]  dst: %996
  call  vm.builtin.alloc_tensor in: %337, i0, c[38], c[493] dst: %997
  call  multiply         in: %994, %997   dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[41], c[494] dst: %998
  call  transpose4       in: %995, %998   dst: %void
  call  vm.builtin.null_value in:              dst: %991
  call  vm.builtin.null_value in:              dst: %995
  call  vm.builtin.alloc_tensor in: %344, i0, c[43], c[495] dst: %999
  call  matmul1          in: %997, %998, %999 dst: %void
  call  vm.builtin.null_value in:              dst: %997
  call  vm.builtin.null_value in:              dst: %998
  call  vm.builtin.reshape in: %137, c[45]  dst: %1000
  call  vm.builtin.alloc_tensor in: %351, i0, c[48], c[496] dst: %1001
  call  transpose5       in: %1000, %1001 dst: %void
  call  vm.builtin.null_value in:              dst: %1000
  call  vm.builtin.reshape in: %1001, c[50] dst: %1002
  call  vm.builtin.alloc_tensor in: %365, i0, c[52], c[497] dst: %1003
  call  transpose6       in: %1002, %1003 dst: %void
  call  vm.builtin.null_value in:              dst: %1001
  call  vm.builtin.null_value in:              dst: %1002
  call  vm.builtin.reshape in: c[54], c[55] dst: %1004
  call  vm.builtin.reshape in: %1004, c[55] dst: %1005
  call  vm.builtin.null_value in:              dst: %1004
  call  vm.builtin.reshape in: c[54], c[56] dst: %1006
  call  vm.builtin.reshape in: %1006, c[56] dst: %1007
  call  vm.builtin.null_value in:              dst: %1006
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[498] dst: %1008
  call  subtract         in: %1005, %1007, %1008 dst: %void
  call  vm.builtin.null_value in:              dst: %1005
  call  vm.builtin.null_value in:              dst: %1007
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[499] dst: %1009
  call  add3             in: %1008, %1009 dst: %void
  call  vm.builtin.null_value in:              dst: %1008
  call  vm.builtin.alloc_tensor in: %348, i0, c[63], c[500] dst: %1010
  call  take             in: %1003, %1009, %1010 dst: %void
  call  vm.builtin.null_value in:              dst: %1003
  call  vm.builtin.null_value in:              dst: %1009
  call  vm.builtin.reshape in: %138, c[45]  dst: %1011
  call  vm.builtin.alloc_tensor in: %351, i0, c[48], c[501] dst: %1012
  call  transpose5       in: %1011, %1012 dst: %void
  call  vm.builtin.null_value in:              dst: %1011
  call  vm.builtin.reshape in: %1012, c[50] dst: %1013
  call  vm.builtin.alloc_tensor in: %365, i0, c[52], c[502] dst: %1014
  call  transpose6       in: %1013, %1014 dst: %void
  call  vm.builtin.null_value in:              dst: %1012
  call  vm.builtin.null_value in:              dst: %1013
  call  vm.builtin.reshape in: c[54], c[55] dst: %1015
  call  vm.builtin.reshape in: %1015, c[55] dst: %1016
  call  vm.builtin.null_value in:              dst: %1015
  call  vm.builtin.reshape in: c[54], c[56] dst: %1017
  call  vm.builtin.reshape in: %1017, c[56] dst: %1018
  call  vm.builtin.null_value in:              dst: %1017
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[503] dst: %1019
  call  subtract         in: %1016, %1018, %1019 dst: %void
  call  vm.builtin.null_value in:              dst: %1016
  call  vm.builtin.null_value in:              dst: %1018
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[504] dst: %1020
  call  add3             in: %1019, %1020 dst: %void
  call  vm.builtin.null_value in:              dst: %1019
  call  vm.builtin.alloc_tensor in: %351, i0, c[63], c[505] dst: %1021
  call  take             in: %1014, %1020, %1021 dst: %void
  call  vm.builtin.null_value in:              dst: %1014
  call  vm.builtin.null_value in:              dst: %1020
  call  vm.builtin.reshape in: %994, c[72]  dst: %1022
  call  vm.builtin.alloc_tensor in: %337, i0, c[73], c[506] dst: %1023
  call  einsum           in: %1022, %1010, %1023 dst: %void
  call  vm.builtin.null_value in:              dst: %1010
  call  vm.builtin.alloc_tensor in: %323, i0, c[73], c[507] dst: %1024
  call  einsum1          in: %1022, %1021, %1024 dst: %void
  call  vm.builtin.null_value in:              dst: %990
  call  vm.builtin.null_value in:              dst: %994
  call  vm.builtin.null_value in:              dst: %1022
  call  vm.builtin.null_value in:              dst: %1021
  call  vm.builtin.reshape in: %999, c[76]  dst: %1025
  call  vm.builtin.reshape in: %1023, c[77] dst: %1026
  call  vm.builtin.reshape in: %1024, c[78] dst: %1027
  call  vm.builtin.alloc_tensor in: %329, i0, c[76], c[508] dst: %1028
  call  add4             in: %1025, %1026, %1028 dst: %void
  call  vm.builtin.null_value in:              dst: %999
  call  vm.builtin.null_value in:              dst: %1025
  call  vm.builtin.null_value in:              dst: %1023
  call  vm.builtin.null_value in:              dst: %1026
  call  vm.builtin.alloc_tensor in: %344, i0, c[76], c[509] dst: %1029
  call  add5             in: %1028, %1027, %1029 dst: %void
  call  vm.builtin.null_value in:              dst: %1028
  call  vm.builtin.null_value in:              dst: %1024
  call  vm.builtin.null_value in:              dst: %1027
  call  vm.builtin.reshape in: %1029, c[43] dst: %1030
  call  vm.builtin.alloc_tensor in: %337, i0, c[43], c[510] dst: %1031
  call  softmax          in: %1030, %1031 dst: %void
  call  vm.builtin.null_value in:              dst: %1029
  call  vm.builtin.null_value in:              dst: %1030
  call  vm.builtin.alloc_tensor in: %329, i0, c[38], c[511] dst: %1032
  call  matmul2          in: %1031, %996, %1032 dst: %void
  call  vm.builtin.null_value in:              dst: %1031
  call  vm.builtin.null_value in:              dst: %992
  call  vm.builtin.null_value in:              dst: %996
  call  vm.builtin.reshape in: %1032, c[83] dst: %1033
  call  vm.builtin.alloc_tensor in: %344, i0, c[84], c[512] dst: %1034
  call  transpose7       in: %1033, %1034 dst: %void
  call  vm.builtin.null_value in:              dst: %1032
  call  vm.builtin.null_value in:              dst: %1033
  call  vm.builtin.reshape in: %1034, c[22] dst: %1035
  call  vm.builtin.alloc_tensor in: %509, i0, c[86], c[513] dst: %1036
  call  transpose8       in: %135, %1036  dst: %void
  call  vm.builtin.alloc_tensor in: %337, i0, c[22], c[514] dst: %1037
  call  matmul3          in: %1035, %1036, %1037 dst: %void
  call  vm.builtin.null_value in:              dst: %1034
  call  vm.builtin.null_value in:              dst: %1035
  call  vm.builtin.null_value in:              dst: %1036
  call  vm.builtin.alloc_tensor in: %318, i0, c[22], c[515] dst: %1038
  call  add6             in: %1037, %136, %1038 dst: %void
  call  vm.builtin.null_value in:              dst: %1037
  call  vm.builtin.reshape in: %1038, c[20] dst: %1039
  call  vm.builtin.alloc_tensor in: %329, i0, c[19], c[516] dst: %1040
  call  transpose9       in: %1039, %1040 dst: %void
  call  vm.builtin.null_value in:              dst: %1038
  call  vm.builtin.null_value in:              dst: %1039
  call  vm.builtin.reshape in: %1040, c[17] dst: %1041
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[517] dst: %1042
  call  strided_slice    in: %1041, %1042 dst: %void
  call  vm.builtin.null_value in:              dst: %1040
  call  vm.builtin.null_value in:              dst: %1041
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[518] dst: %1043
  call  add1             in: %978, %1042, %1043 dst: %void
  call  vm.builtin.null_value in:              dst: %978
  call  vm.builtin.null_value in:              dst: %1042
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[519] dst: %1044
  call  layer_norm       in: %1043, %139, %140, %1044 dst: %void
  call  vm.builtin.alloc_tensor in: %329, i0, c[94], c[520] dst: %1045
  call  transpose10      in: %141, %1045  dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[521] dst: %1046
  call  matmul4          in: %1044, %1045, %1046 dst: %void
  call  vm.builtin.null_value in:              dst: %1044
  call  vm.builtin.null_value in:              dst: %1045
  call  vm.builtin.alloc_tensor in: %315, i0, c[96], c[522] dst: %1047
  call  add7             in: %1046, %142, %1047 dst: %void
  call  vm.builtin.null_value in:              dst: %1046
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[523] dst: %1048
  call  gelu             in: %1047, %1048 dst: %void
  call  vm.builtin.null_value in:              dst: %1047
  call  vm.builtin.alloc_tensor in: %521, i0, c[100], c[524] dst: %1049
  call  transpose11      in: %143, %1049  dst: %void
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[525] dst: %1050
  call  matmul5          in: %1048, %1049, %1050 dst: %void
  call  vm.builtin.null_value in:              dst: %1048
  call  vm.builtin.null_value in:              dst: %1049
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[526] dst: %1051
  call  add8             in: %1050, %144, %1051 dst: %void
  call  vm.builtin.null_value in:              dst: %1050
  call  vm.builtin.alloc_tensor in: %329, i0, c[11], c[527] dst: %1052
  call  add1             in: %1043, %1051, %1052 dst: %void
  call  vm.builtin.null_value in:              dst: %1043
  call  vm.builtin.null_value in:              dst: %1051
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[528] dst: %1053
  call  layer_norm       in: %1052, %145, %146, %1053 dst: %void
  call  vm.builtin.alloc_tensor in: %344, i0, c[17], c[529] dst: %1054
  call  pad              in: %1053, %1054 dst: %void
  call  vm.builtin.null_value in:              dst: %1053
  call  vm.builtin.reshape in: %1054, c[19] dst: %1055
  call  vm.builtin.alloc_tensor in: %337, i0, c[20], c[530] dst: %1056
  call  transpose1       in: %1055, %1056 dst: %void
  call  vm.builtin.null_value in:              dst: %1054
  call  vm.builtin.null_value in:              dst: %1055
  call  vm.builtin.reshape in: %1056, c[22] dst: %1057
  call  vm.builtin.alloc_tensor in: %318, i0, c[23], c[531] dst: %1058
  call  transpose2       in: %147, %1058  dst: %void
  call  vm.builtin.alloc_tensor in: %521, i0, c[26], c[532] dst: %1059
  call  matmul           in: %1057, %1058, %1059 dst: %void
  call  vm.builtin.null_value in:              dst: %1056
  call  vm.builtin.null_value in:              dst: %1057
  call  vm.builtin.null_value in:              dst: %1058
  call  vm.builtin.alloc_tensor in: %344, i0, c[26], c[533] dst: %1060
  call  add2             in: %1059, %148, %1060 dst: %void
  call  vm.builtin.null_value in:              dst: %1059
  call  vm.builtin.reshape in: %1060, c[29] dst: %1061
  call  vm.builtin.alloc_tensor in: %337, i0, c[30], c[534] dst: %1062
  call  transpose3       in: %1061, %1062 dst: %void
  call  vm.builtin.null_value in:              dst: %1060
  call  vm.builtin.null_value in:              dst: %1061
  call  vm.builtin.reshape in: %1062, c[32] dst: %1063
  call  vm.builtin.alloc_tensor in: %318, i0, c[33], c[535] dst: %1064
  call  vm.builtin.alloc_tensor in: %521, i0, c[33], c[536] dst: %1065
  call  vm.builtin.alloc_tensor in: %344, i0, c[33], c[537] dst: %1066
  call  split            in: %1063, %1064, %1065, %1066 dst: %void
  call  vm.builtin.null_value in:              dst: %1062
  call  vm.builtin.null_value in:              dst: %1063
  call  vm.builtin.make_tuple in: %1064, %1065, %1066 dst: %1067
  call  vm.builtin.reshape in: %1064, c[38] dst: %1068
  call  vm.builtin.reshape in: %1065, c[38] dst: %1069
  call  vm.builtin.reshape in: %1066, c[38] dst: %1070
  call  vm.builtin.alloc_tensor in: %337, i0, c[38], c[538] dst: %1071
  call  multiply         in: %1068, %1071 dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[41], c[539] dst: %1072
  call  transpose4       in: %1069, %1072 dst: %void
  call  vm.builtin.null_value in:              dst: %1065
  call  vm.builtin.null_value in:              dst: %1069
  call  vm.builtin.alloc_tensor in: %521, i0, c[43], c[540] dst: %1073
  call  matmul1          in: %1071, %1072, %1073 dst: %void
  call  vm.builtin.null_value in:              dst: %1071
  call  vm.builtin.null_value in:              dst: %1072
  call  vm.builtin.reshape in: %151, c[45]  dst: %1074
  call  vm.builtin.alloc_tensor in: %365, i0, c[48], c[541] dst: %1075
  call  transpose5       in: %1074, %1075 dst: %void
  call  vm.builtin.null_value in:              dst: %1074
  call  vm.builtin.reshape in: %1075, c[50] dst: %1076
  call  vm.builtin.alloc_tensor in: %348, i0, c[52], c[542] dst: %1077
  call  transpose6       in: %1076, %1077 dst: %void
  call  vm.builtin.null_value in:              dst: %1075
  call  vm.builtin.null_value in:              dst: %1076
  call  vm.builtin.reshape in: c[54], c[55] dst: %1078
  call  vm.builtin.reshape in: %1078, c[55] dst: %1079
  call  vm.builtin.null_value in:              dst: %1078
  call  vm.builtin.reshape in: c[54], c[56] dst: %1080
  call  vm.builtin.reshape in: %1080, c[56] dst: %1081
  call  vm.builtin.null_value in:              dst: %1080
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[543] dst: %1082
  call  subtract         in: %1079, %1081, %1082 dst: %void
  call  vm.builtin.null_value in:              dst: %1079
  call  vm.builtin.null_value in:              dst: %1081
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[544] dst: %1083
  call  add3             in: %1082, %1083 dst: %void
  call  vm.builtin.null_value in:              dst: %1082
  call  vm.builtin.alloc_tensor in: %351, i0, c[63], c[545] dst: %1084
  call  take             in: %1077, %1083, %1084 dst: %void
  call  vm.builtin.null_value in:              dst: %1077
  call  vm.builtin.null_value in:              dst: %1083
  call  vm.builtin.reshape in: %152, c[45]  dst: %1085
  call  vm.builtin.alloc_tensor in: %365, i0, c[48], c[546] dst: %1086
  call  transpose5       in: %1085, %1086 dst: %void
  call  vm.builtin.null_value in:              dst: %1085
  call  vm.builtin.reshape in: %1086, c[50] dst: %1087
  call  vm.builtin.alloc_tensor in: %348, i0, c[52], c[547] dst: %1088
  call  transpose6       in: %1087, %1088 dst: %void
  call  vm.builtin.null_value in:              dst: %1086
  call  vm.builtin.null_value in:              dst: %1087
  call  vm.builtin.reshape in: c[54], c[55] dst: %1089
  call  vm.builtin.reshape in: %1089, c[55] dst: %1090
  call  vm.builtin.null_value in:              dst: %1089
  call  vm.builtin.reshape in: c[54], c[56] dst: %1091
  call  vm.builtin.reshape in: %1091, c[56] dst: %1092
  call  vm.builtin.null_value in:              dst: %1091
  call  vm.builtin.alloc_tensor in: %357, i0, c[59], c[548] dst: %1093
  call  subtract         in: %1090, %1092, %1093 dst: %void
  call  vm.builtin.null_value in:              dst: %1090
  call  vm.builtin.null_value in:              dst: %1092
  call  vm.builtin.alloc_tensor in: %359, i0, c[59], c[549] dst: %1094
  call  add3             in: %1093, %1094 dst: %void
  call  vm.builtin.null_value in:              dst: %1093
  call  vm.builtin.alloc_tensor in: %365, i0, c[63], c[550] dst: %1095
  call  take             in: %1088, %1094, %1095 dst: %void
  call  vm.builtin.null_value in:              dst: %1088
  call  vm.builtin.null_value in:              dst: %1094
  call  vm.builtin.reshape in: %1068, c[72] dst: %1096
  call  vm.builtin.alloc_tensor in: %337, i0, c[73], c[551] dst: %1097
  call  einsum           in: %1096, %1084, %1097 dst: %void
  call  vm.builtin.null_value in:              dst: %1084
  call  vm.builtin.alloc_tensor in: %323, i0, c[73], c[552] dst: %1098
  call  einsum1          in: %1096, %1095, %1098 dst: %void
  call  vm.builtin.null_value in:              dst: %1064
  call  vm.builtin.null_value in:              dst: %1068
  call  vm.builtin.null_value in:              dst: %1096
  call  vm.builtin.null_value in:              dst: %1095
  call  vm.builtin.reshape in: %1073, c[76] dst: %1099
  call  vm.builtin.reshape in: %1097, c[77] dst: %1100
  call  vm.builtin.reshape in: %1098, c[78] dst: %1101
  call  vm.builtin.alloc_tensor in: %318, i0, c[76], c[553] dst: %1102
  call  add4             in: %1099, %1100, %1102 dst: %void
  call  vm.builtin.null_value in:              dst: %1073
  call  vm.builtin.null_value in:              dst: %1099
  call  vm.builtin.null_value in:              dst: %1097
  call  vm.builtin.null_value in:              dst: %1100
  call  vm.builtin.alloc_tensor in: %521, i0, c[76], c[554] dst: %1103
  call  add5             in: %1102, %1101, %1103 dst: %void
  call  vm.builtin.null_value in:              dst: %1102
  call  vm.builtin.null_value in:              dst: %1098
  call  vm.builtin.null_value in:              dst: %1101
  call  vm.builtin.reshape in: %1103, c[43] dst: %1104
  call  vm.builtin.alloc_tensor in: %337, i0, c[43], c[555] dst: %1105
  call  softmax          in: %1104, %1105 dst: %void
  call  vm.builtin.null_value in:              dst: %1103
  call  vm.builtin.null_value in:              dst: %1104
  call  vm.builtin.alloc_tensor in: %318, i0, c[38], c[556] dst: %1106
  call  matmul2          in: %1105, %1070, %1106 dst: %void
  call  vm.builtin.null_value in:              dst: %1105
  call  vm.builtin.null_value in:              dst: %1066
  call  vm.builtin.null_value in:              dst: %1070
  call  vm.builtin.reshape in: %1106, c[83] dst: %1107
  call  vm.builtin.alloc_tensor in: %521, i0, c[84], c[557] dst: %1108
  call  transpose7       in: %1107, %1108 dst: %void
  call  vm.builtin.null_value in:              dst: %1106
  call  vm.builtin.null_value in:              dst: %1107
  call  vm.builtin.reshape in: %1108, c[22] dst: %1109
  call  vm.builtin.alloc_tensor in: %509, i0, c[86], c[558] dst: %1110
  call  transpose8       in: %149, %1110  dst: %void
  call  vm.builtin.alloc_tensor in: %337, i0, c[22], c[559] dst: %1111
  call  matmul3          in: %1109, %1110, %1111 dst: %void
  call  vm.builtin.null_value in:              dst: %1108
  call  vm.builtin.null_value in:              dst: %1109
  call  vm.builtin.null_value in:              dst: %1110
  call  vm.builtin.alloc_tensor in: %344, i0, c[22], c[560] dst: %1112
  call  add6             in: %1111, %150, %1112 dst: %void
  call  vm.builtin.null_value in:              dst: %1111
  call  vm.builtin.reshape in: %1112, c[20] dst: %1113
  call  vm.builtin.alloc_tensor in: %318, i0, c[19], c[561] dst: %1114
  call  transpose9       in: %1113, %1114 dst: %void
  call  vm.builtin.null_value in:              dst: %1112
  call  vm.builtin.null_value in:              dst: %1113
  call  vm.builtin.reshape in: %1114, c[17] dst: %1115
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[562] dst: %1116
  call  strided_slice    in: %1115, %1116 dst: %void
  call  vm.builtin.null_value in:              dst: %1114
  call  vm.builtin.null_value in:              dst: %1115
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[563] dst: %1117
  call  add1             in: %1052, %1116, %1117 dst: %void
  call  vm.builtin.null_value in:              dst: %1052
  call  vm.builtin.null_value in:              dst: %1116
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[564] dst: %1118
  call  layer_norm       in: %1117, %153, %154, %1118 dst: %void
  call  vm.builtin.alloc_tensor in: %318, i0, c[94], c[565] dst: %1119
  call  transpose10      in: %155, %1119  dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[566] dst: %1120
  call  matmul4          in: %1118, %1119, %1120 dst: %void
  call  vm.builtin.null_value in:              dst: %1118
  call  vm.builtin.null_value in:              dst: %1119
  call  vm.builtin.alloc_tensor in: %495, i0, c[96], c[567] dst: %1121
  call  add7             in: %1120, %156, %1121 dst: %void
  call  vm.builtin.null_value in:              dst: %1120
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[568] dst: %1122
  call  gelu             in: %1121, %1122 dst: %void
  call  vm.builtin.null_value in:              dst: %1121
  call  vm.builtin.alloc_tensor in: %329, i0, c[100], c[569] dst: %1123
  call  transpose11      in: %157, %1123  dst: %void
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[570] dst: %1124
  call  matmul5          in: %1122, %1123, %1124 dst: %void
  call  vm.builtin.null_value in:              dst: %1122
  call  vm.builtin.null_value in:              dst: %1123
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[571] dst: %1125
  call  add8             in: %1124, %158, %1125 dst: %void
  call  vm.builtin.null_value in:              dst: %1124
  call  vm.builtin.alloc_tensor in: %318, i0, c[11], c[572] dst: %1126
  call  add1             in: %1117, %1125, %1126 dst: %void
  call  vm.builtin.null_value in:              dst: %1117
  call  vm.builtin.null_value in:              dst: %1125
  call  vm.builtin.alloc_tensor in: %329, i0, c[11], c[573] dst: %1127
  call  layer_norm       in: %1126, %159, %160, %1127 dst: %void
  call  vm.builtin.alloc_tensor in: %521, i0, c[23], c[574] dst: %1128
  call  transpose2       in: %161, %1128  dst: %void
  call  vm.builtin.alloc_tensor in: %337, i0, c[152], c[575] dst: %1129
  call  matmul6          in: %1127, %1128, %1129 dst: %void
  call  vm.builtin.null_value in:              dst: %1127
  call  vm.builtin.null_value in:              dst: %1128
  call  vm.builtin.alloc_tensor in: %344, i0, c[152], c[576] dst: %1130
  call  add9             in: %1129, %162, %1130 dst: %void
  call  vm.builtin.null_value in:              dst: %1129
  call  vm.builtin.reshape in: %1130, c[155] dst: %1131
  call  vm.builtin.alloc_tensor in: %329, i0, c[156], c[577] dst: %1132
  call  transpose12      in: %1131, %1132 dst: %void
  call  vm.builtin.null_value in:              dst: %1130
  call  vm.builtin.null_value in:              dst: %1131
  call  vm.builtin.reshape in: %1132, c[158] dst: %1133
  call  vm.builtin.alloc_tensor in: %521, i0, c[159], c[578] dst: %1134
  call  vm.builtin.alloc_tensor in: %337, i0, c[159], c[579] dst: %1135
  call  vm.builtin.alloc_tensor in: %344, i0, c[159], c[580] dst: %1136
  call  split1           in: %1133, %1134, %1135, %1136 dst: %void
  call  vm.builtin.null_value in:              dst: %1132
  call  vm.builtin.null_value in:              dst: %1133
  call  vm.builtin.make_tuple in: %1134, %1135, %1136 dst: %1137
  call  vm.builtin.reshape in: %1134, c[163] dst: %1138
  call  vm.builtin.reshape in: %1135, c[163] dst: %1139
  call  vm.builtin.reshape in: %1136, c[163] dst: %1140
  call  vm.builtin.alloc_tensor in: %329, i0, c[163], c[581] dst: %1141
  call  multiply3        in: %1138, %1141 dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[165], c[582] dst: %1142
  call  transpose13      in: %1139, %1142 dst: %void
  call  vm.builtin.null_value in:              dst: %1135
  call  vm.builtin.null_value in:              dst: %1139
  call  vm.builtin.alloc_tensor in: %315, i0, c[168], c[583] dst: %1143
  call  matmul7          in: %1141, %1142, %1143 dst: %void
  call  vm.builtin.null_value in:              dst: %1141
  call  vm.builtin.null_value in:              dst: %1142
  call  vm.builtin.reshape in: %165, c[170] dst: %1144
  call  vm.builtin.alloc_tensor in: %348, i0, c[171], c[584] dst: %1145
  call  transpose14      in: %1144, %1145 dst: %void
  call  vm.builtin.null_value in:              dst: %1144
  call  vm.builtin.reshape in: %1145, c[173] dst: %1146
  call  vm.builtin.alloc_tensor in: %351, i0, c[174], c[585] dst: %1147
  call  transpose15      in: %1146, %1147 dst: %void
  call  vm.builtin.null_value in:              dst: %1145
  call  vm.builtin.null_value in:              dst: %1146
  call  vm.builtin.reshape in: c[176], c[177] dst: %1148
  call  vm.builtin.reshape in: %1148, c[177] dst: %1149
  call  vm.builtin.null_value in:              dst: %1148
  call  vm.builtin.reshape in: c[176], c[178] dst: %1150
  call  vm.builtin.reshape in: %1150, c[178] dst: %1151
  call  vm.builtin.null_value in:              dst: %1150
  call  vm.builtin.alloc_tensor in: %505, i0, c[181], c[586] dst: %1152
  call  subtract1        in: %1149, %1151, %1152 dst: %void
  call  vm.builtin.null_value in:              dst: %1149
  call  vm.builtin.null_value in:              dst: %1151
  call  vm.builtin.alloc_tensor in: %507, i0, c[181], c[587] dst: %1153
  call  add10            in: %1152, %1153 dst: %void
  call  vm.builtin.null_value in:              dst: %1152
  call  vm.builtin.alloc_tensor in: %736, i0, c[186], c[588] dst: %1154
  call  take1            in: %1147, %1153, %1154 dst: %void
  call  vm.builtin.null_value in:              dst: %1147
  call  vm.builtin.null_value in:              dst: %1153
  call  vm.builtin.reshape in: %166, c[170] dst: %1155
  call  vm.builtin.alloc_tensor in: %365, i0, c[171], c[589] dst: %1156
  call  transpose14      in: %1155, %1156 dst: %void
  call  vm.builtin.null_value in:              dst: %1155
  call  vm.builtin.reshape in: %1156, c[173] dst: %1157
  call  vm.builtin.alloc_tensor in: %348, i0, c[174], c[590] dst: %1158
  call  transpose15      in: %1157, %1158 dst: %void
  call  vm.builtin.null_value in:              dst: %1156
  call  vm.builtin.null_value in:              dst: %1157
  call  vm.builtin.reshape in: c[176], c[177] dst: %1159
  call  vm.builtin.reshape in: %1159, c[177] dst: %1160
  call  vm.builtin.null_value in:              dst: %1159
  call  vm.builtin.reshape in: c[176], c[178] dst: %1161
  call  vm.builtin.reshape in: %1161, c[178] dst: %1162
  call  vm.builtin.null_value in:              dst: %1161
  call  vm.builtin.alloc_tensor in: %505, i0, c[181], c[591] dst: %1163
  call  subtract1        in: %1160, %1162, %1163 dst: %void
  call  vm.builtin.null_value in:              dst: %1160
  call  vm.builtin.null_value in:              dst: %1162
  call  vm.builtin.alloc_tensor in: %507, i0, c[181], c[592] dst: %1164
  call  add10            in: %1163, %1164 dst: %void
  call  vm.builtin.null_value in:              dst: %1163
  call  vm.builtin.alloc_tensor in: %509, i0, c[186], c[593] dst: %1165
  call  take1            in: %1158, %1164, %1165 dst: %void
  call  vm.builtin.null_value in:              dst: %1158
  call  vm.builtin.null_value in:              dst: %1164
  call  vm.builtin.reshape in: %1138, c[194] dst: %1166
  call  vm.builtin.alloc_tensor in: %337, i0, c[194], c[594] dst: %1167
  call  einsum2          in: %1166, %1154, %1167 dst: %void
  call  vm.builtin.null_value in:              dst: %1154
  call  vm.builtin.alloc_tensor in: %329, i0, c[194], c[595] dst: %1168
  call  einsum3          in: %1166, %1165, %1168 dst: %void
  call  vm.builtin.null_value in:              dst: %1134
  call  vm.builtin.null_value in:              dst: %1138
  call  vm.builtin.null_value in:              dst: %1166
  call  vm.builtin.null_value in:              dst: %1165
  call  vm.builtin.reshape in: %1143, c[197] dst: %1169
  call  vm.builtin.reshape in: %1167, c[198] dst: %1170
  call  vm.builtin.reshape in: %1168, c[199] dst: %1171
  call  vm.builtin.alloc_tensor in: %495, i0, c[197], c[596] dst: %1172
  call  add11            in: %1169, %1170, %1172 dst: %void
  call  vm.builtin.null_value in:              dst: %1143
  call  vm.builtin.null_value in:              dst: %1169
  call  vm.builtin.null_value in:              dst: %1167
  call  vm.builtin.null_value in:              dst: %1170
  call  vm.builtin.alloc_tensor in: %315, i0, c[197], c[597] dst: %1173
  call  add12            in: %1172, %1171, %1173 dst: %void
  call  vm.builtin.null_value in:              dst: %1172
  call  vm.builtin.null_value in:              dst: %1168
  call  vm.builtin.null_value in:              dst: %1171
  call  vm.builtin.reshape in: %1173, c[168] dst: %1174
  call  vm.builtin.alloc_tensor in: %495, i0, c[168], c[598] dst: %1175
  call  softmax1         in: %1174, %1175 dst: %void
  call  vm.builtin.null_value in:              dst: %1173
  call  vm.builtin.null_value in:              dst: %1174
  call  vm.builtin.alloc_tensor in: %521, i0, c[163], c[599] dst: %1176
  call  matmul8          in: %1175, %1140, %1176 dst: %void
  call  vm.builtin.null_value in:              dst: %1175
  call  vm.builtin.null_value in:              dst: %1136
  call  vm.builtin.null_value in:              dst: %1140
  call  vm.builtin.reshape in: %1176, c[204] dst: %1177
  call  vm.builtin.alloc_tensor in: %337, i0, c[205], c[600] dst: %1178
  call  transpose16      in: %1177, %1178 dst: %void
  call  vm.builtin.null_value in:              dst: %1176
  call  vm.builtin.null_value in:              dst: %1177
  call  vm.builtin.reshape in: %1178, c[11] dst: %1179
  call  vm.builtin.alloc_tensor in: %509, i0, c[86], c[601] dst: %1180
  call  transpose8       in: %163, %1180  dst: %void
  call  vm.builtin.alloc_tensor in: %329, i0, c[11], c[602] dst: %1181
  call  matmul9          in: %1179, %1180, %1181 dst: %void
  call  vm.builtin.null_value in:              dst: %1178
  call  vm.builtin.null_value in:              dst: %1179
  call  vm.builtin.null_value in:              dst: %1180
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[603] dst: %1182
  call  add8             in: %1181, %164, %1182 dst: %void
  call  vm.builtin.null_value in:              dst: %1181
  call  vm.builtin.alloc_tensor in: %521, i0, c[11], c[604] dst: %1183
  call  add1             in: %1126, %1182, %1183 dst: %void
  call  vm.builtin.null_value in:              dst: %1126
  call  vm.builtin.null_value in:              dst: %1182
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[605] dst: %1184
  call  layer_norm       in: %1183, %167, %168, %1184 dst: %void
  call  vm.builtin.alloc_tensor in: %329, i0, c[94], c[606] dst: %1185
  call  transpose10      in: %169, %1185  dst: %void
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[607] dst: %1186
  call  matmul4          in: %1184, %1185, %1186 dst: %void
  call  vm.builtin.null_value in:              dst: %1184
  call  vm.builtin.null_value in:              dst: %1185
  call  vm.builtin.alloc_tensor in: %315, i0, c[96], c[608] dst: %1187
  call  add7             in: %1186, %170, %1187 dst: %void
  call  vm.builtin.null_value in:              dst: %1186
  call  vm.builtin.alloc_tensor in: %323, i0, c[96], c[609] dst: %1188
  call  gelu             in: %1187, %1188 dst: %void
  call  vm.builtin.null_value in:              dst: %1187
  call  vm.builtin.alloc_tensor in: %318, i0, c[100], c[610] dst: %1189
  call  transpose11      in: %171, %1189  dst: %void
  call  vm.builtin.alloc_tensor in: %344, i0, c[11], c[611] dst: %1190
  call  matmul5          in: %1188, %1189, %1190 dst: %void
  call  vm.builtin.null_value in:              dst: %1188
  call  vm.builtin.null_value in:              dst: %1189
  call  vm.builtin.alloc_tensor in: %337, i0, c[11], c[612] dst: %1191
  call  add8             in: %1190, %172, %1191 dst: %void
  call  vm.builtin.null_value in:              dst: %1190
  call  vm.builtin.alloc_tensor in: %329, i0, c[11], c[613] dst: %1192
  call  add1             in: %1183, %1191, %1192 dst: %void
  call  vm.builtin.null_value in:              dst: %1183
  call  vm.builtin.null_value in:              dst: %1191
  call  vm.builtin.alloc_tensor in: %318, i0, c[5], c[614] dst: %1193
  call  transpose17      in: %1192, %1193 dst: %void
  call  vm.builtin.null_value in:              dst: %1192
  call  vm.builtin.alloc_tensor in: %344, i0, c[615], c[616] dst: %1194
  call  conv2d1          in: %1193, %173, %1194 dst: %void
  call  vm.builtin.null_value in:              dst: %1193
  call  vm.builtin.alloc_tensor in: %351, i0, c[617], c[618] dst: %1195
  call  mean             in: %1194, %1195 dst: %void
  call  vm.builtin.alloc_tensor in: %521, i0, c[615], c[619] dst: %1196
  call  subtract2        in: %1194, %1195, %1196 dst: %void
  call  vm.builtin.null_value in:              dst: %1194
  call  vm.builtin.null_value in:              dst: %1195
  call  vm.builtin.alloc_tensor in: %337, i0, c[615], c[620] dst: %1197
  call  power            in: %1196, %1197 dst: %void
  call  vm.builtin.alloc_tensor in: %365, i0, c[617], c[621] dst: %1198
  call  mean             in: %1197, %1198 dst: %void
  call  vm.builtin.null_value in:              dst: %1197
  call  vm.builtin.alloc_tensor in: %348, i0, c[617], c[622] dst: %1199
  call  add13            in: %1198, %1199 dst: %void
  call  vm.builtin.null_value in:              dst: %1198
  call  vm.builtin.alloc_tensor in: %351, i0, c[617], c[623] dst: %1200
  call  tir_sqrt         in: %1199, %1200 dst: %void
  call  vm.builtin.null_value in:              dst: %1199
  call  vm.builtin.alloc_tensor in: %329, i0, c[615], c[624] dst: %1201
  call  divide           in: %1196, %1200, %1201 dst: %void
  call  vm.builtin.null_value in:              dst: %1196
  call  vm.builtin.null_value in:              dst: %1200
  call  vm.builtin.reshape in: %174, c[625] dst: %1202
  call  vm.builtin.reshape in: %1202, c[626] dst: %1203
  call  vm.builtin.null_value in:              dst: %1202
  call  vm.builtin.reshape in: %175, c[625] dst: %1204
  call  vm.builtin.reshape in: %1204, c[626] dst: %1205
  call  vm.builtin.null_value in:              dst: %1204
  call  vm.builtin.alloc_tensor in: %318, i0, c[615], c[627] dst: %1206
  call  multiply6        in: %1203, %1201, %1206 dst: %void
  call  vm.builtin.null_value in:              dst: %1203
  call  vm.builtin.null_value in:              dst: %1201
  call  vm.builtin.alloc_tensor in: %344, i0, c[615], c[628] dst: %1207
  call  add14            in: %1206, %1205, %1207 dst: %void
  call  vm.builtin.null_value in:              dst: %1205
  call  vm.builtin.null_value in:              dst: %1206
  call  vm.builtin.alloc_tensor in: %337, i0, c[615], c[629] dst: %1208
  call  conv2d2          in: %1207, %176, %1208 dst: %void
  call  vm.builtin.null_value in:              dst: %1207
  call  vm.builtin.alloc_tensor in: %365, i0, c[617], c[630] dst: %1209
  call  mean             in: %1208, %1209 dst: %void
  call  vm.builtin.alloc_tensor in: %521, i0, c[615], c[631] dst: %1210
  call  subtract2        in: %1208, %1209, %1210 dst: %void
  call  vm.builtin.null_value in:              dst: %1208
  call  vm.builtin.null_value in:              dst: %1209
  call  vm.builtin.alloc_tensor in: %329, i0, c[615], c[632] dst: %1211
  call  power            in: %1210, %1211 dst: %void
  call  vm.builtin.alloc_tensor in: %348, i0, c[617], c[633] dst: %1212
  call  mean             in: %1211, %1212 dst: %void
  call  vm.builtin.null_value in:              dst: %1211
  call  vm.builtin.alloc_tensor in: %351, i0, c[617], c[634] dst: %1213
  call  add13            in: %1212, %1213 dst: %void
  call  vm.builtin.null_value in:              dst: %1212
  call  vm.builtin.alloc_tensor in: %365, i0, c[617], c[635] dst: %1214
  call  tir_sqrt         in: %1213, %1214 dst: %void
  call  vm.builtin.null_value in:              dst: %1213
  call  vm.builtin.alloc_tensor in: %318, i0, c[615], c[636] dst: %1215
  call  divide           in: %1210, %1214, %1215 dst: %void
  call  vm.builtin.null_value in:              dst: %1210
  call  vm.builtin.null_value in:              dst: %1214
  call  vm.builtin.reshape in: %177, c[625] dst: %1216
  call  vm.builtin.reshape in: %1216, c[626] dst: %1217
  call  vm.builtin.null_value in:              dst: %1216
  call  vm.builtin.reshape in: %178, c[625] dst: %1218
  call  vm.builtin.reshape in: %1218, c[626] dst: %1219
  call  vm.builtin.null_value in:              dst: %1218
  call  vm.builtin.alloc_tensor in: %344, i0, c[615], c[637] dst: %1220
  call  multiply6        in: %1217, %1215, %1220 dst: %void
  call  vm.builtin.null_value in:              dst: %1217
  call  vm.builtin.null_value in:              dst: %1215
  call  vm.builtin.alloc_storage in: %vm, c[638], i0, c[639], c[4] dst: %1221
  call  vm.builtin.alloc_tensor in: %1221, i0, c[615], c[640] dst: %1222
  call  vm.builtin.null_value in:              dst: %1221
  call  add14            in: %1220, %1219, %1222 dst: %void
  call  vm.builtin.null_value in:              dst: %1219
  call  vm.builtin.null_value in:              dst: %1220
  call  vm.builtin.make_tuple in: %1           dst: %1223
  call  vm.builtin.make_tuple in: %1222, %1223 dst: %1224
  call  vm.builtin.null_value in:              dst: %1222
  call  vm.builtin.null_value in:              dst: %315
  call  vm.builtin.null_value in:              dst: %318
  call  vm.builtin.null_value in:              dst: %323
  call  vm.builtin.null_value in:              dst: %329
  call  vm.builtin.null_value in:              dst: %337
  call  vm.builtin.null_value in:              dst: %344
  call  vm.builtin.null_value in:              dst: %348
  call  vm.builtin.null_value in:              dst: %351
  call  vm.builtin.null_value in:              dst: %357
  call  vm.builtin.null_value in:              dst: %359
  call  vm.builtin.null_value in:              dst: %365
  call  vm.builtin.null_value in:              dst: %495
  call  vm.builtin.null_value in:              dst: %505
  call  vm.builtin.null_value in:              dst: %507
  call  vm.builtin.null_value in:              dst: %509
  call  vm.builtin.null_value in:              dst: %521
  call  vm.builtin.null_value in:              dst: %736
  ret   %1224

@vm.builtin.check_tensor_info packed_func;

@vm.builtin.match_shape packed_func;

@vm.builtin.alloc_storage packed_func;

@vm.builtin.alloc_tensor packed_func;

@conv2d packed_func;

@vm.builtin.reshape packed_func;

@add packed_func;

@vm.builtin.null_value packed_func;

@transpose packed_func;

@add1 packed_func;

@layer_norm packed_func;

@pad packed_func;

@transpose1 packed_func;

@transpose2 packed_func;

@matmul packed_func;

@add2 packed_func;

@transpose3 packed_func;

@split packed_func;

@vm.builtin.make_tuple packed_func;

@multiply packed_func;

@transpose4 packed_func;

@matmul1 packed_func;

@transpose5 packed_func;

@transpose6 packed_func;

@subtract packed_func;

@add3 packed_func;

@take packed_func;

@einsum packed_func;

@einsum1 packed_func;

@add4 packed_func;

@add5 packed_func;

@softmax packed_func;

@matmul2 packed_func;

@transpose7 packed_func;

@transpose8 packed_func;

@matmul3 packed_func;

@add6 packed_func;

@transpose9 packed_func;

@strided_slice packed_func;

@transpose10 packed_func;

@matmul4 packed_func;

@add7 packed_func;

@gelu packed_func;

@transpose11 packed_func;

@matmul5 packed_func;

@add8 packed_func;

@matmul6 packed_func;

@add9 packed_func;

@transpose12 packed_func;

@split1 packed_func;

@multiply3 packed_func;

@transpose13 packed_func;

@matmul7 packed_func;

@transpose14 packed_func;

@transpose15 packed_func;

@subtract1 packed_func;

@add10 packed_func;

@take1 packed_func;

@einsum2 packed_func;

@einsum3 packed_func;

@add11 packed_func;

@add12 packed_func;

@softmax1 packed_func;

@matmul8 packed_func;

@transpose16 packed_func;

@matmul9 packed_func;

@transpose17 packed_func;

@conv2d1 packed_func;

@mean packed_func;

@subtract2 packed_func;

@power packed_func;

@add13 packed_func;

@tir_sqrt packed_func;

@divide packed_func;

@multiply6 packed_func;

@add14 packed_func;

@conv2d2 packed_func;

@get_prompt_embeddings:
  call  vm.builtin.check_tensor_info in: %0, i4, c[641], c[642] dst: %void
  call  vm.builtin.match_shape in: %0, %void, i4, i0, i1, i0, i1, i0, i1, i0, i2, c[642] dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[643], i0, c[644], c[4] dst: %315
  call  vm.builtin.alloc_tensor in: %315, i0, c[645], c[646] dst: %316
  call  ones             in: %316         dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[647], i0, c[648], c[4] dst: %317
  call  vm.builtin.alloc_tensor in: %317, i0, c[649], c[650] dst: %318
  call  add15            in: %0, %318     dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[647], i0, c[651], c[4] dst: %319
  call  vm.builtin.alloc_tensor in: %319, i0, c[649], c[652] dst: %320
  call  zeros            in: %320         dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[653], i0, c[654], c[4] dst: %321
  call  vm.builtin.alloc_tensor in: %321, i0, c[645], c[655] dst: %322
  call  ones             in: %322         dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[653], i0, c[656], c[4] dst: %323
  call  vm.builtin.alloc_tensor in: %323, i0, c[645], c[657] dst: %324
  call  multiply7        in: %322, %324   dst: %void
  call  vm.builtin.null_value in:              dst: %322
  call  vm.builtin.alloc_storage in: %vm, c[658], i0, c[659], c[4] dst: %325
  call  vm.builtin.alloc_tensor in: %325, i0, c[660], c[661] dst: %326
  call  concatenate      in: %318, %320, %326 dst: %void
  call  vm.builtin.null_value in:              dst: %318
  call  vm.builtin.null_value in:              dst: %320
  call  vm.builtin.alloc_tensor in: %321, i0, c[662], c[663] dst: %327
  call  concatenate1     in: %316, %324, %327 dst: %void
  call  vm.builtin.null_value in:              dst: %316
  call  vm.builtin.null_value in:              dst: %324
  call  vm.builtin.alloc_tensor in: %317, i0, c[664], c[665] dst: %328
  call  strided_slice1   in: %326, %328   dst: %void
  call  vm.builtin.alloc_tensor in: %319, i0, c[664], c[666] dst: %329
  call  divide1          in: %328, %329   dst: %void
  call  vm.builtin.null_value in:              dst: %328
  call  vm.builtin.alloc_tensor in: %317, i0, c[664], c[667] dst: %330
  call  strided_slice2   in: %326, %330   dst: %void
  call  vm.builtin.null_value in:              dst: %326
  call  vm.builtin.alloc_tensor in: %325, i0, c[664], c[668] dst: %331
  call  divide1          in: %330, %331   dst: %void
  call  vm.builtin.null_value in:              dst: %330
  call  vm.builtin.alloc_tensor in: %317, i0, c[660], c[669] dst: %332
  call  concatenate2     in: %329, %331, %332 dst: %void
  call  vm.builtin.null_value in:              dst: %329
  call  vm.builtin.null_value in:              dst: %331
  call  vm.builtin.alloc_tensor in: %325, i0, c[660], c[670] dst: %333
  call  add16            in: %332, %332, %333 dst: %void
  call  vm.builtin.null_value in:              dst: %332
  call  vm.builtin.alloc_tensor in: %317, i0, c[660], c[671] dst: %334
  call  subtract3        in: %333, %334   dst: %void
  call  vm.builtin.null_value in:              dst: %333
  call  vm.builtin.alloc_storage in: %vm, c[672], i0, c[673], c[4] dst: %335
  call  vm.builtin.alloc_tensor in: %335, i0, c[674], c[675] dst: %336
  call  ones1            in: %336         dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[676], i0, c[677], c[4] dst: %337
  call  vm.builtin.alloc_tensor in: %337, i0, c[678], c[679] dst: %338
  call  matmul10         in: %334, %336, %338 dst: %void
  call  vm.builtin.null_value in:              dst: %334
  call  vm.builtin.null_value in:              dst: %336
  call  vm.builtin.alloc_tensor in: %335, i0, c[678], c[680] dst: %339
  call  multiply8        in: %338, %339   dst: %void
  call  vm.builtin.null_value in:              dst: %338
  call  vm.builtin.alloc_tensor in: %337, i0, c[678], c[681] dst: %340
  call  tir_sin          in: %339, %340   dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[672], i0, c[682], c[4] dst: %341
  call  vm.builtin.alloc_tensor in: %341, i0, c[678], c[683] dst: %342
  call  tir_cos          in: %339, %342   dst: %void
  call  vm.builtin.null_value in:              dst: %339
  call  vm.builtin.alloc_tensor in: %335, i0, c[684], c[685] dst: %343
  call  concatenate3     in: %340, %342, %343 dst: %void
  call  vm.builtin.null_value in:              dst: %340
  call  vm.builtin.null_value in:              dst: %342
  call  vm.builtin.null_value in:              dst: %343
  call  vm.builtin.reshape in: %327, c[664] dst: %344
  call  vm.builtin.alloc_storage in: %vm, c[686], i0, c[687], c[4] dst: %345
  call  vm.builtin.alloc_tensor in: %345, i0, c[664], c[688] dst: %346
  call  equal            in: %344, %346   dst: %void
  call  vm.builtin.alloc_tensor in: %335, i0, c[684], c[689] dst: %347
  call  where            in: %346, %194, %194, %347 dst: %void
  call  vm.builtin.null_value in:              dst: %346
  call  vm.builtin.alloc_tensor in: %345, i0, c[664], c[690] dst: %348
  call  not_equal        in: %344, %348   dst: %void
  call  vm.builtin.alloc_tensor in: %341, i0, c[684], c[691] dst: %349
  call  where1           in: %348, %347, %347, %349 dst: %void
  call  vm.builtin.null_value in:              dst: %348
  call  vm.builtin.null_value in:              dst: %347
  call  vm.builtin.alloc_tensor in: %345, i0, c[662], c[692] dst: %350
  call  equal1           in: %327, %350   dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[686], i0, c[693], c[4] dst: %351
  call  vm.builtin.alloc_tensor in: %351, i0, c[662], c[694] dst: %352
  call  equal2           in: %327, %352   dst: %void
  call  vm.builtin.null_value in:              dst: %327
  call  vm.builtin.null_value in:              dst: %344
  call  vm.builtin.reshape in: %350, c[664] dst: %353
  call  vm.builtin.reshape in: %190, c[695] dst: %354
  call  vm.builtin.reshape in: %354, c[696] dst: %355
  call  vm.builtin.null_value in:              dst: %354
  call  vm.builtin.alloc_tensor in: %335, i0, c[684], c[697] dst: %356
  call  add17            in: %349, %355, %356 dst: %void
  call  vm.builtin.null_value in:              dst: %355
  call  vm.builtin.null_value in:              dst: %349
  call  vm.builtin.alloc_tensor in: %341, i0, c[684], c[698] dst: %357
  call  where1           in: %353, %356, %356, %357 dst: %void
  call  vm.builtin.null_value in:              dst: %350
  call  vm.builtin.null_value in:              dst: %353
  call  vm.builtin.null_value in:              dst: %356
  call  vm.builtin.reshape in: %352, c[664] dst: %358
  call  vm.builtin.reshape in: %191, c[695] dst: %359
  call  vm.builtin.reshape in: %359, c[696] dst: %360
  call  vm.builtin.null_value in:              dst: %359
  call  vm.builtin.alloc_tensor in: %335, i0, c[684], c[699] dst: %361
  call  add17            in: %357, %360, %361 dst: %void
  call  vm.builtin.null_value in:              dst: %360
  call  vm.builtin.null_value in:              dst: %357
  call  vm.builtin.alloc_storage in: %vm, c[700], i0, c[701], c[4] dst: %362
  call  vm.builtin.alloc_tensor in: %362, i0, c[684], c[702] dst: %363
  call  vm.builtin.null_value in:              dst: %362
  call  where1           in: %358, %361, %361, %363 dst: %void
  call  vm.builtin.null_value in:              dst: %352
  call  vm.builtin.null_value in:              dst: %358
  call  vm.builtin.null_value in:              dst: %361
  call  vm.builtin.reshape in: %189, c[703] dst: %364
  call  vm.builtin.reshape in: %364, c[703] dst: %365
  call  vm.builtin.null_value in:              dst: %364
  call  vm.builtin.alloc_storage in: %vm, c[66], i0, c[704], c[4] dst: %366
  call  vm.builtin.alloc_tensor in: %366, i0, c[705], c[706] dst: %367
  call  repeat1          in: %365, %367   dst: %void
  call  vm.builtin.null_value in:              dst: %365
  call  vm.builtin.alloc_storage in: %vm, c[638], i0, c[707], c[4] dst: %368
  call  vm.builtin.alloc_tensor in: %368, i0, c[615], c[708] dst: %369
  call  vm.builtin.null_value in:              dst: %368
  call  repeat2          in: %367, %369   dst: %void
  call  vm.builtin.null_value in:              dst: %367
  call  vm.builtin.make_tuple in: %363, %369   dst: %370
  call  vm.builtin.make_tuple in: %1           dst: %371
  call  vm.builtin.make_tuple in: %370, %371   dst: %372
  call  vm.builtin.null_value in:              dst: %363
  call  vm.builtin.null_value in:              dst: %369
  call  vm.builtin.null_value in:              dst: %315
  call  vm.builtin.null_value in:              dst: %317
  call  vm.builtin.null_value in:              dst: %319
  call  vm.builtin.null_value in:              dst: %321
  call  vm.builtin.null_value in:              dst: %323
  call  vm.builtin.null_value in:              dst: %325
  call  vm.builtin.null_value in:              dst: %335
  call  vm.builtin.null_value in:              dst: %337
  call  vm.builtin.null_value in:              dst: %341
  call  vm.builtin.null_value in:              dst: %345
  call  vm.builtin.null_value in:              dst: %351
  call  vm.builtin.null_value in:              dst: %366
  ret   %372

@ones packed_func;

@add15 packed_func;

@zeros packed_func;

@multiply7 packed_func;

@concatenate packed_func;

@concatenate1 packed_func;

@strided_slice1 packed_func;

@divide1 packed_func;

@strided_slice2 packed_func;

@concatenate2 packed_func;

@add16 packed_func;

@subtract3 packed_func;

@ones1 packed_func;

@matmul10 packed_func;

@multiply8 packed_func;

@tir_sin packed_func;

@tir_cos packed_func;

@concatenate3 packed_func;

@equal packed_func;

@where packed_func;

@not_equal packed_func;

@where1 packed_func;

@equal1 packed_func;

@equal2 packed_func;

@add17 packed_func;

@repeat1 packed_func;

@repeat2 packed_func;

@forward:
  call  vm.builtin.check_tensor_info in: %0, i4, c[709], c[710] dst: %void
  call  vm.builtin.check_tensor_info in: %1, i4, c[711], c[712] dst: %void
  call  vm.builtin.match_shape in: %0, %void, i4, i0, i1, i0, i3, i0, i1024, i0, i1024, c[710] dst: %void
  call  vm.builtin.match_shape in: %1, %void, i4, i0, i1, i0, i1, i0, i1, i0, i2, c[712] dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[46], i0, c[713], c[4] dst: %316
  call  vm.builtin.alloc_tensor in: %316, i0, c[181], c[714] dst: %317
  call  ones2            in: %317         dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[46], i0, c[715], c[4] dst: %318
  call  vm.builtin.alloc_tensor in: %318, i0, c[181], c[716] dst: %319
  call  cumsum           in: %317, %319   dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[66], i0, c[717], c[4] dst: %320
  call  vm.builtin.alloc_tensor in: %320, i0, c[181], c[718] dst: %321
  call  subtract4        in: %319, %321   dst: %void
  call  vm.builtin.null_value in:              dst: %319
  call  vm.builtin.alloc_tensor in: %318, i0, c[181], c[719] dst: %322
  call  cumsum1          in: %317, %322   dst: %void
  call  vm.builtin.null_value in:              dst: %317
  call  vm.builtin.alloc_tensor in: %316, i0, c[181], c[720] dst: %323
  call  subtract4        in: %322, %323   dst: %void
  call  vm.builtin.null_value in:              dst: %322
  call  vm.builtin.alloc_tensor in: %318, i0, c[181], c[721] dst: %324
  call  divide2          in: %321, %324   dst: %void
  call  vm.builtin.null_value in:              dst: %321
  call  vm.builtin.alloc_tensor in: %320, i0, c[181], c[722] dst: %325
  call  divide2          in: %323, %325   dst: %void
  call  vm.builtin.null_value in:              dst: %323
  call  vm.builtin.reshape in: %325, c[723] dst: %326
  call  vm.builtin.reshape in: %324, c[723] dst: %327
  call  vm.builtin.alloc_tensor in: %316, i0, c[724], c[725] dst: %328
  call  concatenate4     in: %326, %327, %328 dst: %void
  call  vm.builtin.null_value in:              dst: %325
  call  vm.builtin.null_value in:              dst: %326
  call  vm.builtin.null_value in:              dst: %324
  call  vm.builtin.null_value in:              dst: %327
  call  vm.builtin.alloc_tensor in: %320, i0, c[724], c[726] dst: %329
  call  add18            in: %328, %328, %329 dst: %void
  call  vm.builtin.null_value in:              dst: %328
  call  vm.builtin.alloc_tensor in: %318, i0, c[724], c[727] dst: %330
  call  subtract5        in: %329, %330   dst: %void
  call  vm.builtin.null_value in:              dst: %329
  call  vm.builtin.alloc_storage in: %vm, c[676], i0, c[728], c[4] dst: %331
  call  vm.builtin.alloc_tensor in: %331, i0, c[674], c[729] dst: %332
  call  ones1            in: %332         dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[8], i0, c[730], c[4] dst: %333
  call  vm.builtin.alloc_tensor in: %333, i0, c[731], c[732] dst: %334
  call  matmul11         in: %330, %332, %334 dst: %void
  call  vm.builtin.null_value in:              dst: %330
  call  vm.builtin.null_value in:              dst: %332
  call  vm.builtin.alloc_storage in: %vm, c[66], i0, c[733], c[4] dst: %335
  call  vm.builtin.alloc_tensor in: %335, i0, c[731], c[734] dst: %336
  call  multiply9        in: %334, %336   dst: %void
  call  vm.builtin.null_value in:              dst: %334
  call  vm.builtin.alloc_tensor in: %333, i0, c[731], c[735] dst: %337
  call  tir_sin1         in: %336, %337   dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[736], i0, c[737], c[4] dst: %338
  call  vm.builtin.alloc_tensor in: %338, i0, c[731], c[738] dst: %339
  call  tir_cos1         in: %336, %339   dst: %void
  call  vm.builtin.null_value in:              dst: %336
  call  vm.builtin.alloc_storage in: %vm, c[8], i0, c[739], c[4] dst: %340
  call  vm.builtin.alloc_tensor in: %340, i0, c[740], c[741] dst: %341
  call  concatenate5     in: %337, %339, %341 dst: %void
  call  vm.builtin.null_value in:              dst: %337
  call  vm.builtin.null_value in:              dst: %339
  call  vm.builtin.alloc_storage in: %vm, c[8], i0, c[742], c[4] dst: %342
  call  vm.builtin.alloc_tensor in: %342, i0, c[743], c[744] dst: %343
  call  transpose18      in: %341, %343   dst: %void
  call  vm.builtin.null_value in:              dst: %341
  call  vm.builtin.reshape in: %343, c[615] dst: %344
  call  vm.builtin.reshape in: %344, c[615] dst: %345
  call  vm.builtin.alloc_storage in: %vm, c[8], i0, c[745], c[4] dst: %346
  call  vm.builtin.alloc_tensor in: %346, i0, c[5], c[746] dst: %347
  call  conv2d           in: %0, %3, %347 dst: %void
  call  vm.builtin.reshape in: %4, c[7]     dst: %348
  call  vm.builtin.alloc_storage in: %vm, c[8], i0, c[747], c[4] dst: %349
  call  vm.builtin.alloc_tensor in: %349, i0, c[5], c[748] dst: %350
  call  add              in: %347, %348, %350 dst: %void
  call  vm.builtin.null_value in:              dst: %348
  call  vm.builtin.null_value in:              dst: %347
  call  vm.builtin.alloc_storage in: %vm, c[8], i0, c[749], c[4] dst: %351
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[750] dst: %352
  call  transpose        in: %350, %352   dst: %void
  call  vm.builtin.null_value in:              dst: %350
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[751] dst: %353
  call  add1             in: %352, %5, %353 dst: %void
  call  vm.builtin.null_value in:              dst: %352
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[752] dst: %354
  call  layer_norm       in: %353, %6, %7, %354 dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[17], c[753] dst: %355
  call  pad              in: %354, %355   dst: %void
  call  vm.builtin.null_value in:              dst: %354
  call  vm.builtin.reshape in: %355, c[19]  dst: %356
  call  vm.builtin.alloc_tensor in: %351, i0, c[20], c[754] dst: %357
  call  transpose1       in: %356, %357   dst: %void
  call  vm.builtin.null_value in:              dst: %355
  call  vm.builtin.null_value in:              dst: %356
  call  vm.builtin.reshape in: %357, c[22]  dst: %358
  call  vm.builtin.alloc_tensor in: %346, i0, c[23], c[755] dst: %359
  call  transpose2       in: %8, %359     dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[26], c[756] dst: %360
  call  matmul           in: %358, %359, %360 dst: %void
  call  vm.builtin.null_value in:              dst: %357
  call  vm.builtin.null_value in:              dst: %358
  call  vm.builtin.null_value in:              dst: %359
  call  vm.builtin.alloc_tensor in: %351, i0, c[26], c[757] dst: %361
  call  add2             in: %360, %9, %361 dst: %void
  call  vm.builtin.null_value in:              dst: %360
  call  vm.builtin.reshape in: %361, c[29]  dst: %362
  call  vm.builtin.alloc_tensor in: %346, i0, c[30], c[758] dst: %363
  call  transpose3       in: %362, %363   dst: %void
  call  vm.builtin.null_value in:              dst: %361
  call  vm.builtin.null_value in:              dst: %362
  call  vm.builtin.reshape in: %363, c[32]  dst: %364
  call  vm.builtin.alloc_tensor in: %349, i0, c[33], c[759] dst: %365
  call  vm.builtin.alloc_tensor in: %351, i0, c[33], c[760] dst: %366
  call  vm.builtin.alloc_storage in: %vm, c[15], i0, c[761], c[4] dst: %367
  call  vm.builtin.alloc_tensor in: %367, i0, c[33], c[762] dst: %368
  call  split            in: %364, %365, %366, %368 dst: %void
  call  vm.builtin.null_value in:              dst: %363
  call  vm.builtin.null_value in:              dst: %364
  call  vm.builtin.make_tuple in: %365, %366, %368 dst: %369
  call  vm.builtin.reshape in: %365, c[38]  dst: %370
  call  vm.builtin.reshape in: %366, c[38]  dst: %371
  call  vm.builtin.reshape in: %368, c[38]  dst: %372
  call  vm.builtin.alloc_tensor in: %346, i0, c[38], c[763] dst: %373
  call  multiply         in: %370, %373   dst: %void
  call  vm.builtin.alloc_tensor in: %333, i0, c[41], c[764] dst: %374
  call  transpose4       in: %371, %374   dst: %void
  call  vm.builtin.null_value in:              dst: %366
  call  vm.builtin.null_value in:              dst: %371
  call  vm.builtin.alloc_tensor in: %351, i0, c[43], c[765] dst: %375
  call  matmul1          in: %373, %374, %375 dst: %void
  call  vm.builtin.null_value in:              dst: %373
  call  vm.builtin.null_value in:              dst: %374
  call  vm.builtin.reshape in: %12, c[45]   dst: %376
  call  vm.builtin.alloc_tensor in: %316, i0, c[48], c[766] dst: %377
  call  transpose5       in: %376, %377   dst: %void
  call  vm.builtin.null_value in:              dst: %376
  call  vm.builtin.reshape in: %377, c[50]  dst: %378
  call  vm.builtin.alloc_tensor in: %320, i0, c[52], c[767] dst: %379
  call  transpose6       in: %378, %379   dst: %void
  call  vm.builtin.null_value in:              dst: %377
  call  vm.builtin.null_value in:              dst: %378
  call  vm.builtin.reshape in: c[54], c[55] dst: %380
  call  vm.builtin.reshape in: %380, c[55]  dst: %381
  call  vm.builtin.null_value in:              dst: %380
  call  vm.builtin.reshape in: c[54], c[56] dst: %382
  call  vm.builtin.reshape in: %382, c[56]  dst: %383
  call  vm.builtin.null_value in:              dst: %382
  call  vm.builtin.alloc_storage in: %vm, c[57], i0, c[768], c[4] dst: %384
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[769] dst: %385
  call  subtract         in: %381, %383, %385 dst: %void
  call  vm.builtin.null_value in:              dst: %381
  call  vm.builtin.null_value in:              dst: %383
  call  vm.builtin.alloc_storage in: %vm, c[57], i0, c[770], c[4] dst: %386
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[771] dst: %387
  call  add3             in: %385, %387   dst: %void
  call  vm.builtin.null_value in:              dst: %385
  call  vm.builtin.alloc_tensor in: %318, i0, c[63], c[772] dst: %388
  call  take             in: %379, %387, %388 dst: %void
  call  vm.builtin.null_value in:              dst: %379
  call  vm.builtin.null_value in:              dst: %387
  call  vm.builtin.reshape in: %13, c[45]   dst: %389
  call  vm.builtin.alloc_tensor in: %316, i0, c[48], c[773] dst: %390
  call  transpose5       in: %389, %390   dst: %void
  call  vm.builtin.null_value in:              dst: %389
  call  vm.builtin.reshape in: %390, c[50]  dst: %391
  call  vm.builtin.alloc_tensor in: %320, i0, c[52], c[774] dst: %392
  call  transpose6       in: %391, %392   dst: %void
  call  vm.builtin.null_value in:              dst: %390
  call  vm.builtin.null_value in:              dst: %391
  call  vm.builtin.reshape in: c[54], c[55] dst: %393
  call  vm.builtin.reshape in: %393, c[55]  dst: %394
  call  vm.builtin.null_value in:              dst: %393
  call  vm.builtin.reshape in: c[54], c[56] dst: %395
  call  vm.builtin.reshape in: %395, c[56]  dst: %396
  call  vm.builtin.null_value in:              dst: %395
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[775] dst: %397
  call  subtract         in: %394, %396, %397 dst: %void
  call  vm.builtin.null_value in:              dst: %394
  call  vm.builtin.null_value in:              dst: %396
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[776] dst: %398
  call  add3             in: %397, %398   dst: %void
  call  vm.builtin.null_value in:              dst: %397
  call  vm.builtin.alloc_tensor in: %316, i0, c[63], c[777] dst: %399
  call  take             in: %392, %398, %399 dst: %void
  call  vm.builtin.null_value in:              dst: %392
  call  vm.builtin.null_value in:              dst: %398
  call  vm.builtin.reshape in: %370, c[72]  dst: %400
  call  vm.builtin.alloc_tensor in: %333, i0, c[73], c[778] dst: %401
  call  einsum           in: %400, %388, %401 dst: %void
  call  vm.builtin.null_value in:              dst: %388
  call  vm.builtin.alloc_tensor in: %346, i0, c[73], c[779] dst: %402
  call  einsum1          in: %400, %399, %402 dst: %void
  call  vm.builtin.null_value in:              dst: %365
  call  vm.builtin.null_value in:              dst: %370
  call  vm.builtin.null_value in:              dst: %400
  call  vm.builtin.null_value in:              dst: %399
  call  vm.builtin.reshape in: %375, c[76]  dst: %403
  call  vm.builtin.reshape in: %401, c[77]  dst: %404
  call  vm.builtin.reshape in: %402, c[78]  dst: %405
  call  vm.builtin.alloc_tensor in: %349, i0, c[76], c[780] dst: %406
  call  add4             in: %403, %404, %406 dst: %void
  call  vm.builtin.null_value in:              dst: %375
  call  vm.builtin.null_value in:              dst: %403
  call  vm.builtin.null_value in:              dst: %401
  call  vm.builtin.null_value in:              dst: %404
  call  vm.builtin.alloc_tensor in: %351, i0, c[76], c[781] dst: %407
  call  add5             in: %406, %405, %407 dst: %void
  call  vm.builtin.null_value in:              dst: %406
  call  vm.builtin.null_value in:              dst: %402
  call  vm.builtin.null_value in:              dst: %405
  call  vm.builtin.reshape in: %407, c[43]  dst: %408
  call  vm.builtin.alloc_tensor in: %349, i0, c[43], c[782] dst: %409
  call  softmax          in: %408, %409   dst: %void
  call  vm.builtin.null_value in:              dst: %407
  call  vm.builtin.null_value in:              dst: %408
  call  vm.builtin.alloc_tensor in: %333, i0, c[38], c[783] dst: %410
  call  matmul2          in: %409, %372, %410 dst: %void
  call  vm.builtin.null_value in:              dst: %409
  call  vm.builtin.null_value in:              dst: %368
  call  vm.builtin.null_value in:              dst: %372
  call  vm.builtin.reshape in: %410, c[83]  dst: %411
  call  vm.builtin.alloc_tensor in: %346, i0, c[84], c[784] dst: %412
  call  transpose7       in: %411, %412   dst: %void
  call  vm.builtin.null_value in:              dst: %410
  call  vm.builtin.null_value in:              dst: %411
  call  vm.builtin.reshape in: %412, c[22]  dst: %413
  call  vm.builtin.alloc_tensor in: %333, i0, c[86], c[785] dst: %414
  call  transpose8       in: %10, %414    dst: %void
  call  vm.builtin.alloc_tensor in: %351, i0, c[22], c[786] dst: %415
  call  matmul3          in: %413, %414, %415 dst: %void
  call  vm.builtin.null_value in:              dst: %412
  call  vm.builtin.null_value in:              dst: %413
  call  vm.builtin.null_value in:              dst: %414
  call  vm.builtin.alloc_tensor in: %333, i0, c[22], c[787] dst: %416
  call  add6             in: %415, %11, %416 dst: %void
  call  vm.builtin.null_value in:              dst: %415
  call  vm.builtin.reshape in: %416, c[20]  dst: %417
  call  vm.builtin.alloc_tensor in: %349, i0, c[19], c[788] dst: %418
  call  transpose9       in: %417, %418   dst: %void
  call  vm.builtin.null_value in:              dst: %416
  call  vm.builtin.null_value in:              dst: %417
  call  vm.builtin.reshape in: %418, c[17]  dst: %419
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[789] dst: %420
  call  strided_slice    in: %419, %420   dst: %void
  call  vm.builtin.null_value in:              dst: %418
  call  vm.builtin.null_value in:              dst: %419
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[790] dst: %421
  call  add1             in: %353, %420, %421 dst: %void
  call  vm.builtin.null_value in:              dst: %353
  call  vm.builtin.null_value in:              dst: %420
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[791] dst: %422
  call  layer_norm       in: %421, %14, %15, %422 dst: %void
  call  vm.builtin.alloc_tensor in: %351, i0, c[94], c[792] dst: %423
  call  transpose10      in: %16, %423    dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[793] dst: %424
  call  matmul4          in: %422, %423, %424 dst: %void
  call  vm.builtin.null_value in:              dst: %422
  call  vm.builtin.null_value in:              dst: %423
  call  vm.builtin.alloc_storage in: %vm, c[2], i0, c[794], c[4] dst: %425
  call  vm.builtin.alloc_tensor in: %425, i0, c[96], c[795] dst: %426
  call  add7             in: %424, %17, %426 dst: %void
  call  vm.builtin.null_value in:              dst: %424
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[796] dst: %427
  call  gelu             in: %426, %427   dst: %void
  call  vm.builtin.null_value in:              dst: %426
  call  vm.builtin.alloc_tensor in: %333, i0, c[100], c[797] dst: %428
  call  transpose11      in: %18, %428    dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[798] dst: %429
  call  matmul5          in: %427, %428, %429 dst: %void
  call  vm.builtin.null_value in:              dst: %427
  call  vm.builtin.null_value in:              dst: %428
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[799] dst: %430
  call  add8             in: %429, %19, %430 dst: %void
  call  vm.builtin.null_value in:              dst: %429
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[800] dst: %431
  call  add1             in: %421, %430, %431 dst: %void
  call  vm.builtin.null_value in:              dst: %421
  call  vm.builtin.null_value in:              dst: %430
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[801] dst: %432
  call  layer_norm       in: %431, %20, %21, %432 dst: %void
  call  vm.builtin.alloc_tensor in: %351, i0, c[17], c[802] dst: %433
  call  pad              in: %432, %433   dst: %void
  call  vm.builtin.null_value in:              dst: %432
  call  vm.builtin.reshape in: %433, c[19]  dst: %434
  call  vm.builtin.alloc_tensor in: %333, i0, c[20], c[803] dst: %435
  call  transpose1       in: %434, %435   dst: %void
  call  vm.builtin.null_value in:              dst: %433
  call  vm.builtin.null_value in:              dst: %434
  call  vm.builtin.reshape in: %435, c[22]  dst: %436
  call  vm.builtin.alloc_tensor in: %349, i0, c[23], c[804] dst: %437
  call  transpose2       in: %22, %437    dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[26], c[805] dst: %438
  call  matmul           in: %436, %437, %438 dst: %void
  call  vm.builtin.null_value in:              dst: %435
  call  vm.builtin.null_value in:              dst: %436
  call  vm.builtin.null_value in:              dst: %437
  call  vm.builtin.alloc_tensor in: %351, i0, c[26], c[806] dst: %439
  call  add2             in: %438, %23, %439 dst: %void
  call  vm.builtin.null_value in:              dst: %438
  call  vm.builtin.reshape in: %439, c[29]  dst: %440
  call  vm.builtin.alloc_tensor in: %349, i0, c[30], c[807] dst: %441
  call  transpose3       in: %440, %441   dst: %void
  call  vm.builtin.null_value in:              dst: %439
  call  vm.builtin.null_value in:              dst: %440
  call  vm.builtin.reshape in: %441, c[32]  dst: %442
  call  vm.builtin.alloc_tensor in: %333, i0, c[33], c[808] dst: %443
  call  vm.builtin.alloc_tensor in: %346, i0, c[33], c[809] dst: %444
  call  vm.builtin.alloc_tensor in: %351, i0, c[33], c[810] dst: %445
  call  split            in: %442, %443, %444, %445 dst: %void
  call  vm.builtin.null_value in:              dst: %441
  call  vm.builtin.null_value in:              dst: %442
  call  vm.builtin.make_tuple in: %443, %444, %445 dst: %446
  call  vm.builtin.reshape in: %443, c[38]  dst: %447
  call  vm.builtin.reshape in: %444, c[38]  dst: %448
  call  vm.builtin.reshape in: %445, c[38]  dst: %449
  call  vm.builtin.alloc_tensor in: %349, i0, c[38], c[811] dst: %450
  call  multiply         in: %447, %450   dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[41], c[812] dst: %451
  call  transpose4       in: %448, %451   dst: %void
  call  vm.builtin.null_value in:              dst: %444
  call  vm.builtin.null_value in:              dst: %448
  call  vm.builtin.alloc_tensor in: %346, i0, c[43], c[813] dst: %452
  call  matmul1          in: %450, %451, %452 dst: %void
  call  vm.builtin.null_value in:              dst: %450
  call  vm.builtin.null_value in:              dst: %451
  call  vm.builtin.reshape in: %26, c[45]   dst: %453
  call  vm.builtin.alloc_tensor in: %320, i0, c[48], c[814] dst: %454
  call  transpose5       in: %453, %454   dst: %void
  call  vm.builtin.null_value in:              dst: %453
  call  vm.builtin.reshape in: %454, c[50]  dst: %455
  call  vm.builtin.alloc_tensor in: %318, i0, c[52], c[815] dst: %456
  call  transpose6       in: %455, %456   dst: %void
  call  vm.builtin.null_value in:              dst: %454
  call  vm.builtin.null_value in:              dst: %455
  call  vm.builtin.reshape in: c[54], c[55] dst: %457
  call  vm.builtin.reshape in: %457, c[55]  dst: %458
  call  vm.builtin.null_value in:              dst: %457
  call  vm.builtin.reshape in: c[54], c[56] dst: %459
  call  vm.builtin.reshape in: %459, c[56]  dst: %460
  call  vm.builtin.null_value in:              dst: %459
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[816] dst: %461
  call  subtract         in: %458, %460, %461 dst: %void
  call  vm.builtin.null_value in:              dst: %458
  call  vm.builtin.null_value in:              dst: %460
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[817] dst: %462
  call  add3             in: %461, %462   dst: %void
  call  vm.builtin.null_value in:              dst: %461
  call  vm.builtin.alloc_tensor in: %316, i0, c[63], c[818] dst: %463
  call  take             in: %456, %462, %463 dst: %void
  call  vm.builtin.null_value in:              dst: %456
  call  vm.builtin.null_value in:              dst: %462
  call  vm.builtin.reshape in: %27, c[45]   dst: %464
  call  vm.builtin.alloc_tensor in: %320, i0, c[48], c[819] dst: %465
  call  transpose5       in: %464, %465   dst: %void
  call  vm.builtin.null_value in:              dst: %464
  call  vm.builtin.reshape in: %465, c[50]  dst: %466
  call  vm.builtin.alloc_tensor in: %318, i0, c[52], c[820] dst: %467
  call  transpose6       in: %466, %467   dst: %void
  call  vm.builtin.null_value in:              dst: %465
  call  vm.builtin.null_value in:              dst: %466
  call  vm.builtin.reshape in: c[54], c[55] dst: %468
  call  vm.builtin.reshape in: %468, c[55]  dst: %469
  call  vm.builtin.null_value in:              dst: %468
  call  vm.builtin.reshape in: c[54], c[56] dst: %470
  call  vm.builtin.reshape in: %470, c[56]  dst: %471
  call  vm.builtin.null_value in:              dst: %470
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[821] dst: %472
  call  subtract         in: %469, %471, %472 dst: %void
  call  vm.builtin.null_value in:              dst: %469
  call  vm.builtin.null_value in:              dst: %471
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[822] dst: %473
  call  add3             in: %472, %473   dst: %void
  call  vm.builtin.null_value in:              dst: %472
  call  vm.builtin.alloc_tensor in: %320, i0, c[63], c[823] dst: %474
  call  take             in: %467, %473, %474 dst: %void
  call  vm.builtin.null_value in:              dst: %467
  call  vm.builtin.null_value in:              dst: %473
  call  vm.builtin.reshape in: %447, c[72]  dst: %475
  call  vm.builtin.alloc_tensor in: %349, i0, c[73], c[824] dst: %476
  call  einsum           in: %475, %463, %476 dst: %void
  call  vm.builtin.null_value in:              dst: %463
  call  vm.builtin.alloc_tensor in: %367, i0, c[73], c[825] dst: %477
  call  einsum1          in: %475, %474, %477 dst: %void
  call  vm.builtin.null_value in:              dst: %443
  call  vm.builtin.null_value in:              dst: %447
  call  vm.builtin.null_value in:              dst: %475
  call  vm.builtin.null_value in:              dst: %474
  call  vm.builtin.reshape in: %452, c[76]  dst: %478
  call  vm.builtin.reshape in: %476, c[77]  dst: %479
  call  vm.builtin.reshape in: %477, c[78]  dst: %480
  call  vm.builtin.alloc_tensor in: %333, i0, c[76], c[826] dst: %481
  call  add4             in: %478, %479, %481 dst: %void
  call  vm.builtin.null_value in:              dst: %452
  call  vm.builtin.null_value in:              dst: %478
  call  vm.builtin.null_value in:              dst: %476
  call  vm.builtin.null_value in:              dst: %479
  call  vm.builtin.alloc_tensor in: %346, i0, c[76], c[827] dst: %482
  call  add5             in: %481, %480, %482 dst: %void
  call  vm.builtin.null_value in:              dst: %481
  call  vm.builtin.null_value in:              dst: %477
  call  vm.builtin.null_value in:              dst: %480
  call  vm.builtin.reshape in: %482, c[43]  dst: %483
  call  vm.builtin.alloc_tensor in: %349, i0, c[43], c[828] dst: %484
  call  softmax          in: %483, %484   dst: %void
  call  vm.builtin.null_value in:              dst: %482
  call  vm.builtin.null_value in:              dst: %483
  call  vm.builtin.alloc_tensor in: %333, i0, c[38], c[829] dst: %485
  call  matmul2          in: %484, %449, %485 dst: %void
  call  vm.builtin.null_value in:              dst: %484
  call  vm.builtin.null_value in:              dst: %445
  call  vm.builtin.null_value in:              dst: %449
  call  vm.builtin.reshape in: %485, c[83]  dst: %486
  call  vm.builtin.alloc_tensor in: %346, i0, c[84], c[830] dst: %487
  call  transpose7       in: %486, %487   dst: %void
  call  vm.builtin.null_value in:              dst: %485
  call  vm.builtin.null_value in:              dst: %486
  call  vm.builtin.reshape in: %487, c[22]  dst: %488
  call  vm.builtin.alloc_tensor in: %338, i0, c[86], c[831] dst: %489
  call  transpose8       in: %24, %489    dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[22], c[832] dst: %490
  call  matmul3          in: %488, %489, %490 dst: %void
  call  vm.builtin.null_value in:              dst: %487
  call  vm.builtin.null_value in:              dst: %488
  call  vm.builtin.null_value in:              dst: %489
  call  vm.builtin.alloc_tensor in: %351, i0, c[22], c[833] dst: %491
  call  add6             in: %490, %25, %491 dst: %void
  call  vm.builtin.null_value in:              dst: %490
  call  vm.builtin.reshape in: %491, c[20]  dst: %492
  call  vm.builtin.alloc_tensor in: %333, i0, c[19], c[834] dst: %493
  call  transpose9       in: %492, %493   dst: %void
  call  vm.builtin.null_value in:              dst: %491
  call  vm.builtin.null_value in:              dst: %492
  call  vm.builtin.reshape in: %493, c[17]  dst: %494
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[835] dst: %495
  call  strided_slice    in: %494, %495   dst: %void
  call  vm.builtin.null_value in:              dst: %493
  call  vm.builtin.null_value in:              dst: %494
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[836] dst: %496
  call  add1             in: %431, %495, %496 dst: %void
  call  vm.builtin.null_value in:              dst: %431
  call  vm.builtin.null_value in:              dst: %495
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[837] dst: %497
  call  layer_norm       in: %496, %28, %29, %497 dst: %void
  call  vm.builtin.alloc_tensor in: %333, i0, c[94], c[838] dst: %498
  call  transpose10      in: %30, %498    dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[839] dst: %499
  call  matmul4          in: %497, %498, %499 dst: %void
  call  vm.builtin.null_value in:              dst: %497
  call  vm.builtin.null_value in:              dst: %498
  call  vm.builtin.alloc_storage in: %vm, c[2], i0, c[840], c[4] dst: %500
  call  vm.builtin.alloc_tensor in: %500, i0, c[96], c[841] dst: %501
  call  add7             in: %499, %31, %501 dst: %void
  call  vm.builtin.null_value in:              dst: %499
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[842] dst: %502
  call  gelu             in: %501, %502   dst: %void
  call  vm.builtin.null_value in:              dst: %501
  call  vm.builtin.alloc_tensor in: %340, i0, c[100], c[843] dst: %503
  call  transpose11      in: %32, %503    dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[844] dst: %504
  call  matmul5          in: %502, %503, %504 dst: %void
  call  vm.builtin.null_value in:              dst: %502
  call  vm.builtin.null_value in:              dst: %503
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[845] dst: %505
  call  add8             in: %504, %33, %505 dst: %void
  call  vm.builtin.null_value in:              dst: %504
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[846] dst: %506
  call  add1             in: %496, %505, %506 dst: %void
  call  vm.builtin.null_value in:              dst: %496
  call  vm.builtin.null_value in:              dst: %505
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[847] dst: %507
  call  layer_norm       in: %506, %34, %35, %507 dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[23], c[848] dst: %508
  call  transpose2       in: %36, %508    dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[152], c[849] dst: %509
  call  matmul6          in: %507, %508, %509 dst: %void
  call  vm.builtin.null_value in:              dst: %507
  call  vm.builtin.null_value in:              dst: %508
  call  vm.builtin.alloc_tensor in: %351, i0, c[152], c[850] dst: %510
  call  add9             in: %509, %37, %510 dst: %void
  call  vm.builtin.null_value in:              dst: %509
  call  vm.builtin.reshape in: %510, c[155] dst: %511
  call  vm.builtin.alloc_tensor in: %340, i0, c[156], c[851] dst: %512
  call  transpose12      in: %511, %512   dst: %void
  call  vm.builtin.null_value in:              dst: %510
  call  vm.builtin.null_value in:              dst: %511
  call  vm.builtin.reshape in: %512, c[158] dst: %513
  call  vm.builtin.alloc_tensor in: %346, i0, c[159], c[852] dst: %514
  call  vm.builtin.alloc_tensor in: %349, i0, c[159], c[853] dst: %515
  call  vm.builtin.alloc_tensor in: %351, i0, c[159], c[854] dst: %516
  call  split1           in: %513, %514, %515, %516 dst: %void
  call  vm.builtin.null_value in:              dst: %512
  call  vm.builtin.null_value in:              dst: %513
  call  vm.builtin.make_tuple in: %514, %515, %516 dst: %517
  call  vm.builtin.reshape in: %514, c[163] dst: %518
  call  vm.builtin.reshape in: %515, c[163] dst: %519
  call  vm.builtin.reshape in: %516, c[163] dst: %520
  call  vm.builtin.alloc_tensor in: %340, i0, c[163], c[855] dst: %521
  call  multiply3        in: %518, %521   dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[165], c[856] dst: %522
  call  transpose13      in: %519, %522   dst: %void
  call  vm.builtin.null_value in:              dst: %515
  call  vm.builtin.null_value in:              dst: %519
  call  vm.builtin.alloc_tensor in: %425, i0, c[168], c[857] dst: %523
  call  matmul7          in: %521, %522, %523 dst: %void
  call  vm.builtin.null_value in:              dst: %521
  call  vm.builtin.null_value in:              dst: %522
  call  vm.builtin.reshape in: %40, c[170]  dst: %524
  call  vm.builtin.alloc_tensor in: %318, i0, c[171], c[858] dst: %525
  call  transpose14      in: %524, %525   dst: %void
  call  vm.builtin.null_value in:              dst: %524
  call  vm.builtin.reshape in: %525, c[173] dst: %526
  call  vm.builtin.alloc_tensor in: %316, i0, c[174], c[859] dst: %527
  call  transpose15      in: %526, %527   dst: %void
  call  vm.builtin.null_value in:              dst: %525
  call  vm.builtin.null_value in:              dst: %526
  call  vm.builtin.reshape in: c[176], c[177] dst: %528
  call  vm.builtin.reshape in: %528, c[177] dst: %529
  call  vm.builtin.null_value in:              dst: %528
  call  vm.builtin.reshape in: c[176], c[178] dst: %530
  call  vm.builtin.reshape in: %530, c[178] dst: %531
  call  vm.builtin.null_value in:              dst: %530
  call  vm.builtin.alloc_storage in: %vm, c[179], i0, c[860], c[4] dst: %532
  call  vm.builtin.alloc_tensor in: %532, i0, c[181], c[861] dst: %533
  call  subtract1        in: %529, %531, %533 dst: %void
  call  vm.builtin.null_value in:              dst: %529
  call  vm.builtin.null_value in:              dst: %531
  call  vm.builtin.alloc_storage in: %vm, c[179], i0, c[862], c[4] dst: %534
  call  vm.builtin.alloc_tensor in: %534, i0, c[181], c[863] dst: %535
  call  add10            in: %533, %535   dst: %void
  call  vm.builtin.null_value in:              dst: %533
  call  vm.builtin.alloc_tensor in: %335, i0, c[186], c[864] dst: %536
  call  take1            in: %527, %535, %536 dst: %void
  call  vm.builtin.null_value in:              dst: %527
  call  vm.builtin.null_value in:              dst: %535
  call  vm.builtin.reshape in: %41, c[170]  dst: %537
  call  vm.builtin.alloc_tensor in: %320, i0, c[171], c[865] dst: %538
  call  transpose14      in: %537, %538   dst: %void
  call  vm.builtin.null_value in:              dst: %537
  call  vm.builtin.reshape in: %538, c[173] dst: %539
  call  vm.builtin.alloc_tensor in: %318, i0, c[174], c[866] dst: %540
  call  transpose15      in: %539, %540   dst: %void
  call  vm.builtin.null_value in:              dst: %538
  call  vm.builtin.null_value in:              dst: %539
  call  vm.builtin.reshape in: c[176], c[177] dst: %541
  call  vm.builtin.reshape in: %541, c[177] dst: %542
  call  vm.builtin.null_value in:              dst: %541
  call  vm.builtin.reshape in: c[176], c[178] dst: %543
  call  vm.builtin.reshape in: %543, c[178] dst: %544
  call  vm.builtin.null_value in:              dst: %543
  call  vm.builtin.alloc_tensor in: %532, i0, c[181], c[867] dst: %545
  call  subtract1        in: %542, %544, %545 dst: %void
  call  vm.builtin.null_value in:              dst: %542
  call  vm.builtin.null_value in:              dst: %544
  call  vm.builtin.alloc_tensor in: %534, i0, c[181], c[868] dst: %546
  call  add10            in: %545, %546   dst: %void
  call  vm.builtin.null_value in:              dst: %545
  call  vm.builtin.alloc_tensor in: %338, i0, c[186], c[869] dst: %547
  call  take1            in: %540, %546, %547 dst: %void
  call  vm.builtin.null_value in:              dst: %540
  call  vm.builtin.null_value in:              dst: %546
  call  vm.builtin.reshape in: %518, c[194] dst: %548
  call  vm.builtin.alloc_tensor in: %349, i0, c[194], c[870] dst: %549
  call  einsum2          in: %548, %536, %549 dst: %void
  call  vm.builtin.null_value in:              dst: %536
  call  vm.builtin.alloc_tensor in: %340, i0, c[194], c[871] dst: %550
  call  einsum3          in: %548, %547, %550 dst: %void
  call  vm.builtin.null_value in:              dst: %514
  call  vm.builtin.null_value in:              dst: %518
  call  vm.builtin.null_value in:              dst: %548
  call  vm.builtin.null_value in:              dst: %547
  call  vm.builtin.reshape in: %523, c[197] dst: %551
  call  vm.builtin.reshape in: %549, c[198] dst: %552
  call  vm.builtin.reshape in: %550, c[199] dst: %553
  call  vm.builtin.alloc_tensor in: %500, i0, c[197], c[872] dst: %554
  call  add11            in: %551, %552, %554 dst: %void
  call  vm.builtin.null_value in:              dst: %523
  call  vm.builtin.null_value in:              dst: %551
  call  vm.builtin.null_value in:              dst: %549
  call  vm.builtin.null_value in:              dst: %552
  call  vm.builtin.alloc_tensor in: %425, i0, c[197], c[873] dst: %555
  call  add12            in: %554, %553, %555 dst: %void
  call  vm.builtin.null_value in:              dst: %554
  call  vm.builtin.null_value in:              dst: %550
  call  vm.builtin.null_value in:              dst: %553
  call  vm.builtin.reshape in: %555, c[168] dst: %556
  call  vm.builtin.alloc_tensor in: %500, i0, c[168], c[874] dst: %557
  call  softmax1         in: %556, %557   dst: %void
  call  vm.builtin.null_value in:              dst: %555
  call  vm.builtin.null_value in:              dst: %556
  call  vm.builtin.alloc_tensor in: %346, i0, c[163], c[875] dst: %558
  call  matmul8          in: %557, %520, %558 dst: %void
  call  vm.builtin.null_value in:              dst: %557
  call  vm.builtin.null_value in:              dst: %516
  call  vm.builtin.null_value in:              dst: %520
  call  vm.builtin.reshape in: %558, c[204] dst: %559
  call  vm.builtin.alloc_tensor in: %349, i0, c[205], c[876] dst: %560
  call  transpose16      in: %559, %560   dst: %void
  call  vm.builtin.null_value in:              dst: %558
  call  vm.builtin.null_value in:              dst: %559
  call  vm.builtin.reshape in: %560, c[11]  dst: %561
  call  vm.builtin.alloc_tensor in: %338, i0, c[86], c[877] dst: %562
  call  transpose8       in: %38, %562    dst: %void
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[878] dst: %563
  call  matmul9          in: %561, %562, %563 dst: %void
  call  vm.builtin.null_value in:              dst: %560
  call  vm.builtin.null_value in:              dst: %561
  call  vm.builtin.null_value in:              dst: %562
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[879] dst: %564
  call  add8             in: %563, %39, %564 dst: %void
  call  vm.builtin.null_value in:              dst: %563
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[880] dst: %565
  call  add1             in: %506, %564, %565 dst: %void
  call  vm.builtin.null_value in:              dst: %506
  call  vm.builtin.null_value in:              dst: %564
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[881] dst: %566
  call  layer_norm       in: %565, %42, %43, %566 dst: %void
  call  vm.builtin.alloc_tensor in: %340, i0, c[94], c[882] dst: %567
  call  transpose10      in: %44, %567    dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[883] dst: %568
  call  matmul4          in: %566, %567, %568 dst: %void
  call  vm.builtin.null_value in:              dst: %566
  call  vm.builtin.null_value in:              dst: %567
  call  vm.builtin.alloc_tensor in: %425, i0, c[96], c[884] dst: %569
  call  add7             in: %568, %45, %569 dst: %void
  call  vm.builtin.null_value in:              dst: %568
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[885] dst: %570
  call  gelu             in: %569, %570   dst: %void
  call  vm.builtin.null_value in:              dst: %569
  call  vm.builtin.alloc_tensor in: %333, i0, c[100], c[886] dst: %571
  call  transpose11      in: %46, %571    dst: %void
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[887] dst: %572
  call  matmul5          in: %570, %571, %572 dst: %void
  call  vm.builtin.null_value in:              dst: %570
  call  vm.builtin.null_value in:              dst: %571
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[888] dst: %573
  call  add8             in: %572, %47, %573 dst: %void
  call  vm.builtin.null_value in:              dst: %572
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[889] dst: %574
  call  add1             in: %565, %573, %574 dst: %void
  call  vm.builtin.null_value in:              dst: %565
  call  vm.builtin.null_value in:              dst: %573
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[890] dst: %575
  call  layer_norm       in: %574, %48, %49, %575 dst: %void
  call  vm.builtin.alloc_tensor in: %351, i0, c[17], c[891] dst: %576
  call  pad              in: %575, %576   dst: %void
  call  vm.builtin.null_value in:              dst: %575
  call  vm.builtin.reshape in: %576, c[19]  dst: %577
  call  vm.builtin.alloc_tensor in: %346, i0, c[20], c[892] dst: %578
  call  transpose1       in: %577, %578   dst: %void
  call  vm.builtin.null_value in:              dst: %576
  call  vm.builtin.null_value in:              dst: %577
  call  vm.builtin.reshape in: %578, c[22]  dst: %579
  call  vm.builtin.alloc_tensor in: %349, i0, c[23], c[893] dst: %580
  call  transpose2       in: %50, %580    dst: %void
  call  vm.builtin.alloc_tensor in: %333, i0, c[26], c[894] dst: %581
  call  matmul           in: %579, %580, %581 dst: %void
  call  vm.builtin.null_value in:              dst: %578
  call  vm.builtin.null_value in:              dst: %579
  call  vm.builtin.null_value in:              dst: %580
  call  vm.builtin.alloc_tensor in: %351, i0, c[26], c[895] dst: %582
  call  add2             in: %581, %51, %582 dst: %void
  call  vm.builtin.null_value in:              dst: %581
  call  vm.builtin.reshape in: %582, c[29]  dst: %583
  call  vm.builtin.alloc_tensor in: %346, i0, c[30], c[896] dst: %584
  call  transpose3       in: %583, %584   dst: %void
  call  vm.builtin.null_value in:              dst: %582
  call  vm.builtin.null_value in:              dst: %583
  call  vm.builtin.reshape in: %584, c[32]  dst: %585
  call  vm.builtin.alloc_tensor in: %349, i0, c[33], c[897] dst: %586
  call  vm.builtin.alloc_tensor in: %333, i0, c[33], c[898] dst: %587
  call  vm.builtin.alloc_tensor in: %351, i0, c[33], c[899] dst: %588
  call  split            in: %585, %586, %587, %588 dst: %void
  call  vm.builtin.null_value in:              dst: %584
  call  vm.builtin.null_value in:              dst: %585
  call  vm.builtin.make_tuple in: %586, %587, %588 dst: %589
  call  vm.builtin.reshape in: %586, c[38]  dst: %590
  call  vm.builtin.reshape in: %587, c[38]  dst: %591
  call  vm.builtin.reshape in: %588, c[38]  dst: %592
  call  vm.builtin.alloc_tensor in: %346, i0, c[38], c[900] dst: %593
  call  multiply         in: %590, %593   dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[41], c[901] dst: %594
  call  transpose4       in: %591, %594   dst: %void
  call  vm.builtin.null_value in:              dst: %587
  call  vm.builtin.null_value in:              dst: %591
  call  vm.builtin.alloc_tensor in: %333, i0, c[43], c[902] dst: %595
  call  matmul1          in: %593, %594, %595 dst: %void
  call  vm.builtin.null_value in:              dst: %593
  call  vm.builtin.null_value in:              dst: %594
  call  vm.builtin.reshape in: %54, c[45]   dst: %596
  call  vm.builtin.alloc_tensor in: %316, i0, c[48], c[903] dst: %597
  call  transpose5       in: %596, %597   dst: %void
  call  vm.builtin.null_value in:              dst: %596
  call  vm.builtin.reshape in: %597, c[50]  dst: %598
  call  vm.builtin.alloc_tensor in: %320, i0, c[52], c[904] dst: %599
  call  transpose6       in: %598, %599   dst: %void
  call  vm.builtin.null_value in:              dst: %597
  call  vm.builtin.null_value in:              dst: %598
  call  vm.builtin.reshape in: c[54], c[55] dst: %600
  call  vm.builtin.reshape in: %600, c[55]  dst: %601
  call  vm.builtin.null_value in:              dst: %600
  call  vm.builtin.reshape in: c[54], c[56] dst: %602
  call  vm.builtin.reshape in: %602, c[56]  dst: %603
  call  vm.builtin.null_value in:              dst: %602
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[905] dst: %604
  call  subtract         in: %601, %603, %604 dst: %void
  call  vm.builtin.null_value in:              dst: %601
  call  vm.builtin.null_value in:              dst: %603
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[906] dst: %605
  call  add3             in: %604, %605   dst: %void
  call  vm.builtin.null_value in:              dst: %604
  call  vm.builtin.alloc_tensor in: %318, i0, c[63], c[907] dst: %606
  call  take             in: %599, %605, %606 dst: %void
  call  vm.builtin.null_value in:              dst: %599
  call  vm.builtin.null_value in:              dst: %605
  call  vm.builtin.reshape in: %55, c[45]   dst: %607
  call  vm.builtin.alloc_tensor in: %316, i0, c[48], c[908] dst: %608
  call  transpose5       in: %607, %608   dst: %void
  call  vm.builtin.null_value in:              dst: %607
  call  vm.builtin.reshape in: %608, c[50]  dst: %609
  call  vm.builtin.alloc_tensor in: %320, i0, c[52], c[909] dst: %610
  call  transpose6       in: %609, %610   dst: %void
  call  vm.builtin.null_value in:              dst: %608
  call  vm.builtin.null_value in:              dst: %609
  call  vm.builtin.reshape in: c[54], c[55] dst: %611
  call  vm.builtin.reshape in: %611, c[55]  dst: %612
  call  vm.builtin.null_value in:              dst: %611
  call  vm.builtin.reshape in: c[54], c[56] dst: %613
  call  vm.builtin.reshape in: %613, c[56]  dst: %614
  call  vm.builtin.null_value in:              dst: %613
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[910] dst: %615
  call  subtract         in: %612, %614, %615 dst: %void
  call  vm.builtin.null_value in:              dst: %612
  call  vm.builtin.null_value in:              dst: %614
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[911] dst: %616
  call  add3             in: %615, %616   dst: %void
  call  vm.builtin.null_value in:              dst: %615
  call  vm.builtin.alloc_tensor in: %316, i0, c[63], c[912] dst: %617
  call  take             in: %610, %616, %617 dst: %void
  call  vm.builtin.null_value in:              dst: %610
  call  vm.builtin.null_value in:              dst: %616
  call  vm.builtin.reshape in: %590, c[72]  dst: %618
  call  vm.builtin.alloc_tensor in: %346, i0, c[73], c[913] dst: %619
  call  einsum           in: %618, %606, %619 dst: %void
  call  vm.builtin.null_value in:              dst: %606
  call  vm.builtin.alloc_tensor in: %367, i0, c[73], c[914] dst: %620
  call  einsum1          in: %618, %617, %620 dst: %void
  call  vm.builtin.null_value in:              dst: %586
  call  vm.builtin.null_value in:              dst: %590
  call  vm.builtin.null_value in:              dst: %618
  call  vm.builtin.null_value in:              dst: %617
  call  vm.builtin.reshape in: %595, c[76]  dst: %621
  call  vm.builtin.reshape in: %619, c[77]  dst: %622
  call  vm.builtin.reshape in: %620, c[78]  dst: %623
  call  vm.builtin.alloc_tensor in: %349, i0, c[76], c[915] dst: %624
  call  add4             in: %621, %622, %624 dst: %void
  call  vm.builtin.null_value in:              dst: %595
  call  vm.builtin.null_value in:              dst: %621
  call  vm.builtin.null_value in:              dst: %619
  call  vm.builtin.null_value in:              dst: %622
  call  vm.builtin.alloc_tensor in: %333, i0, c[76], c[916] dst: %625
  call  add5             in: %624, %623, %625 dst: %void
  call  vm.builtin.null_value in:              dst: %624
  call  vm.builtin.null_value in:              dst: %620
  call  vm.builtin.null_value in:              dst: %623
  call  vm.builtin.reshape in: %625, c[43]  dst: %626
  call  vm.builtin.alloc_tensor in: %346, i0, c[43], c[917] dst: %627
  call  softmax          in: %626, %627   dst: %void
  call  vm.builtin.null_value in:              dst: %625
  call  vm.builtin.null_value in:              dst: %626
  call  vm.builtin.alloc_tensor in: %349, i0, c[38], c[918] dst: %628
  call  matmul2          in: %627, %592, %628 dst: %void
  call  vm.builtin.null_value in:              dst: %627
  call  vm.builtin.null_value in:              dst: %588
  call  vm.builtin.null_value in:              dst: %592
  call  vm.builtin.reshape in: %628, c[83]  dst: %629
  call  vm.builtin.alloc_tensor in: %333, i0, c[84], c[919] dst: %630
  call  transpose7       in: %629, %630   dst: %void
  call  vm.builtin.null_value in:              dst: %628
  call  vm.builtin.null_value in:              dst: %629
  call  vm.builtin.reshape in: %630, c[22]  dst: %631
  call  vm.builtin.alloc_tensor in: %338, i0, c[86], c[920] dst: %632
  call  transpose8       in: %52, %632    dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[22], c[921] dst: %633
  call  matmul3          in: %631, %632, %633 dst: %void
  call  vm.builtin.null_value in:              dst: %630
  call  vm.builtin.null_value in:              dst: %631
  call  vm.builtin.null_value in:              dst: %632
  call  vm.builtin.alloc_tensor in: %351, i0, c[22], c[922] dst: %634
  call  add6             in: %633, %53, %634 dst: %void
  call  vm.builtin.null_value in:              dst: %633
  call  vm.builtin.reshape in: %634, c[20]  dst: %635
  call  vm.builtin.alloc_tensor in: %349, i0, c[19], c[923] dst: %636
  call  transpose9       in: %635, %636   dst: %void
  call  vm.builtin.null_value in:              dst: %634
  call  vm.builtin.null_value in:              dst: %635
  call  vm.builtin.reshape in: %636, c[17]  dst: %637
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[924] dst: %638
  call  strided_slice    in: %637, %638   dst: %void
  call  vm.builtin.null_value in:              dst: %636
  call  vm.builtin.null_value in:              dst: %637
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[925] dst: %639
  call  add1             in: %574, %638, %639 dst: %void
  call  vm.builtin.null_value in:              dst: %574
  call  vm.builtin.null_value in:              dst: %638
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[926] dst: %640
  call  layer_norm       in: %639, %56, %57, %640 dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[94], c[927] dst: %641
  call  transpose10      in: %58, %641    dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[928] dst: %642
  call  matmul4          in: %640, %641, %642 dst: %void
  call  vm.builtin.null_value in:              dst: %640
  call  vm.builtin.null_value in:              dst: %641
  call  vm.builtin.alloc_tensor in: %500, i0, c[96], c[929] dst: %643
  call  add7             in: %642, %59, %643 dst: %void
  call  vm.builtin.null_value in:              dst: %642
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[930] dst: %644
  call  gelu             in: %643, %644   dst: %void
  call  vm.builtin.null_value in:              dst: %643
  call  vm.builtin.alloc_tensor in: %340, i0, c[100], c[931] dst: %645
  call  transpose11      in: %60, %645    dst: %void
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[932] dst: %646
  call  matmul5          in: %644, %645, %646 dst: %void
  call  vm.builtin.null_value in:              dst: %644
  call  vm.builtin.null_value in:              dst: %645
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[933] dst: %647
  call  add8             in: %646, %61, %647 dst: %void
  call  vm.builtin.null_value in:              dst: %646
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[934] dst: %648
  call  add1             in: %639, %647, %648 dst: %void
  call  vm.builtin.null_value in:              dst: %639
  call  vm.builtin.null_value in:              dst: %647
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[935] dst: %649
  call  layer_norm       in: %648, %62, %63, %649 dst: %void
  call  vm.builtin.alloc_tensor in: %333, i0, c[17], c[936] dst: %650
  call  pad              in: %649, %650   dst: %void
  call  vm.builtin.null_value in:              dst: %649
  call  vm.builtin.reshape in: %650, c[19]  dst: %651
  call  vm.builtin.alloc_tensor in: %346, i0, c[20], c[937] dst: %652
  call  transpose1       in: %651, %652   dst: %void
  call  vm.builtin.null_value in:              dst: %650
  call  vm.builtin.null_value in:              dst: %651
  call  vm.builtin.reshape in: %652, c[22]  dst: %653
  call  vm.builtin.alloc_tensor in: %351, i0, c[23], c[938] dst: %654
  call  transpose2       in: %64, %654    dst: %void
  call  vm.builtin.alloc_tensor in: %340, i0, c[26], c[939] dst: %655
  call  matmul           in: %653, %654, %655 dst: %void
  call  vm.builtin.null_value in:              dst: %652
  call  vm.builtin.null_value in:              dst: %653
  call  vm.builtin.null_value in:              dst: %654
  call  vm.builtin.alloc_tensor in: %333, i0, c[26], c[940] dst: %656
  call  add2             in: %655, %65, %656 dst: %void
  call  vm.builtin.null_value in:              dst: %655
  call  vm.builtin.reshape in: %656, c[29]  dst: %657
  call  vm.builtin.alloc_tensor in: %346, i0, c[30], c[941] dst: %658
  call  transpose3       in: %657, %658   dst: %void
  call  vm.builtin.null_value in:              dst: %656
  call  vm.builtin.null_value in:              dst: %657
  call  vm.builtin.reshape in: %658, c[32]  dst: %659
  call  vm.builtin.alloc_tensor in: %351, i0, c[33], c[942] dst: %660
  call  vm.builtin.alloc_tensor in: %340, i0, c[33], c[943] dst: %661
  call  vm.builtin.alloc_tensor in: %333, i0, c[33], c[944] dst: %662
  call  split            in: %659, %660, %661, %662 dst: %void
  call  vm.builtin.null_value in:              dst: %658
  call  vm.builtin.null_value in:              dst: %659
  call  vm.builtin.make_tuple in: %660, %661, %662 dst: %663
  call  vm.builtin.reshape in: %660, c[38]  dst: %664
  call  vm.builtin.reshape in: %661, c[38]  dst: %665
  call  vm.builtin.reshape in: %662, c[38]  dst: %666
  call  vm.builtin.alloc_tensor in: %346, i0, c[38], c[945] dst: %667
  call  multiply         in: %664, %667   dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[41], c[946] dst: %668
  call  transpose4       in: %665, %668   dst: %void
  call  vm.builtin.null_value in:              dst: %661
  call  vm.builtin.null_value in:              dst: %665
  call  vm.builtin.alloc_tensor in: %340, i0, c[43], c[947] dst: %669
  call  matmul1          in: %667, %668, %669 dst: %void
  call  vm.builtin.null_value in:              dst: %667
  call  vm.builtin.null_value in:              dst: %668
  call  vm.builtin.reshape in: %68, c[45]   dst: %670
  call  vm.builtin.alloc_tensor in: %320, i0, c[48], c[948] dst: %671
  call  transpose5       in: %670, %671   dst: %void
  call  vm.builtin.null_value in:              dst: %670
  call  vm.builtin.reshape in: %671, c[50]  dst: %672
  call  vm.builtin.alloc_tensor in: %318, i0, c[52], c[949] dst: %673
  call  transpose6       in: %672, %673   dst: %void
  call  vm.builtin.null_value in:              dst: %671
  call  vm.builtin.null_value in:              dst: %672
  call  vm.builtin.reshape in: c[54], c[55] dst: %674
  call  vm.builtin.reshape in: %674, c[55]  dst: %675
  call  vm.builtin.null_value in:              dst: %674
  call  vm.builtin.reshape in: c[54], c[56] dst: %676
  call  vm.builtin.reshape in: %676, c[56]  dst: %677
  call  vm.builtin.null_value in:              dst: %676
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[950] dst: %678
  call  subtract         in: %675, %677, %678 dst: %void
  call  vm.builtin.null_value in:              dst: %675
  call  vm.builtin.null_value in:              dst: %677
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[951] dst: %679
  call  add3             in: %678, %679   dst: %void
  call  vm.builtin.null_value in:              dst: %678
  call  vm.builtin.alloc_tensor in: %316, i0, c[63], c[952] dst: %680
  call  take             in: %673, %679, %680 dst: %void
  call  vm.builtin.null_value in:              dst: %673
  call  vm.builtin.null_value in:              dst: %679
  call  vm.builtin.reshape in: %69, c[45]   dst: %681
  call  vm.builtin.alloc_tensor in: %320, i0, c[48], c[953] dst: %682
  call  transpose5       in: %681, %682   dst: %void
  call  vm.builtin.null_value in:              dst: %681
  call  vm.builtin.reshape in: %682, c[50]  dst: %683
  call  vm.builtin.alloc_tensor in: %318, i0, c[52], c[954] dst: %684
  call  transpose6       in: %683, %684   dst: %void
  call  vm.builtin.null_value in:              dst: %682
  call  vm.builtin.null_value in:              dst: %683
  call  vm.builtin.reshape in: c[54], c[55] dst: %685
  call  vm.builtin.reshape in: %685, c[55]  dst: %686
  call  vm.builtin.null_value in:              dst: %685
  call  vm.builtin.reshape in: c[54], c[56] dst: %687
  call  vm.builtin.reshape in: %687, c[56]  dst: %688
  call  vm.builtin.null_value in:              dst: %687
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[955] dst: %689
  call  subtract         in: %686, %688, %689 dst: %void
  call  vm.builtin.null_value in:              dst: %686
  call  vm.builtin.null_value in:              dst: %688
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[956] dst: %690
  call  add3             in: %689, %690   dst: %void
  call  vm.builtin.null_value in:              dst: %689
  call  vm.builtin.alloc_tensor in: %320, i0, c[63], c[957] dst: %691
  call  take             in: %684, %690, %691 dst: %void
  call  vm.builtin.null_value in:              dst: %684
  call  vm.builtin.null_value in:              dst: %690
  call  vm.builtin.reshape in: %664, c[72]  dst: %692
  call  vm.builtin.alloc_tensor in: %346, i0, c[73], c[958] dst: %693
  call  einsum           in: %692, %680, %693 dst: %void
  call  vm.builtin.null_value in:              dst: %680
  call  vm.builtin.alloc_tensor in: %367, i0, c[73], c[959] dst: %694
  call  einsum1          in: %692, %691, %694 dst: %void
  call  vm.builtin.null_value in:              dst: %660
  call  vm.builtin.null_value in:              dst: %664
  call  vm.builtin.null_value in:              dst: %692
  call  vm.builtin.null_value in:              dst: %691
  call  vm.builtin.reshape in: %669, c[76]  dst: %695
  call  vm.builtin.reshape in: %693, c[77]  dst: %696
  call  vm.builtin.reshape in: %694, c[78]  dst: %697
  call  vm.builtin.alloc_tensor in: %351, i0, c[76], c[960] dst: %698
  call  add4             in: %695, %696, %698 dst: %void
  call  vm.builtin.null_value in:              dst: %669
  call  vm.builtin.null_value in:              dst: %695
  call  vm.builtin.null_value in:              dst: %693
  call  vm.builtin.null_value in:              dst: %696
  call  vm.builtin.alloc_tensor in: %340, i0, c[76], c[961] dst: %699
  call  add5             in: %698, %697, %699 dst: %void
  call  vm.builtin.null_value in:              dst: %698
  call  vm.builtin.null_value in:              dst: %694
  call  vm.builtin.null_value in:              dst: %697
  call  vm.builtin.reshape in: %699, c[43]  dst: %700
  call  vm.builtin.alloc_tensor in: %346, i0, c[43], c[962] dst: %701
  call  softmax          in: %700, %701   dst: %void
  call  vm.builtin.null_value in:              dst: %699
  call  vm.builtin.null_value in:              dst: %700
  call  vm.builtin.alloc_tensor in: %351, i0, c[38], c[963] dst: %702
  call  matmul2          in: %701, %666, %702 dst: %void
  call  vm.builtin.null_value in:              dst: %701
  call  vm.builtin.null_value in:              dst: %662
  call  vm.builtin.null_value in:              dst: %666
  call  vm.builtin.reshape in: %702, c[83]  dst: %703
  call  vm.builtin.alloc_tensor in: %340, i0, c[84], c[964] dst: %704
  call  transpose7       in: %703, %704   dst: %void
  call  vm.builtin.null_value in:              dst: %702
  call  vm.builtin.null_value in:              dst: %703
  call  vm.builtin.reshape in: %704, c[22]  dst: %705
  call  vm.builtin.alloc_tensor in: %338, i0, c[86], c[965] dst: %706
  call  transpose8       in: %66, %706    dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[22], c[966] dst: %707
  call  matmul3          in: %705, %706, %707 dst: %void
  call  vm.builtin.null_value in:              dst: %704
  call  vm.builtin.null_value in:              dst: %705
  call  vm.builtin.null_value in:              dst: %706
  call  vm.builtin.alloc_tensor in: %333, i0, c[22], c[967] dst: %708
  call  add6             in: %707, %67, %708 dst: %void
  call  vm.builtin.null_value in:              dst: %707
  call  vm.builtin.reshape in: %708, c[20]  dst: %709
  call  vm.builtin.alloc_tensor in: %351, i0, c[19], c[968] dst: %710
  call  transpose9       in: %709, %710   dst: %void
  call  vm.builtin.null_value in:              dst: %708
  call  vm.builtin.null_value in:              dst: %709
  call  vm.builtin.reshape in: %710, c[17]  dst: %711
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[969] dst: %712
  call  strided_slice    in: %711, %712   dst: %void
  call  vm.builtin.null_value in:              dst: %710
  call  vm.builtin.null_value in:              dst: %711
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[970] dst: %713
  call  add1             in: %648, %712, %713 dst: %void
  call  vm.builtin.null_value in:              dst: %648
  call  vm.builtin.null_value in:              dst: %712
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[971] dst: %714
  call  layer_norm       in: %713, %70, %71, %714 dst: %void
  call  vm.builtin.alloc_tensor in: %351, i0, c[94], c[972] dst: %715
  call  transpose10      in: %72, %715    dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[973] dst: %716
  call  matmul4          in: %714, %715, %716 dst: %void
  call  vm.builtin.null_value in:              dst: %714
  call  vm.builtin.null_value in:              dst: %715
  call  vm.builtin.alloc_tensor in: %425, i0, c[96], c[974] dst: %717
  call  add7             in: %716, %73, %717 dst: %void
  call  vm.builtin.null_value in:              dst: %716
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[975] dst: %718
  call  gelu             in: %717, %718   dst: %void
  call  vm.builtin.null_value in:              dst: %717
  call  vm.builtin.alloc_tensor in: %349, i0, c[100], c[976] dst: %719
  call  transpose11      in: %74, %719    dst: %void
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[977] dst: %720
  call  matmul5          in: %718, %719, %720 dst: %void
  call  vm.builtin.null_value in:              dst: %718
  call  vm.builtin.null_value in:              dst: %719
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[978] dst: %721
  call  add8             in: %720, %75, %721 dst: %void
  call  vm.builtin.null_value in:              dst: %720
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[979] dst: %722
  call  add1             in: %713, %721, %722 dst: %void
  call  vm.builtin.null_value in:              dst: %713
  call  vm.builtin.null_value in:              dst: %721
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[980] dst: %723
  call  layer_norm       in: %722, %76, %77, %723 dst: %void
  call  vm.builtin.alloc_tensor in: %340, i0, c[23], c[981] dst: %724
  call  transpose2       in: %78, %724    dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[152], c[982] dst: %725
  call  matmul6          in: %723, %724, %725 dst: %void
  call  vm.builtin.null_value in:              dst: %723
  call  vm.builtin.null_value in:              dst: %724
  call  vm.builtin.alloc_tensor in: %333, i0, c[152], c[983] dst: %726
  call  add9             in: %725, %79, %726 dst: %void
  call  vm.builtin.null_value in:              dst: %725
  call  vm.builtin.reshape in: %726, c[155] dst: %727
  call  vm.builtin.alloc_tensor in: %349, i0, c[156], c[984] dst: %728
  call  transpose12      in: %727, %728   dst: %void
  call  vm.builtin.null_value in:              dst: %726
  call  vm.builtin.null_value in:              dst: %727
  call  vm.builtin.reshape in: %728, c[158] dst: %729
  call  vm.builtin.alloc_tensor in: %340, i0, c[159], c[985] dst: %730
  call  vm.builtin.alloc_tensor in: %346, i0, c[159], c[986] dst: %731
  call  vm.builtin.alloc_tensor in: %333, i0, c[159], c[987] dst: %732
  call  split1           in: %729, %730, %731, %732 dst: %void
  call  vm.builtin.null_value in:              dst: %728
  call  vm.builtin.null_value in:              dst: %729
  call  vm.builtin.make_tuple in: %730, %731, %732 dst: %733
  call  vm.builtin.reshape in: %730, c[163] dst: %734
  call  vm.builtin.reshape in: %731, c[163] dst: %735
  call  vm.builtin.reshape in: %732, c[163] dst: %736
  call  vm.builtin.alloc_tensor in: %349, i0, c[163], c[988] dst: %737
  call  multiply3        in: %734, %737   dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[165], c[989] dst: %738
  call  transpose13      in: %735, %738   dst: %void
  call  vm.builtin.null_value in:              dst: %731
  call  vm.builtin.null_value in:              dst: %735
  call  vm.builtin.alloc_tensor in: %500, i0, c[168], c[990] dst: %739
  call  matmul7          in: %737, %738, %739 dst: %void
  call  vm.builtin.null_value in:              dst: %737
  call  vm.builtin.null_value in:              dst: %738
  call  vm.builtin.reshape in: %82, c[170]  dst: %740
  call  vm.builtin.alloc_tensor in: %318, i0, c[171], c[991] dst: %741
  call  transpose14      in: %740, %741   dst: %void
  call  vm.builtin.null_value in:              dst: %740
  call  vm.builtin.reshape in: %741, c[173] dst: %742
  call  vm.builtin.alloc_tensor in: %316, i0, c[174], c[992] dst: %743
  call  transpose15      in: %742, %743   dst: %void
  call  vm.builtin.null_value in:              dst: %741
  call  vm.builtin.null_value in:              dst: %742
  call  vm.builtin.reshape in: c[176], c[177] dst: %744
  call  vm.builtin.reshape in: %744, c[177] dst: %745
  call  vm.builtin.null_value in:              dst: %744
  call  vm.builtin.reshape in: c[176], c[178] dst: %746
  call  vm.builtin.reshape in: %746, c[178] dst: %747
  call  vm.builtin.null_value in:              dst: %746
  call  vm.builtin.alloc_tensor in: %532, i0, c[181], c[993] dst: %748
  call  subtract1        in: %745, %747, %748 dst: %void
  call  vm.builtin.null_value in:              dst: %745
  call  vm.builtin.null_value in:              dst: %747
  call  vm.builtin.alloc_tensor in: %534, i0, c[181], c[994] dst: %749
  call  add10            in: %748, %749   dst: %void
  call  vm.builtin.null_value in:              dst: %748
  call  vm.builtin.alloc_tensor in: %335, i0, c[186], c[995] dst: %750
  call  take1            in: %743, %749, %750 dst: %void
  call  vm.builtin.null_value in:              dst: %743
  call  vm.builtin.null_value in:              dst: %749
  call  vm.builtin.reshape in: %83, c[170]  dst: %751
  call  vm.builtin.alloc_tensor in: %320, i0, c[171], c[996] dst: %752
  call  transpose14      in: %751, %752   dst: %void
  call  vm.builtin.null_value in:              dst: %751
  call  vm.builtin.reshape in: %752, c[173] dst: %753
  call  vm.builtin.alloc_tensor in: %318, i0, c[174], c[997] dst: %754
  call  transpose15      in: %753, %754   dst: %void
  call  vm.builtin.null_value in:              dst: %752
  call  vm.builtin.null_value in:              dst: %753
  call  vm.builtin.reshape in: c[176], c[177] dst: %755
  call  vm.builtin.reshape in: %755, c[177] dst: %756
  call  vm.builtin.null_value in:              dst: %755
  call  vm.builtin.reshape in: c[176], c[178] dst: %757
  call  vm.builtin.reshape in: %757, c[178] dst: %758
  call  vm.builtin.null_value in:              dst: %757
  call  vm.builtin.alloc_tensor in: %532, i0, c[181], c[998] dst: %759
  call  subtract1        in: %756, %758, %759 dst: %void
  call  vm.builtin.null_value in:              dst: %756
  call  vm.builtin.null_value in:              dst: %758
  call  vm.builtin.alloc_tensor in: %534, i0, c[181], c[999] dst: %760
  call  add10            in: %759, %760   dst: %void
  call  vm.builtin.null_value in:              dst: %759
  call  vm.builtin.alloc_tensor in: %338, i0, c[186], c[1000] dst: %761
  call  take1            in: %754, %760, %761 dst: %void
  call  vm.builtin.null_value in:              dst: %754
  call  vm.builtin.null_value in:              dst: %760
  call  vm.builtin.reshape in: %734, c[194] dst: %762
  call  vm.builtin.alloc_tensor in: %346, i0, c[194], c[1001] dst: %763
  call  einsum2          in: %762, %750, %763 dst: %void
  call  vm.builtin.null_value in:              dst: %750
  call  vm.builtin.alloc_tensor in: %349, i0, c[194], c[1002] dst: %764
  call  einsum3          in: %762, %761, %764 dst: %void
  call  vm.builtin.null_value in:              dst: %730
  call  vm.builtin.null_value in:              dst: %734
  call  vm.builtin.null_value in:              dst: %762
  call  vm.builtin.null_value in:              dst: %761
  call  vm.builtin.reshape in: %739, c[197] dst: %765
  call  vm.builtin.reshape in: %763, c[198] dst: %766
  call  vm.builtin.reshape in: %764, c[199] dst: %767
  call  vm.builtin.alloc_tensor in: %425, i0, c[197], c[1003] dst: %768
  call  add11            in: %765, %766, %768 dst: %void
  call  vm.builtin.null_value in:              dst: %739
  call  vm.builtin.null_value in:              dst: %765
  call  vm.builtin.null_value in:              dst: %763
  call  vm.builtin.null_value in:              dst: %766
  call  vm.builtin.alloc_tensor in: %500, i0, c[197], c[1004] dst: %769
  call  add12            in: %768, %767, %769 dst: %void
  call  vm.builtin.null_value in:              dst: %768
  call  vm.builtin.null_value in:              dst: %764
  call  vm.builtin.null_value in:              dst: %767
  call  vm.builtin.reshape in: %769, c[168] dst: %770
  call  vm.builtin.alloc_tensor in: %425, i0, c[168], c[1005] dst: %771
  call  softmax1         in: %770, %771   dst: %void
  call  vm.builtin.null_value in:              dst: %769
  call  vm.builtin.null_value in:              dst: %770
  call  vm.builtin.alloc_tensor in: %340, i0, c[163], c[1006] dst: %772
  call  matmul8          in: %771, %736, %772 dst: %void
  call  vm.builtin.null_value in:              dst: %771
  call  vm.builtin.null_value in:              dst: %732
  call  vm.builtin.null_value in:              dst: %736
  call  vm.builtin.reshape in: %772, c[204] dst: %773
  call  vm.builtin.alloc_tensor in: %346, i0, c[205], c[1007] dst: %774
  call  transpose16      in: %773, %774   dst: %void
  call  vm.builtin.null_value in:              dst: %772
  call  vm.builtin.null_value in:              dst: %773
  call  vm.builtin.reshape in: %774, c[11]  dst: %775
  call  vm.builtin.alloc_tensor in: %338, i0, c[86], c[1008] dst: %776
  call  transpose8       in: %80, %776    dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[1009] dst: %777
  call  matmul9          in: %775, %776, %777 dst: %void
  call  vm.builtin.null_value in:              dst: %774
  call  vm.builtin.null_value in:              dst: %775
  call  vm.builtin.null_value in:              dst: %776
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[1010] dst: %778
  call  add8             in: %777, %81, %778 dst: %void
  call  vm.builtin.null_value in:              dst: %777
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[1011] dst: %779
  call  add1             in: %722, %778, %779 dst: %void
  call  vm.builtin.null_value in:              dst: %722
  call  vm.builtin.null_value in:              dst: %778
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[1012] dst: %780
  call  layer_norm       in: %779, %84, %85, %780 dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[94], c[1013] dst: %781
  call  transpose10      in: %86, %781    dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1014] dst: %782
  call  matmul4          in: %780, %781, %782 dst: %void
  call  vm.builtin.null_value in:              dst: %780
  call  vm.builtin.null_value in:              dst: %781
  call  vm.builtin.alloc_tensor in: %500, i0, c[96], c[1015] dst: %783
  call  add7             in: %782, %87, %783 dst: %void
  call  vm.builtin.null_value in:              dst: %782
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1016] dst: %784
  call  gelu             in: %783, %784   dst: %void
  call  vm.builtin.null_value in:              dst: %783
  call  vm.builtin.alloc_tensor in: %351, i0, c[100], c[1017] dst: %785
  call  transpose11      in: %88, %785    dst: %void
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[1018] dst: %786
  call  matmul5          in: %784, %785, %786 dst: %void
  call  vm.builtin.null_value in:              dst: %784
  call  vm.builtin.null_value in:              dst: %785
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[1019] dst: %787
  call  add8             in: %786, %89, %787 dst: %void
  call  vm.builtin.null_value in:              dst: %786
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[1020] dst: %788
  call  add1             in: %779, %787, %788 dst: %void
  call  vm.builtin.null_value in:              dst: %779
  call  vm.builtin.null_value in:              dst: %787
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[1021] dst: %789
  call  layer_norm       in: %788, %90, %91, %789 dst: %void
  call  vm.builtin.alloc_tensor in: %333, i0, c[17], c[1022] dst: %790
  call  pad              in: %789, %790   dst: %void
  call  vm.builtin.null_value in:              dst: %789
  call  vm.builtin.reshape in: %790, c[19]  dst: %791
  call  vm.builtin.alloc_tensor in: %340, i0, c[20], c[1023] dst: %792
  call  transpose1       in: %791, %792   dst: %void
  call  vm.builtin.null_value in:              dst: %790
  call  vm.builtin.null_value in:              dst: %791
  call  vm.builtin.reshape in: %792, c[22]  dst: %793
  call  vm.builtin.alloc_tensor in: %346, i0, c[23], c[1024] dst: %794
  call  transpose2       in: %92, %794    dst: %void
  call  vm.builtin.alloc_tensor in: %351, i0, c[26], c[1025] dst: %795
  call  matmul           in: %793, %794, %795 dst: %void
  call  vm.builtin.null_value in:              dst: %792
  call  vm.builtin.null_value in:              dst: %793
  call  vm.builtin.null_value in:              dst: %794
  call  vm.builtin.alloc_tensor in: %333, i0, c[26], c[1026] dst: %796
  call  add2             in: %795, %93, %796 dst: %void
  call  vm.builtin.null_value in:              dst: %795
  call  vm.builtin.reshape in: %796, c[29]  dst: %797
  call  vm.builtin.alloc_tensor in: %340, i0, c[30], c[1027] dst: %798
  call  transpose3       in: %797, %798   dst: %void
  call  vm.builtin.null_value in:              dst: %796
  call  vm.builtin.null_value in:              dst: %797
  call  vm.builtin.reshape in: %798, c[32]  dst: %799
  call  vm.builtin.alloc_tensor in: %346, i0, c[33], c[1028] dst: %800
  call  vm.builtin.alloc_tensor in: %351, i0, c[33], c[1029] dst: %801
  call  vm.builtin.alloc_tensor in: %333, i0, c[33], c[1030] dst: %802
  call  split            in: %799, %800, %801, %802 dst: %void
  call  vm.builtin.null_value in:              dst: %798
  call  vm.builtin.null_value in:              dst: %799
  call  vm.builtin.make_tuple in: %800, %801, %802 dst: %803
  call  vm.builtin.reshape in: %800, c[38]  dst: %804
  call  vm.builtin.reshape in: %801, c[38]  dst: %805
  call  vm.builtin.reshape in: %802, c[38]  dst: %806
  call  vm.builtin.alloc_tensor in: %340, i0, c[38], c[1031] dst: %807
  call  multiply         in: %804, %807   dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[41], c[1032] dst: %808
  call  transpose4       in: %805, %808   dst: %void
  call  vm.builtin.null_value in:              dst: %801
  call  vm.builtin.null_value in:              dst: %805
  call  vm.builtin.alloc_tensor in: %351, i0, c[43], c[1033] dst: %809
  call  matmul1          in: %807, %808, %809 dst: %void
  call  vm.builtin.null_value in:              dst: %807
  call  vm.builtin.null_value in:              dst: %808
  call  vm.builtin.reshape in: %96, c[45]   dst: %810
  call  vm.builtin.alloc_tensor in: %316, i0, c[48], c[1034] dst: %811
  call  transpose5       in: %810, %811   dst: %void
  call  vm.builtin.null_value in:              dst: %810
  call  vm.builtin.reshape in: %811, c[50]  dst: %812
  call  vm.builtin.alloc_tensor in: %320, i0, c[52], c[1035] dst: %813
  call  transpose6       in: %812, %813   dst: %void
  call  vm.builtin.null_value in:              dst: %811
  call  vm.builtin.null_value in:              dst: %812
  call  vm.builtin.reshape in: c[54], c[55] dst: %814
  call  vm.builtin.reshape in: %814, c[55]  dst: %815
  call  vm.builtin.null_value in:              dst: %814
  call  vm.builtin.reshape in: c[54], c[56] dst: %816
  call  vm.builtin.reshape in: %816, c[56]  dst: %817
  call  vm.builtin.null_value in:              dst: %816
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[1036] dst: %818
  call  subtract         in: %815, %817, %818 dst: %void
  call  vm.builtin.null_value in:              dst: %815
  call  vm.builtin.null_value in:              dst: %817
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[1037] dst: %819
  call  add3             in: %818, %819   dst: %void
  call  vm.builtin.null_value in:              dst: %818
  call  vm.builtin.alloc_tensor in: %318, i0, c[63], c[1038] dst: %820
  call  take             in: %813, %819, %820 dst: %void
  call  vm.builtin.null_value in:              dst: %813
  call  vm.builtin.null_value in:              dst: %819
  call  vm.builtin.reshape in: %97, c[45]   dst: %821
  call  vm.builtin.alloc_tensor in: %316, i0, c[48], c[1039] dst: %822
  call  transpose5       in: %821, %822   dst: %void
  call  vm.builtin.null_value in:              dst: %821
  call  vm.builtin.reshape in: %822, c[50]  dst: %823
  call  vm.builtin.alloc_tensor in: %320, i0, c[52], c[1040] dst: %824
  call  transpose6       in: %823, %824   dst: %void
  call  vm.builtin.null_value in:              dst: %822
  call  vm.builtin.null_value in:              dst: %823
  call  vm.builtin.reshape in: c[54], c[55] dst: %825
  call  vm.builtin.reshape in: %825, c[55]  dst: %826
  call  vm.builtin.null_value in:              dst: %825
  call  vm.builtin.reshape in: c[54], c[56] dst: %827
  call  vm.builtin.reshape in: %827, c[56]  dst: %828
  call  vm.builtin.null_value in:              dst: %827
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[1041] dst: %829
  call  subtract         in: %826, %828, %829 dst: %void
  call  vm.builtin.null_value in:              dst: %826
  call  vm.builtin.null_value in:              dst: %828
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[1042] dst: %830
  call  add3             in: %829, %830   dst: %void
  call  vm.builtin.null_value in:              dst: %829
  call  vm.builtin.alloc_tensor in: %316, i0, c[63], c[1043] dst: %831
  call  take             in: %824, %830, %831 dst: %void
  call  vm.builtin.null_value in:              dst: %824
  call  vm.builtin.null_value in:              dst: %830
  call  vm.builtin.reshape in: %804, c[72]  dst: %832
  call  vm.builtin.alloc_tensor in: %340, i0, c[73], c[1044] dst: %833
  call  einsum           in: %832, %820, %833 dst: %void
  call  vm.builtin.null_value in:              dst: %820
  call  vm.builtin.alloc_tensor in: %367, i0, c[73], c[1045] dst: %834
  call  einsum1          in: %832, %831, %834 dst: %void
  call  vm.builtin.null_value in:              dst: %800
  call  vm.builtin.null_value in:              dst: %804
  call  vm.builtin.null_value in:              dst: %832
  call  vm.builtin.null_value in:              dst: %831
  call  vm.builtin.reshape in: %809, c[76]  dst: %835
  call  vm.builtin.reshape in: %833, c[77]  dst: %836
  call  vm.builtin.reshape in: %834, c[78]  dst: %837
  call  vm.builtin.alloc_tensor in: %346, i0, c[76], c[1046] dst: %838
  call  add4             in: %835, %836, %838 dst: %void
  call  vm.builtin.null_value in:              dst: %809
  call  vm.builtin.null_value in:              dst: %835
  call  vm.builtin.null_value in:              dst: %833
  call  vm.builtin.null_value in:              dst: %836
  call  vm.builtin.alloc_tensor in: %351, i0, c[76], c[1047] dst: %839
  call  add5             in: %838, %837, %839 dst: %void
  call  vm.builtin.null_value in:              dst: %838
  call  vm.builtin.null_value in:              dst: %834
  call  vm.builtin.null_value in:              dst: %837
  call  vm.builtin.reshape in: %839, c[43]  dst: %840
  call  vm.builtin.alloc_tensor in: %340, i0, c[43], c[1048] dst: %841
  call  softmax          in: %840, %841   dst: %void
  call  vm.builtin.null_value in:              dst: %839
  call  vm.builtin.null_value in:              dst: %840
  call  vm.builtin.alloc_tensor in: %346, i0, c[38], c[1049] dst: %842
  call  matmul2          in: %841, %806, %842 dst: %void
  call  vm.builtin.null_value in:              dst: %841
  call  vm.builtin.null_value in:              dst: %802
  call  vm.builtin.null_value in:              dst: %806
  call  vm.builtin.reshape in: %842, c[83]  dst: %843
  call  vm.builtin.alloc_tensor in: %351, i0, c[84], c[1050] dst: %844
  call  transpose7       in: %843, %844   dst: %void
  call  vm.builtin.null_value in:              dst: %842
  call  vm.builtin.null_value in:              dst: %843
  call  vm.builtin.reshape in: %844, c[22]  dst: %845
  call  vm.builtin.alloc_tensor in: %338, i0, c[86], c[1051] dst: %846
  call  transpose8       in: %94, %846    dst: %void
  call  vm.builtin.alloc_tensor in: %340, i0, c[22], c[1052] dst: %847
  call  matmul3          in: %845, %846, %847 dst: %void
  call  vm.builtin.null_value in:              dst: %844
  call  vm.builtin.null_value in:              dst: %845
  call  vm.builtin.null_value in:              dst: %846
  call  vm.builtin.alloc_tensor in: %333, i0, c[22], c[1053] dst: %848
  call  add6             in: %847, %95, %848 dst: %void
  call  vm.builtin.null_value in:              dst: %847
  call  vm.builtin.reshape in: %848, c[20]  dst: %849
  call  vm.builtin.alloc_tensor in: %346, i0, c[19], c[1054] dst: %850
  call  transpose9       in: %849, %850   dst: %void
  call  vm.builtin.null_value in:              dst: %848
  call  vm.builtin.null_value in:              dst: %849
  call  vm.builtin.reshape in: %850, c[17]  dst: %851
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[1055] dst: %852
  call  strided_slice    in: %851, %852   dst: %void
  call  vm.builtin.null_value in:              dst: %850
  call  vm.builtin.null_value in:              dst: %851
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[1056] dst: %853
  call  add1             in: %788, %852, %853 dst: %void
  call  vm.builtin.null_value in:              dst: %788
  call  vm.builtin.null_value in:              dst: %852
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[1057] dst: %854
  call  layer_norm       in: %853, %98, %99, %854 dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[94], c[1058] dst: %855
  call  transpose10      in: %100, %855   dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1059] dst: %856
  call  matmul4          in: %854, %855, %856 dst: %void
  call  vm.builtin.null_value in:              dst: %854
  call  vm.builtin.null_value in:              dst: %855
  call  vm.builtin.alloc_tensor in: %425, i0, c[96], c[1060] dst: %857
  call  add7             in: %856, %101, %857 dst: %void
  call  vm.builtin.null_value in:              dst: %856
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1061] dst: %858
  call  gelu             in: %857, %858   dst: %void
  call  vm.builtin.null_value in:              dst: %857
  call  vm.builtin.alloc_tensor in: %349, i0, c[100], c[1062] dst: %859
  call  transpose11      in: %102, %859   dst: %void
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[1063] dst: %860
  call  matmul5          in: %858, %859, %860 dst: %void
  call  vm.builtin.null_value in:              dst: %858
  call  vm.builtin.null_value in:              dst: %859
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[1064] dst: %861
  call  add8             in: %860, %103, %861 dst: %void
  call  vm.builtin.null_value in:              dst: %860
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[1065] dst: %862
  call  add1             in: %853, %861, %862 dst: %void
  call  vm.builtin.null_value in:              dst: %853
  call  vm.builtin.null_value in:              dst: %861
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[1066] dst: %863
  call  layer_norm       in: %862, %104, %105, %863 dst: %void
  call  vm.builtin.alloc_tensor in: %351, i0, c[17], c[1067] dst: %864
  call  pad              in: %863, %864   dst: %void
  call  vm.builtin.null_value in:              dst: %863
  call  vm.builtin.reshape in: %864, c[19]  dst: %865
  call  vm.builtin.alloc_tensor in: %340, i0, c[20], c[1068] dst: %866
  call  transpose1       in: %865, %866   dst: %void
  call  vm.builtin.null_value in:              dst: %864
  call  vm.builtin.null_value in:              dst: %865
  call  vm.builtin.reshape in: %866, c[22]  dst: %867
  call  vm.builtin.alloc_tensor in: %333, i0, c[23], c[1069] dst: %868
  call  transpose2       in: %106, %868   dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[26], c[1070] dst: %869
  call  matmul           in: %867, %868, %869 dst: %void
  call  vm.builtin.null_value in:              dst: %866
  call  vm.builtin.null_value in:              dst: %867
  call  vm.builtin.null_value in:              dst: %868
  call  vm.builtin.alloc_tensor in: %351, i0, c[26], c[1071] dst: %870
  call  add2             in: %869, %107, %870 dst: %void
  call  vm.builtin.null_value in:              dst: %869
  call  vm.builtin.reshape in: %870, c[29]  dst: %871
  call  vm.builtin.alloc_tensor in: %340, i0, c[30], c[1072] dst: %872
  call  transpose3       in: %871, %872   dst: %void
  call  vm.builtin.null_value in:              dst: %870
  call  vm.builtin.null_value in:              dst: %871
  call  vm.builtin.reshape in: %872, c[32]  dst: %873
  call  vm.builtin.alloc_tensor in: %333, i0, c[33], c[1073] dst: %874
  call  vm.builtin.alloc_tensor in: %349, i0, c[33], c[1074] dst: %875
  call  vm.builtin.alloc_tensor in: %351, i0, c[33], c[1075] dst: %876
  call  split            in: %873, %874, %875, %876 dst: %void
  call  vm.builtin.null_value in:              dst: %872
  call  vm.builtin.null_value in:              dst: %873
  call  vm.builtin.make_tuple in: %874, %875, %876 dst: %877
  call  vm.builtin.reshape in: %874, c[38]  dst: %878
  call  vm.builtin.reshape in: %875, c[38]  dst: %879
  call  vm.builtin.reshape in: %876, c[38]  dst: %880
  call  vm.builtin.alloc_tensor in: %340, i0, c[38], c[1076] dst: %881
  call  multiply         in: %878, %881   dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[41], c[1077] dst: %882
  call  transpose4       in: %879, %882   dst: %void
  call  vm.builtin.null_value in:              dst: %875
  call  vm.builtin.null_value in:              dst: %879
  call  vm.builtin.alloc_tensor in: %349, i0, c[43], c[1078] dst: %883
  call  matmul1          in: %881, %882, %883 dst: %void
  call  vm.builtin.null_value in:              dst: %881
  call  vm.builtin.null_value in:              dst: %882
  call  vm.builtin.reshape in: %110, c[45]  dst: %884
  call  vm.builtin.alloc_tensor in: %320, i0, c[48], c[1079] dst: %885
  call  transpose5       in: %884, %885   dst: %void
  call  vm.builtin.null_value in:              dst: %884
  call  vm.builtin.reshape in: %885, c[50]  dst: %886
  call  vm.builtin.alloc_tensor in: %318, i0, c[52], c[1080] dst: %887
  call  transpose6       in: %886, %887   dst: %void
  call  vm.builtin.null_value in:              dst: %885
  call  vm.builtin.null_value in:              dst: %886
  call  vm.builtin.reshape in: c[54], c[55] dst: %888
  call  vm.builtin.reshape in: %888, c[55]  dst: %889
  call  vm.builtin.null_value in:              dst: %888
  call  vm.builtin.reshape in: c[54], c[56] dst: %890
  call  vm.builtin.reshape in: %890, c[56]  dst: %891
  call  vm.builtin.null_value in:              dst: %890
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[1081] dst: %892
  call  subtract         in: %889, %891, %892 dst: %void
  call  vm.builtin.null_value in:              dst: %889
  call  vm.builtin.null_value in:              dst: %891
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[1082] dst: %893
  call  add3             in: %892, %893   dst: %void
  call  vm.builtin.null_value in:              dst: %892
  call  vm.builtin.alloc_tensor in: %316, i0, c[63], c[1083] dst: %894
  call  take             in: %887, %893, %894 dst: %void
  call  vm.builtin.null_value in:              dst: %887
  call  vm.builtin.null_value in:              dst: %893
  call  vm.builtin.reshape in: %111, c[45]  dst: %895
  call  vm.builtin.alloc_tensor in: %320, i0, c[48], c[1084] dst: %896
  call  transpose5       in: %895, %896   dst: %void
  call  vm.builtin.null_value in:              dst: %895
  call  vm.builtin.reshape in: %896, c[50]  dst: %897
  call  vm.builtin.alloc_tensor in: %318, i0, c[52], c[1085] dst: %898
  call  transpose6       in: %897, %898   dst: %void
  call  vm.builtin.null_value in:              dst: %896
  call  vm.builtin.null_value in:              dst: %897
  call  vm.builtin.reshape in: c[54], c[55] dst: %899
  call  vm.builtin.reshape in: %899, c[55]  dst: %900
  call  vm.builtin.null_value in:              dst: %899
  call  vm.builtin.reshape in: c[54], c[56] dst: %901
  call  vm.builtin.reshape in: %901, c[56]  dst: %902
  call  vm.builtin.null_value in:              dst: %901
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[1086] dst: %903
  call  subtract         in: %900, %902, %903 dst: %void
  call  vm.builtin.null_value in:              dst: %900
  call  vm.builtin.null_value in:              dst: %902
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[1087] dst: %904
  call  add3             in: %903, %904   dst: %void
  call  vm.builtin.null_value in:              dst: %903
  call  vm.builtin.alloc_tensor in: %320, i0, c[63], c[1088] dst: %905
  call  take             in: %898, %904, %905 dst: %void
  call  vm.builtin.null_value in:              dst: %898
  call  vm.builtin.null_value in:              dst: %904
  call  vm.builtin.reshape in: %878, c[72]  dst: %906
  call  vm.builtin.alloc_tensor in: %340, i0, c[73], c[1089] dst: %907
  call  einsum           in: %906, %894, %907 dst: %void
  call  vm.builtin.null_value in:              dst: %894
  call  vm.builtin.alloc_tensor in: %367, i0, c[73], c[1090] dst: %908
  call  einsum1          in: %906, %905, %908 dst: %void
  call  vm.builtin.null_value in:              dst: %874
  call  vm.builtin.null_value in:              dst: %878
  call  vm.builtin.null_value in:              dst: %906
  call  vm.builtin.null_value in:              dst: %905
  call  vm.builtin.reshape in: %883, c[76]  dst: %909
  call  vm.builtin.reshape in: %907, c[77]  dst: %910
  call  vm.builtin.reshape in: %908, c[78]  dst: %911
  call  vm.builtin.alloc_tensor in: %333, i0, c[76], c[1091] dst: %912
  call  add4             in: %909, %910, %912 dst: %void
  call  vm.builtin.null_value in:              dst: %883
  call  vm.builtin.null_value in:              dst: %909
  call  vm.builtin.null_value in:              dst: %907
  call  vm.builtin.null_value in:              dst: %910
  call  vm.builtin.alloc_tensor in: %349, i0, c[76], c[1092] dst: %913
  call  add5             in: %912, %911, %913 dst: %void
  call  vm.builtin.null_value in:              dst: %912
  call  vm.builtin.null_value in:              dst: %908
  call  vm.builtin.null_value in:              dst: %911
  call  vm.builtin.reshape in: %913, c[43]  dst: %914
  call  vm.builtin.alloc_tensor in: %340, i0, c[43], c[1093] dst: %915
  call  softmax          in: %914, %915   dst: %void
  call  vm.builtin.null_value in:              dst: %913
  call  vm.builtin.null_value in:              dst: %914
  call  vm.builtin.alloc_tensor in: %333, i0, c[38], c[1094] dst: %916
  call  matmul2          in: %915, %880, %916 dst: %void
  call  vm.builtin.null_value in:              dst: %915
  call  vm.builtin.null_value in:              dst: %876
  call  vm.builtin.null_value in:              dst: %880
  call  vm.builtin.reshape in: %916, c[83]  dst: %917
  call  vm.builtin.alloc_tensor in: %349, i0, c[84], c[1095] dst: %918
  call  transpose7       in: %917, %918   dst: %void
  call  vm.builtin.null_value in:              dst: %916
  call  vm.builtin.null_value in:              dst: %917
  call  vm.builtin.reshape in: %918, c[22]  dst: %919
  call  vm.builtin.alloc_tensor in: %338, i0, c[86], c[1096] dst: %920
  call  transpose8       in: %108, %920   dst: %void
  call  vm.builtin.alloc_tensor in: %340, i0, c[22], c[1097] dst: %921
  call  matmul3          in: %919, %920, %921 dst: %void
  call  vm.builtin.null_value in:              dst: %918
  call  vm.builtin.null_value in:              dst: %919
  call  vm.builtin.null_value in:              dst: %920
  call  vm.builtin.alloc_tensor in: %351, i0, c[22], c[1098] dst: %922
  call  add6             in: %921, %109, %922 dst: %void
  call  vm.builtin.null_value in:              dst: %921
  call  vm.builtin.reshape in: %922, c[20]  dst: %923
  call  vm.builtin.alloc_tensor in: %333, i0, c[19], c[1099] dst: %924
  call  transpose9       in: %923, %924   dst: %void
  call  vm.builtin.null_value in:              dst: %922
  call  vm.builtin.null_value in:              dst: %923
  call  vm.builtin.reshape in: %924, c[17]  dst: %925
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[1100] dst: %926
  call  strided_slice    in: %925, %926   dst: %void
  call  vm.builtin.null_value in:              dst: %924
  call  vm.builtin.null_value in:              dst: %925
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[1101] dst: %927
  call  add1             in: %862, %926, %927 dst: %void
  call  vm.builtin.null_value in:              dst: %862
  call  vm.builtin.null_value in:              dst: %926
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[1102] dst: %928
  call  layer_norm       in: %927, %112, %113, %928 dst: %void
  call  vm.builtin.alloc_tensor in: %333, i0, c[94], c[1103] dst: %929
  call  transpose10      in: %114, %929   dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1104] dst: %930
  call  matmul4          in: %928, %929, %930 dst: %void
  call  vm.builtin.null_value in:              dst: %928
  call  vm.builtin.null_value in:              dst: %929
  call  vm.builtin.alloc_tensor in: %500, i0, c[96], c[1105] dst: %931
  call  add7             in: %930, %115, %931 dst: %void
  call  vm.builtin.null_value in:              dst: %930
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1106] dst: %932
  call  gelu             in: %931, %932   dst: %void
  call  vm.builtin.null_value in:              dst: %931
  call  vm.builtin.alloc_tensor in: %346, i0, c[100], c[1107] dst: %933
  call  transpose11      in: %116, %933   dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[1108] dst: %934
  call  matmul5          in: %932, %933, %934 dst: %void
  call  vm.builtin.null_value in:              dst: %932
  call  vm.builtin.null_value in:              dst: %933
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[1109] dst: %935
  call  add8             in: %934, %117, %935 dst: %void
  call  vm.builtin.null_value in:              dst: %934
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[1110] dst: %936
  call  add1             in: %927, %935, %936 dst: %void
  call  vm.builtin.null_value in:              dst: %927
  call  vm.builtin.null_value in:              dst: %935
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[1111] dst: %937
  call  layer_norm       in: %936, %118, %119, %937 dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[23], c[1112] dst: %938
  call  transpose2       in: %120, %938   dst: %void
  call  vm.builtin.alloc_tensor in: %340, i0, c[152], c[1113] dst: %939
  call  matmul6          in: %937, %938, %939 dst: %void
  call  vm.builtin.null_value in:              dst: %937
  call  vm.builtin.null_value in:              dst: %938
  call  vm.builtin.alloc_tensor in: %351, i0, c[152], c[1114] dst: %940
  call  add9             in: %939, %121, %940 dst: %void
  call  vm.builtin.null_value in:              dst: %939
  call  vm.builtin.reshape in: %940, c[155] dst: %941
  call  vm.builtin.alloc_tensor in: %346, i0, c[156], c[1115] dst: %942
  call  transpose12      in: %941, %942   dst: %void
  call  vm.builtin.null_value in:              dst: %940
  call  vm.builtin.null_value in:              dst: %941
  call  vm.builtin.reshape in: %942, c[158] dst: %943
  call  vm.builtin.alloc_tensor in: %349, i0, c[159], c[1116] dst: %944
  call  vm.builtin.alloc_tensor in: %340, i0, c[159], c[1117] dst: %945
  call  vm.builtin.alloc_tensor in: %351, i0, c[159], c[1118] dst: %946
  call  split1           in: %943, %944, %945, %946 dst: %void
  call  vm.builtin.null_value in:              dst: %942
  call  vm.builtin.null_value in:              dst: %943
  call  vm.builtin.make_tuple in: %944, %945, %946 dst: %947
  call  vm.builtin.reshape in: %944, c[163] dst: %948
  call  vm.builtin.reshape in: %945, c[163] dst: %949
  call  vm.builtin.reshape in: %946, c[163] dst: %950
  call  vm.builtin.alloc_tensor in: %346, i0, c[163], c[1119] dst: %951
  call  multiply3        in: %948, %951   dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[165], c[1120] dst: %952
  call  transpose13      in: %949, %952   dst: %void
  call  vm.builtin.null_value in:              dst: %945
  call  vm.builtin.null_value in:              dst: %949
  call  vm.builtin.alloc_tensor in: %425, i0, c[168], c[1121] dst: %953
  call  matmul7          in: %951, %952, %953 dst: %void
  call  vm.builtin.null_value in:              dst: %951
  call  vm.builtin.null_value in:              dst: %952
  call  vm.builtin.reshape in: %124, c[170] dst: %954
  call  vm.builtin.alloc_tensor in: %318, i0, c[171], c[1122] dst: %955
  call  transpose14      in: %954, %955   dst: %void
  call  vm.builtin.null_value in:              dst: %954
  call  vm.builtin.reshape in: %955, c[173] dst: %956
  call  vm.builtin.alloc_tensor in: %316, i0, c[174], c[1123] dst: %957
  call  transpose15      in: %956, %957   dst: %void
  call  vm.builtin.null_value in:              dst: %955
  call  vm.builtin.null_value in:              dst: %956
  call  vm.builtin.reshape in: c[176], c[177] dst: %958
  call  vm.builtin.reshape in: %958, c[177] dst: %959
  call  vm.builtin.null_value in:              dst: %958
  call  vm.builtin.reshape in: c[176], c[178] dst: %960
  call  vm.builtin.reshape in: %960, c[178] dst: %961
  call  vm.builtin.null_value in:              dst: %960
  call  vm.builtin.alloc_tensor in: %532, i0, c[181], c[1124] dst: %962
  call  subtract1        in: %959, %961, %962 dst: %void
  call  vm.builtin.null_value in:              dst: %959
  call  vm.builtin.null_value in:              dst: %961
  call  vm.builtin.alloc_tensor in: %534, i0, c[181], c[1125] dst: %963
  call  add10            in: %962, %963   dst: %void
  call  vm.builtin.null_value in:              dst: %962
  call  vm.builtin.alloc_tensor in: %335, i0, c[186], c[1126] dst: %964
  call  take1            in: %957, %963, %964 dst: %void
  call  vm.builtin.null_value in:              dst: %957
  call  vm.builtin.null_value in:              dst: %963
  call  vm.builtin.reshape in: %125, c[170] dst: %965
  call  vm.builtin.alloc_tensor in: %320, i0, c[171], c[1127] dst: %966
  call  transpose14      in: %965, %966   dst: %void
  call  vm.builtin.null_value in:              dst: %965
  call  vm.builtin.reshape in: %966, c[173] dst: %967
  call  vm.builtin.alloc_tensor in: %318, i0, c[174], c[1128] dst: %968
  call  transpose15      in: %967, %968   dst: %void
  call  vm.builtin.null_value in:              dst: %966
  call  vm.builtin.null_value in:              dst: %967
  call  vm.builtin.reshape in: c[176], c[177] dst: %969
  call  vm.builtin.reshape in: %969, c[177] dst: %970
  call  vm.builtin.null_value in:              dst: %969
  call  vm.builtin.reshape in: c[176], c[178] dst: %971
  call  vm.builtin.reshape in: %971, c[178] dst: %972
  call  vm.builtin.null_value in:              dst: %971
  call  vm.builtin.alloc_tensor in: %532, i0, c[181], c[1129] dst: %973
  call  subtract1        in: %970, %972, %973 dst: %void
  call  vm.builtin.null_value in:              dst: %970
  call  vm.builtin.null_value in:              dst: %972
  call  vm.builtin.alloc_tensor in: %534, i0, c[181], c[1130] dst: %974
  call  add10            in: %973, %974   dst: %void
  call  vm.builtin.null_value in:              dst: %973
  call  vm.builtin.alloc_tensor in: %338, i0, c[186], c[1131] dst: %975
  call  take1            in: %968, %974, %975 dst: %void
  call  vm.builtin.null_value in:              dst: %968
  call  vm.builtin.null_value in:              dst: %974
  call  vm.builtin.reshape in: %948, c[194] dst: %976
  call  vm.builtin.alloc_tensor in: %340, i0, c[194], c[1132] dst: %977
  call  einsum2          in: %976, %964, %977 dst: %void
  call  vm.builtin.null_value in:              dst: %964
  call  vm.builtin.alloc_tensor in: %346, i0, c[194], c[1133] dst: %978
  call  einsum3          in: %976, %975, %978 dst: %void
  call  vm.builtin.null_value in:              dst: %944
  call  vm.builtin.null_value in:              dst: %948
  call  vm.builtin.null_value in:              dst: %976
  call  vm.builtin.null_value in:              dst: %975
  call  vm.builtin.reshape in: %953, c[197] dst: %979
  call  vm.builtin.reshape in: %977, c[198] dst: %980
  call  vm.builtin.reshape in: %978, c[199] dst: %981
  call  vm.builtin.alloc_tensor in: %500, i0, c[197], c[1134] dst: %982
  call  add11            in: %979, %980, %982 dst: %void
  call  vm.builtin.null_value in:              dst: %953
  call  vm.builtin.null_value in:              dst: %979
  call  vm.builtin.null_value in:              dst: %977
  call  vm.builtin.null_value in:              dst: %980
  call  vm.builtin.alloc_tensor in: %425, i0, c[197], c[1135] dst: %983
  call  add12            in: %982, %981, %983 dst: %void
  call  vm.builtin.null_value in:              dst: %982
  call  vm.builtin.null_value in:              dst: %978
  call  vm.builtin.null_value in:              dst: %981
  call  vm.builtin.reshape in: %983, c[168] dst: %984
  call  vm.builtin.alloc_tensor in: %500, i0, c[168], c[1136] dst: %985
  call  softmax1         in: %984, %985   dst: %void
  call  vm.builtin.null_value in:              dst: %983
  call  vm.builtin.null_value in:              dst: %984
  call  vm.builtin.alloc_tensor in: %349, i0, c[163], c[1137] dst: %986
  call  matmul8          in: %985, %950, %986 dst: %void
  call  vm.builtin.null_value in:              dst: %985
  call  vm.builtin.null_value in:              dst: %946
  call  vm.builtin.null_value in:              dst: %950
  call  vm.builtin.reshape in: %986, c[204] dst: %987
  call  vm.builtin.alloc_tensor in: %340, i0, c[205], c[1138] dst: %988
  call  transpose16      in: %987, %988   dst: %void
  call  vm.builtin.null_value in:              dst: %986
  call  vm.builtin.null_value in:              dst: %987
  call  vm.builtin.reshape in: %988, c[11]  dst: %989
  call  vm.builtin.alloc_tensor in: %338, i0, c[86], c[1139] dst: %990
  call  transpose8       in: %122, %990   dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[1140] dst: %991
  call  matmul9          in: %989, %990, %991 dst: %void
  call  vm.builtin.null_value in:              dst: %988
  call  vm.builtin.null_value in:              dst: %989
  call  vm.builtin.null_value in:              dst: %990
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[1141] dst: %992
  call  add8             in: %991, %123, %992 dst: %void
  call  vm.builtin.null_value in:              dst: %991
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[1142] dst: %993
  call  add1             in: %936, %992, %993 dst: %void
  call  vm.builtin.null_value in:              dst: %936
  call  vm.builtin.null_value in:              dst: %992
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[1143] dst: %994
  call  layer_norm       in: %993, %126, %127, %994 dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[94], c[1144] dst: %995
  call  transpose10      in: %128, %995   dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1145] dst: %996
  call  matmul4          in: %994, %995, %996 dst: %void
  call  vm.builtin.null_value in:              dst: %994
  call  vm.builtin.null_value in:              dst: %995
  call  vm.builtin.alloc_tensor in: %425, i0, c[96], c[1146] dst: %997
  call  add7             in: %996, %129, %997 dst: %void
  call  vm.builtin.null_value in:              dst: %996
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1147] dst: %998
  call  gelu             in: %997, %998   dst: %void
  call  vm.builtin.null_value in:              dst: %997
  call  vm.builtin.alloc_tensor in: %333, i0, c[100], c[1148] dst: %999
  call  transpose11      in: %130, %999   dst: %void
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[1149] dst: %1000
  call  matmul5          in: %998, %999, %1000 dst: %void
  call  vm.builtin.null_value in:              dst: %998
  call  vm.builtin.null_value in:              dst: %999
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[1150] dst: %1001
  call  add8             in: %1000, %131, %1001 dst: %void
  call  vm.builtin.null_value in:              dst: %1000
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[1151] dst: %1002
  call  add1             in: %993, %1001, %1002 dst: %void
  call  vm.builtin.null_value in:              dst: %993
  call  vm.builtin.null_value in:              dst: %1001
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[1152] dst: %1003
  call  layer_norm       in: %1002, %132, %133, %1003 dst: %void
  call  vm.builtin.alloc_tensor in: %351, i0, c[17], c[1153] dst: %1004
  call  pad              in: %1003, %1004 dst: %void
  call  vm.builtin.null_value in:              dst: %1003
  call  vm.builtin.reshape in: %1004, c[19] dst: %1005
  call  vm.builtin.alloc_tensor in: %349, i0, c[20], c[1154] dst: %1006
  call  transpose1       in: %1005, %1006 dst: %void
  call  vm.builtin.null_value in:              dst: %1004
  call  vm.builtin.null_value in:              dst: %1005
  call  vm.builtin.reshape in: %1006, c[22] dst: %1007
  call  vm.builtin.alloc_tensor in: %340, i0, c[23], c[1155] dst: %1008
  call  transpose2       in: %134, %1008  dst: %void
  call  vm.builtin.alloc_tensor in: %333, i0, c[26], c[1156] dst: %1009
  call  matmul           in: %1007, %1008, %1009 dst: %void
  call  vm.builtin.null_value in:              dst: %1006
  call  vm.builtin.null_value in:              dst: %1007
  call  vm.builtin.null_value in:              dst: %1008
  call  vm.builtin.alloc_tensor in: %351, i0, c[26], c[1157] dst: %1010
  call  add2             in: %1009, %135, %1010 dst: %void
  call  vm.builtin.null_value in:              dst: %1009
  call  vm.builtin.reshape in: %1010, c[29] dst: %1011
  call  vm.builtin.alloc_tensor in: %349, i0, c[30], c[1158] dst: %1012
  call  transpose3       in: %1011, %1012 dst: %void
  call  vm.builtin.null_value in:              dst: %1010
  call  vm.builtin.null_value in:              dst: %1011
  call  vm.builtin.reshape in: %1012, c[32] dst: %1013
  call  vm.builtin.alloc_tensor in: %340, i0, c[33], c[1159] dst: %1014
  call  vm.builtin.alloc_tensor in: %333, i0, c[33], c[1160] dst: %1015
  call  vm.builtin.alloc_tensor in: %351, i0, c[33], c[1161] dst: %1016
  call  split            in: %1013, %1014, %1015, %1016 dst: %void
  call  vm.builtin.null_value in:              dst: %1012
  call  vm.builtin.null_value in:              dst: %1013
  call  vm.builtin.make_tuple in: %1014, %1015, %1016 dst: %1017
  call  vm.builtin.reshape in: %1014, c[38] dst: %1018
  call  vm.builtin.reshape in: %1015, c[38] dst: %1019
  call  vm.builtin.reshape in: %1016, c[38] dst: %1020
  call  vm.builtin.alloc_tensor in: %349, i0, c[38], c[1162] dst: %1021
  call  multiply         in: %1018, %1021 dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[41], c[1163] dst: %1022
  call  transpose4       in: %1019, %1022 dst: %void
  call  vm.builtin.null_value in:              dst: %1015
  call  vm.builtin.null_value in:              dst: %1019
  call  vm.builtin.alloc_tensor in: %333, i0, c[43], c[1164] dst: %1023
  call  matmul1          in: %1021, %1022, %1023 dst: %void
  call  vm.builtin.null_value in:              dst: %1021
  call  vm.builtin.null_value in:              dst: %1022
  call  vm.builtin.reshape in: %138, c[45]  dst: %1024
  call  vm.builtin.alloc_tensor in: %316, i0, c[48], c[1165] dst: %1025
  call  transpose5       in: %1024, %1025 dst: %void
  call  vm.builtin.null_value in:              dst: %1024
  call  vm.builtin.reshape in: %1025, c[50] dst: %1026
  call  vm.builtin.alloc_tensor in: %320, i0, c[52], c[1166] dst: %1027
  call  transpose6       in: %1026, %1027 dst: %void
  call  vm.builtin.null_value in:              dst: %1025
  call  vm.builtin.null_value in:              dst: %1026
  call  vm.builtin.reshape in: c[54], c[55] dst: %1028
  call  vm.builtin.reshape in: %1028, c[55] dst: %1029
  call  vm.builtin.null_value in:              dst: %1028
  call  vm.builtin.reshape in: c[54], c[56] dst: %1030
  call  vm.builtin.reshape in: %1030, c[56] dst: %1031
  call  vm.builtin.null_value in:              dst: %1030
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[1167] dst: %1032
  call  subtract         in: %1029, %1031, %1032 dst: %void
  call  vm.builtin.null_value in:              dst: %1029
  call  vm.builtin.null_value in:              dst: %1031
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[1168] dst: %1033
  call  add3             in: %1032, %1033 dst: %void
  call  vm.builtin.null_value in:              dst: %1032
  call  vm.builtin.alloc_tensor in: %318, i0, c[63], c[1169] dst: %1034
  call  take             in: %1027, %1033, %1034 dst: %void
  call  vm.builtin.null_value in:              dst: %1027
  call  vm.builtin.null_value in:              dst: %1033
  call  vm.builtin.reshape in: %139, c[45]  dst: %1035
  call  vm.builtin.alloc_tensor in: %316, i0, c[48], c[1170] dst: %1036
  call  transpose5       in: %1035, %1036 dst: %void
  call  vm.builtin.null_value in:              dst: %1035
  call  vm.builtin.reshape in: %1036, c[50] dst: %1037
  call  vm.builtin.alloc_tensor in: %320, i0, c[52], c[1171] dst: %1038
  call  transpose6       in: %1037, %1038 dst: %void
  call  vm.builtin.null_value in:              dst: %1036
  call  vm.builtin.null_value in:              dst: %1037
  call  vm.builtin.reshape in: c[54], c[55] dst: %1039
  call  vm.builtin.reshape in: %1039, c[55] dst: %1040
  call  vm.builtin.null_value in:              dst: %1039
  call  vm.builtin.reshape in: c[54], c[56] dst: %1041
  call  vm.builtin.reshape in: %1041, c[56] dst: %1042
  call  vm.builtin.null_value in:              dst: %1041
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[1172] dst: %1043
  call  subtract         in: %1040, %1042, %1043 dst: %void
  call  vm.builtin.null_value in:              dst: %1040
  call  vm.builtin.null_value in:              dst: %1042
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[1173] dst: %1044
  call  add3             in: %1043, %1044 dst: %void
  call  vm.builtin.null_value in:              dst: %1043
  call  vm.builtin.alloc_tensor in: %316, i0, c[63], c[1174] dst: %1045
  call  take             in: %1038, %1044, %1045 dst: %void
  call  vm.builtin.null_value in:              dst: %1038
  call  vm.builtin.null_value in:              dst: %1044
  call  vm.builtin.reshape in: %1018, c[72] dst: %1046
  call  vm.builtin.alloc_tensor in: %349, i0, c[73], c[1175] dst: %1047
  call  einsum           in: %1046, %1034, %1047 dst: %void
  call  vm.builtin.null_value in:              dst: %1034
  call  vm.builtin.alloc_tensor in: %367, i0, c[73], c[1176] dst: %1048
  call  einsum1          in: %1046, %1045, %1048 dst: %void
  call  vm.builtin.null_value in:              dst: %1014
  call  vm.builtin.null_value in:              dst: %1018
  call  vm.builtin.null_value in:              dst: %1046
  call  vm.builtin.null_value in:              dst: %1045
  call  vm.builtin.reshape in: %1023, c[76] dst: %1049
  call  vm.builtin.reshape in: %1047, c[77] dst: %1050
  call  vm.builtin.reshape in: %1048, c[78] dst: %1051
  call  vm.builtin.alloc_tensor in: %340, i0, c[76], c[1177] dst: %1052
  call  add4             in: %1049, %1050, %1052 dst: %void
  call  vm.builtin.null_value in:              dst: %1023
  call  vm.builtin.null_value in:              dst: %1049
  call  vm.builtin.null_value in:              dst: %1047
  call  vm.builtin.null_value in:              dst: %1050
  call  vm.builtin.alloc_tensor in: %333, i0, c[76], c[1178] dst: %1053
  call  add5             in: %1052, %1051, %1053 dst: %void
  call  vm.builtin.null_value in:              dst: %1052
  call  vm.builtin.null_value in:              dst: %1048
  call  vm.builtin.null_value in:              dst: %1051
  call  vm.builtin.reshape in: %1053, c[43] dst: %1054
  call  vm.builtin.alloc_tensor in: %349, i0, c[43], c[1179] dst: %1055
  call  softmax          in: %1054, %1055 dst: %void
  call  vm.builtin.null_value in:              dst: %1053
  call  vm.builtin.null_value in:              dst: %1054
  call  vm.builtin.alloc_tensor in: %340, i0, c[38], c[1180] dst: %1056
  call  matmul2          in: %1055, %1020, %1056 dst: %void
  call  vm.builtin.null_value in:              dst: %1055
  call  vm.builtin.null_value in:              dst: %1016
  call  vm.builtin.null_value in:              dst: %1020
  call  vm.builtin.reshape in: %1056, c[83] dst: %1057
  call  vm.builtin.alloc_tensor in: %333, i0, c[84], c[1181] dst: %1058
  call  transpose7       in: %1057, %1058 dst: %void
  call  vm.builtin.null_value in:              dst: %1056
  call  vm.builtin.null_value in:              dst: %1057
  call  vm.builtin.reshape in: %1058, c[22] dst: %1059
  call  vm.builtin.alloc_tensor in: %338, i0, c[86], c[1182] dst: %1060
  call  transpose8       in: %136, %1060  dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[22], c[1183] dst: %1061
  call  matmul3          in: %1059, %1060, %1061 dst: %void
  call  vm.builtin.null_value in:              dst: %1058
  call  vm.builtin.null_value in:              dst: %1059
  call  vm.builtin.null_value in:              dst: %1060
  call  vm.builtin.alloc_tensor in: %351, i0, c[22], c[1184] dst: %1062
  call  add6             in: %1061, %137, %1062 dst: %void
  call  vm.builtin.null_value in:              dst: %1061
  call  vm.builtin.reshape in: %1062, c[20] dst: %1063
  call  vm.builtin.alloc_tensor in: %340, i0, c[19], c[1185] dst: %1064
  call  transpose9       in: %1063, %1064 dst: %void
  call  vm.builtin.null_value in:              dst: %1062
  call  vm.builtin.null_value in:              dst: %1063
  call  vm.builtin.reshape in: %1064, c[17] dst: %1065
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[1186] dst: %1066
  call  strided_slice    in: %1065, %1066 dst: %void
  call  vm.builtin.null_value in:              dst: %1064
  call  vm.builtin.null_value in:              dst: %1065
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[1187] dst: %1067
  call  add1             in: %1002, %1066, %1067 dst: %void
  call  vm.builtin.null_value in:              dst: %1002
  call  vm.builtin.null_value in:              dst: %1066
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[1188] dst: %1068
  call  layer_norm       in: %1067, %140, %141, %1068 dst: %void
  call  vm.builtin.alloc_tensor in: %340, i0, c[94], c[1189] dst: %1069
  call  transpose10      in: %142, %1069  dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1190] dst: %1070
  call  matmul4          in: %1068, %1069, %1070 dst: %void
  call  vm.builtin.null_value in:              dst: %1068
  call  vm.builtin.null_value in:              dst: %1069
  call  vm.builtin.alloc_tensor in: %500, i0, c[96], c[1191] dst: %1071
  call  add7             in: %1070, %143, %1071 dst: %void
  call  vm.builtin.null_value in:              dst: %1070
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1192] dst: %1072
  call  gelu             in: %1071, %1072 dst: %void
  call  vm.builtin.null_value in:              dst: %1071
  call  vm.builtin.alloc_tensor in: %346, i0, c[100], c[1193] dst: %1073
  call  transpose11      in: %144, %1073  dst: %void
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[1194] dst: %1074
  call  matmul5          in: %1072, %1073, %1074 dst: %void
  call  vm.builtin.null_value in:              dst: %1072
  call  vm.builtin.null_value in:              dst: %1073
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[1195] dst: %1075
  call  add8             in: %1074, %145, %1075 dst: %void
  call  vm.builtin.null_value in:              dst: %1074
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[1196] dst: %1076
  call  add1             in: %1067, %1075, %1076 dst: %void
  call  vm.builtin.null_value in:              dst: %1067
  call  vm.builtin.null_value in:              dst: %1075
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[1197] dst: %1077
  call  layer_norm       in: %1076, %146, %147, %1077 dst: %void
  call  vm.builtin.alloc_tensor in: %333, i0, c[17], c[1198] dst: %1078
  call  pad              in: %1077, %1078 dst: %void
  call  vm.builtin.null_value in:              dst: %1077
  call  vm.builtin.reshape in: %1078, c[19] dst: %1079
  call  vm.builtin.alloc_tensor in: %349, i0, c[20], c[1199] dst: %1080
  call  transpose1       in: %1079, %1080 dst: %void
  call  vm.builtin.null_value in:              dst: %1078
  call  vm.builtin.null_value in:              dst: %1079
  call  vm.builtin.reshape in: %1080, c[22] dst: %1081
  call  vm.builtin.alloc_tensor in: %351, i0, c[23], c[1200] dst: %1082
  call  transpose2       in: %148, %1082  dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[26], c[1201] dst: %1083
  call  matmul           in: %1081, %1082, %1083 dst: %void
  call  vm.builtin.null_value in:              dst: %1080
  call  vm.builtin.null_value in:              dst: %1081
  call  vm.builtin.null_value in:              dst: %1082
  call  vm.builtin.alloc_tensor in: %333, i0, c[26], c[1202] dst: %1084
  call  add2             in: %1083, %149, %1084 dst: %void
  call  vm.builtin.null_value in:              dst: %1083
  call  vm.builtin.reshape in: %1084, c[29] dst: %1085
  call  vm.builtin.alloc_tensor in: %349, i0, c[30], c[1203] dst: %1086
  call  transpose3       in: %1085, %1086 dst: %void
  call  vm.builtin.null_value in:              dst: %1084
  call  vm.builtin.null_value in:              dst: %1085
  call  vm.builtin.reshape in: %1086, c[32] dst: %1087
  call  vm.builtin.alloc_tensor in: %351, i0, c[33], c[1204] dst: %1088
  call  vm.builtin.alloc_tensor in: %346, i0, c[33], c[1205] dst: %1089
  call  vm.builtin.alloc_tensor in: %333, i0, c[33], c[1206] dst: %1090
  call  split            in: %1087, %1088, %1089, %1090 dst: %void
  call  vm.builtin.null_value in:              dst: %1086
  call  vm.builtin.null_value in:              dst: %1087
  call  vm.builtin.make_tuple in: %1088, %1089, %1090 dst: %1091
  call  vm.builtin.reshape in: %1088, c[38] dst: %1092
  call  vm.builtin.reshape in: %1089, c[38] dst: %1093
  call  vm.builtin.reshape in: %1090, c[38] dst: %1094
  call  vm.builtin.alloc_tensor in: %349, i0, c[38], c[1207] dst: %1095
  call  multiply         in: %1092, %1095 dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[41], c[1208] dst: %1096
  call  transpose4       in: %1093, %1096 dst: %void
  call  vm.builtin.null_value in:              dst: %1089
  call  vm.builtin.null_value in:              dst: %1093
  call  vm.builtin.alloc_tensor in: %346, i0, c[43], c[1209] dst: %1097
  call  matmul1          in: %1095, %1096, %1097 dst: %void
  call  vm.builtin.null_value in:              dst: %1095
  call  vm.builtin.null_value in:              dst: %1096
  call  vm.builtin.reshape in: %152, c[45]  dst: %1098
  call  vm.builtin.alloc_tensor in: %320, i0, c[48], c[1210] dst: %1099
  call  transpose5       in: %1098, %1099 dst: %void
  call  vm.builtin.null_value in:              dst: %1098
  call  vm.builtin.reshape in: %1099, c[50] dst: %1100
  call  vm.builtin.alloc_tensor in: %318, i0, c[52], c[1211] dst: %1101
  call  transpose6       in: %1100, %1101 dst: %void
  call  vm.builtin.null_value in:              dst: %1099
  call  vm.builtin.null_value in:              dst: %1100
  call  vm.builtin.reshape in: c[54], c[55] dst: %1102
  call  vm.builtin.reshape in: %1102, c[55] dst: %1103
  call  vm.builtin.null_value in:              dst: %1102
  call  vm.builtin.reshape in: c[54], c[56] dst: %1104
  call  vm.builtin.reshape in: %1104, c[56] dst: %1105
  call  vm.builtin.null_value in:              dst: %1104
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[1212] dst: %1106
  call  subtract         in: %1103, %1105, %1106 dst: %void
  call  vm.builtin.null_value in:              dst: %1103
  call  vm.builtin.null_value in:              dst: %1105
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[1213] dst: %1107
  call  add3             in: %1106, %1107 dst: %void
  call  vm.builtin.null_value in:              dst: %1106
  call  vm.builtin.alloc_tensor in: %316, i0, c[63], c[1214] dst: %1108
  call  take             in: %1101, %1107, %1108 dst: %void
  call  vm.builtin.null_value in:              dst: %1101
  call  vm.builtin.null_value in:              dst: %1107
  call  vm.builtin.reshape in: %153, c[45]  dst: %1109
  call  vm.builtin.alloc_tensor in: %320, i0, c[48], c[1215] dst: %1110
  call  transpose5       in: %1109, %1110 dst: %void
  call  vm.builtin.null_value in:              dst: %1109
  call  vm.builtin.reshape in: %1110, c[50] dst: %1111
  call  vm.builtin.alloc_tensor in: %318, i0, c[52], c[1216] dst: %1112
  call  transpose6       in: %1111, %1112 dst: %void
  call  vm.builtin.null_value in:              dst: %1110
  call  vm.builtin.null_value in:              dst: %1111
  call  vm.builtin.reshape in: c[54], c[55] dst: %1113
  call  vm.builtin.reshape in: %1113, c[55] dst: %1114
  call  vm.builtin.null_value in:              dst: %1113
  call  vm.builtin.reshape in: c[54], c[56] dst: %1115
  call  vm.builtin.reshape in: %1115, c[56] dst: %1116
  call  vm.builtin.null_value in:              dst: %1115
  call  vm.builtin.alloc_tensor in: %384, i0, c[59], c[1217] dst: %1117
  call  subtract         in: %1114, %1116, %1117 dst: %void
  call  vm.builtin.null_value in:              dst: %1114
  call  vm.builtin.null_value in:              dst: %1116
  call  vm.builtin.alloc_tensor in: %386, i0, c[59], c[1218] dst: %1118
  call  add3             in: %1117, %1118 dst: %void
  call  vm.builtin.null_value in:              dst: %1117
  call  vm.builtin.alloc_tensor in: %320, i0, c[63], c[1219] dst: %1119
  call  take             in: %1112, %1118, %1119 dst: %void
  call  vm.builtin.null_value in:              dst: %1112
  call  vm.builtin.null_value in:              dst: %1118
  call  vm.builtin.reshape in: %1092, c[72] dst: %1120
  call  vm.builtin.alloc_tensor in: %349, i0, c[73], c[1220] dst: %1121
  call  einsum           in: %1120, %1108, %1121 dst: %void
  call  vm.builtin.null_value in:              dst: %1108
  call  vm.builtin.alloc_tensor in: %367, i0, c[73], c[1221] dst: %1122
  call  einsum1          in: %1120, %1119, %1122 dst: %void
  call  vm.builtin.null_value in:              dst: %1088
  call  vm.builtin.null_value in:              dst: %1092
  call  vm.builtin.null_value in:              dst: %1120
  call  vm.builtin.null_value in:              dst: %1119
  call  vm.builtin.reshape in: %1097, c[76] dst: %1123
  call  vm.builtin.reshape in: %1121, c[77] dst: %1124
  call  vm.builtin.reshape in: %1122, c[78] dst: %1125
  call  vm.builtin.alloc_tensor in: %351, i0, c[76], c[1222] dst: %1126
  call  add4             in: %1123, %1124, %1126 dst: %void
  call  vm.builtin.null_value in:              dst: %1097
  call  vm.builtin.null_value in:              dst: %1123
  call  vm.builtin.null_value in:              dst: %1121
  call  vm.builtin.null_value in:              dst: %1124
  call  vm.builtin.alloc_tensor in: %346, i0, c[76], c[1223] dst: %1127
  call  add5             in: %1126, %1125, %1127 dst: %void
  call  vm.builtin.null_value in:              dst: %1126
  call  vm.builtin.null_value in:              dst: %1122
  call  vm.builtin.null_value in:              dst: %1125
  call  vm.builtin.reshape in: %1127, c[43] dst: %1128
  call  vm.builtin.alloc_tensor in: %349, i0, c[43], c[1224] dst: %1129
  call  softmax          in: %1128, %1129 dst: %void
  call  vm.builtin.null_value in:              dst: %1127
  call  vm.builtin.null_value in:              dst: %1128
  call  vm.builtin.alloc_tensor in: %351, i0, c[38], c[1225] dst: %1130
  call  matmul2          in: %1129, %1094, %1130 dst: %void
  call  vm.builtin.null_value in:              dst: %1129
  call  vm.builtin.null_value in:              dst: %1090
  call  vm.builtin.null_value in:              dst: %1094
  call  vm.builtin.reshape in: %1130, c[83] dst: %1131
  call  vm.builtin.alloc_tensor in: %346, i0, c[84], c[1226] dst: %1132
  call  transpose7       in: %1131, %1132 dst: %void
  call  vm.builtin.null_value in:              dst: %1130
  call  vm.builtin.null_value in:              dst: %1131
  call  vm.builtin.reshape in: %1132, c[22] dst: %1133
  call  vm.builtin.alloc_tensor in: %338, i0, c[86], c[1227] dst: %1134
  call  transpose8       in: %150, %1134  dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[22], c[1228] dst: %1135
  call  matmul3          in: %1133, %1134, %1135 dst: %void
  call  vm.builtin.null_value in:              dst: %1132
  call  vm.builtin.null_value in:              dst: %1133
  call  vm.builtin.null_value in:              dst: %1134
  call  vm.builtin.alloc_tensor in: %333, i0, c[22], c[1229] dst: %1136
  call  add6             in: %1135, %151, %1136 dst: %void
  call  vm.builtin.null_value in:              dst: %1135
  call  vm.builtin.reshape in: %1136, c[20] dst: %1137
  call  vm.builtin.alloc_tensor in: %351, i0, c[19], c[1230] dst: %1138
  call  transpose9       in: %1137, %1138 dst: %void
  call  vm.builtin.null_value in:              dst: %1136
  call  vm.builtin.null_value in:              dst: %1137
  call  vm.builtin.reshape in: %1138, c[17] dst: %1139
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[1231] dst: %1140
  call  strided_slice    in: %1139, %1140 dst: %void
  call  vm.builtin.null_value in:              dst: %1138
  call  vm.builtin.null_value in:              dst: %1139
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[1232] dst: %1141
  call  add1             in: %1076, %1140, %1141 dst: %void
  call  vm.builtin.null_value in:              dst: %1076
  call  vm.builtin.null_value in:              dst: %1140
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[1233] dst: %1142
  call  layer_norm       in: %1141, %154, %155, %1142 dst: %void
  call  vm.builtin.alloc_tensor in: %351, i0, c[94], c[1234] dst: %1143
  call  transpose10      in: %156, %1143  dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1235] dst: %1144
  call  matmul4          in: %1142, %1143, %1144 dst: %void
  call  vm.builtin.null_value in:              dst: %1142
  call  vm.builtin.null_value in:              dst: %1143
  call  vm.builtin.alloc_tensor in: %425, i0, c[96], c[1236] dst: %1145
  call  add7             in: %1144, %157, %1145 dst: %void
  call  vm.builtin.null_value in:              dst: %1144
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1237] dst: %1146
  call  gelu             in: %1145, %1146 dst: %void
  call  vm.builtin.null_value in:              dst: %1145
  call  vm.builtin.alloc_tensor in: %340, i0, c[100], c[1238] dst: %1147
  call  transpose11      in: %158, %1147  dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[1239] dst: %1148
  call  matmul5          in: %1146, %1147, %1148 dst: %void
  call  vm.builtin.null_value in:              dst: %1146
  call  vm.builtin.null_value in:              dst: %1147
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[1240] dst: %1149
  call  add8             in: %1148, %159, %1149 dst: %void
  call  vm.builtin.null_value in:              dst: %1148
  call  vm.builtin.alloc_tensor in: %351, i0, c[11], c[1241] dst: %1150
  call  add1             in: %1141, %1149, %1150 dst: %void
  call  vm.builtin.null_value in:              dst: %1141
  call  vm.builtin.null_value in:              dst: %1149
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[1242] dst: %1151
  call  layer_norm       in: %1150, %160, %161, %1151 dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[23], c[1243] dst: %1152
  call  transpose2       in: %162, %1152  dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[152], c[1244] dst: %1153
  call  matmul6          in: %1151, %1152, %1153 dst: %void
  call  vm.builtin.null_value in:              dst: %1151
  call  vm.builtin.null_value in:              dst: %1152
  call  vm.builtin.alloc_tensor in: %333, i0, c[152], c[1245] dst: %1154
  call  add9             in: %1153, %163, %1154 dst: %void
  call  vm.builtin.null_value in:              dst: %1153
  call  vm.builtin.reshape in: %1154, c[155] dst: %1155
  call  vm.builtin.alloc_tensor in: %340, i0, c[156], c[1246] dst: %1156
  call  transpose12      in: %1155, %1156 dst: %void
  call  vm.builtin.null_value in:              dst: %1154
  call  vm.builtin.null_value in:              dst: %1155
  call  vm.builtin.reshape in: %1156, c[158] dst: %1157
  call  vm.builtin.alloc_tensor in: %346, i0, c[159], c[1247] dst: %1158
  call  vm.builtin.alloc_tensor in: %349, i0, c[159], c[1248] dst: %1159
  call  vm.builtin.alloc_tensor in: %333, i0, c[159], c[1249] dst: %1160
  call  split1           in: %1157, %1158, %1159, %1160 dst: %void
  call  vm.builtin.null_value in:              dst: %1156
  call  vm.builtin.null_value in:              dst: %1157
  call  vm.builtin.make_tuple in: %1158, %1159, %1160 dst: %1161
  call  vm.builtin.reshape in: %1158, c[163] dst: %1162
  call  vm.builtin.reshape in: %1159, c[163] dst: %1163
  call  vm.builtin.reshape in: %1160, c[163] dst: %1164
  call  vm.builtin.alloc_tensor in: %340, i0, c[163], c[1250] dst: %1165
  call  multiply3        in: %1162, %1165 dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[165], c[1251] dst: %1166
  call  transpose13      in: %1163, %1166 dst: %void
  call  vm.builtin.null_value in:              dst: %1159
  call  vm.builtin.null_value in:              dst: %1163
  call  vm.builtin.alloc_tensor in: %500, i0, c[168], c[1252] dst: %1167
  call  matmul7          in: %1165, %1166, %1167 dst: %void
  call  vm.builtin.null_value in:              dst: %1165
  call  vm.builtin.null_value in:              dst: %1166
  call  vm.builtin.reshape in: %166, c[170] dst: %1168
  call  vm.builtin.alloc_tensor in: %318, i0, c[171], c[1253] dst: %1169
  call  transpose14      in: %1168, %1169 dst: %void
  call  vm.builtin.null_value in:              dst: %1168
  call  vm.builtin.reshape in: %1169, c[173] dst: %1170
  call  vm.builtin.alloc_tensor in: %316, i0, c[174], c[1254] dst: %1171
  call  transpose15      in: %1170, %1171 dst: %void
  call  vm.builtin.null_value in:              dst: %1169
  call  vm.builtin.null_value in:              dst: %1170
  call  vm.builtin.reshape in: c[176], c[177] dst: %1172
  call  vm.builtin.reshape in: %1172, c[177] dst: %1173
  call  vm.builtin.null_value in:              dst: %1172
  call  vm.builtin.reshape in: c[176], c[178] dst: %1174
  call  vm.builtin.reshape in: %1174, c[178] dst: %1175
  call  vm.builtin.null_value in:              dst: %1174
  call  vm.builtin.alloc_tensor in: %532, i0, c[181], c[1255] dst: %1176
  call  subtract1        in: %1173, %1175, %1176 dst: %void
  call  vm.builtin.null_value in:              dst: %1173
  call  vm.builtin.null_value in:              dst: %1175
  call  vm.builtin.alloc_tensor in: %534, i0, c[181], c[1256] dst: %1177
  call  add10            in: %1176, %1177 dst: %void
  call  vm.builtin.null_value in:              dst: %1176
  call  vm.builtin.alloc_tensor in: %335, i0, c[186], c[1257] dst: %1178
  call  take1            in: %1171, %1177, %1178 dst: %void
  call  vm.builtin.null_value in:              dst: %1171
  call  vm.builtin.null_value in:              dst: %1177
  call  vm.builtin.reshape in: %167, c[170] dst: %1179
  call  vm.builtin.alloc_tensor in: %320, i0, c[171], c[1258] dst: %1180
  call  transpose14      in: %1179, %1180 dst: %void
  call  vm.builtin.null_value in:              dst: %1179
  call  vm.builtin.reshape in: %1180, c[173] dst: %1181
  call  vm.builtin.alloc_tensor in: %318, i0, c[174], c[1259] dst: %1182
  call  transpose15      in: %1181, %1182 dst: %void
  call  vm.builtin.null_value in:              dst: %1180
  call  vm.builtin.null_value in:              dst: %1181
  call  vm.builtin.reshape in: c[176], c[177] dst: %1183
  call  vm.builtin.reshape in: %1183, c[177] dst: %1184
  call  vm.builtin.null_value in:              dst: %1183
  call  vm.builtin.reshape in: c[176], c[178] dst: %1185
  call  vm.builtin.reshape in: %1185, c[178] dst: %1186
  call  vm.builtin.null_value in:              dst: %1185
  call  vm.builtin.alloc_tensor in: %532, i0, c[181], c[1260] dst: %1187
  call  subtract1        in: %1184, %1186, %1187 dst: %void
  call  vm.builtin.null_value in:              dst: %1184
  call  vm.builtin.null_value in:              dst: %1186
  call  vm.builtin.alloc_tensor in: %534, i0, c[181], c[1261] dst: %1188
  call  add10            in: %1187, %1188 dst: %void
  call  vm.builtin.null_value in:              dst: %1187
  call  vm.builtin.alloc_tensor in: %338, i0, c[186], c[1262] dst: %1189
  call  take1            in: %1182, %1188, %1189 dst: %void
  call  vm.builtin.null_value in:              dst: %1182
  call  vm.builtin.null_value in:              dst: %1188
  call  vm.builtin.reshape in: %1162, c[194] dst: %1190
  call  vm.builtin.alloc_tensor in: %349, i0, c[194], c[1263] dst: %1191
  call  einsum2          in: %1190, %1178, %1191 dst: %void
  call  vm.builtin.null_value in:              dst: %1178
  call  vm.builtin.alloc_tensor in: %340, i0, c[194], c[1264] dst: %1192
  call  einsum3          in: %1190, %1189, %1192 dst: %void
  call  vm.builtin.null_value in:              dst: %1158
  call  vm.builtin.null_value in:              dst: %1162
  call  vm.builtin.null_value in:              dst: %1190
  call  vm.builtin.null_value in:              dst: %1189
  call  vm.builtin.reshape in: %1167, c[197] dst: %1193
  call  vm.builtin.reshape in: %1191, c[198] dst: %1194
  call  vm.builtin.reshape in: %1192, c[199] dst: %1195
  call  vm.builtin.alloc_tensor in: %425, i0, c[197], c[1265] dst: %1196
  call  add11            in: %1193, %1194, %1196 dst: %void
  call  vm.builtin.null_value in:              dst: %1167
  call  vm.builtin.null_value in:              dst: %1193
  call  vm.builtin.null_value in:              dst: %1191
  call  vm.builtin.null_value in:              dst: %1194
  call  vm.builtin.alloc_tensor in: %500, i0, c[197], c[1266] dst: %1197
  call  add12            in: %1196, %1195, %1197 dst: %void
  call  vm.builtin.null_value in:              dst: %1196
  call  vm.builtin.null_value in:              dst: %1192
  call  vm.builtin.null_value in:              dst: %1195
  call  vm.builtin.reshape in: %1197, c[168] dst: %1198
  call  vm.builtin.alloc_tensor in: %425, i0, c[168], c[1267] dst: %1199
  call  softmax1         in: %1198, %1199 dst: %void
  call  vm.builtin.null_value in:              dst: %1197
  call  vm.builtin.null_value in:              dst: %1198
  call  vm.builtin.alloc_tensor in: %346, i0, c[163], c[1268] dst: %1200
  call  matmul8          in: %1199, %1164, %1200 dst: %void
  call  vm.builtin.null_value in:              dst: %1199
  call  vm.builtin.null_value in:              dst: %1160
  call  vm.builtin.null_value in:              dst: %1164
  call  vm.builtin.reshape in: %1200, c[204] dst: %1201
  call  vm.builtin.alloc_tensor in: %349, i0, c[205], c[1269] dst: %1202
  call  transpose16      in: %1201, %1202 dst: %void
  call  vm.builtin.null_value in:              dst: %1200
  call  vm.builtin.null_value in:              dst: %1201
  call  vm.builtin.reshape in: %1202, c[11] dst: %1203
  call  vm.builtin.alloc_tensor in: %338, i0, c[86], c[1270] dst: %1204
  call  transpose8       in: %164, %1204  dst: %void
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[1271] dst: %1205
  call  matmul9          in: %1203, %1204, %1205 dst: %void
  call  vm.builtin.null_value in:              dst: %1202
  call  vm.builtin.null_value in:              dst: %1203
  call  vm.builtin.null_value in:              dst: %1204
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[1272] dst: %1206
  call  add8             in: %1205, %165, %1206 dst: %void
  call  vm.builtin.null_value in:              dst: %1205
  call  vm.builtin.alloc_tensor in: %346, i0, c[11], c[1273] dst: %1207
  call  add1             in: %1150, %1206, %1207 dst: %void
  call  vm.builtin.null_value in:              dst: %1150
  call  vm.builtin.null_value in:              dst: %1206
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[1274] dst: %1208
  call  layer_norm       in: %1207, %168, %169, %1208 dst: %void
  call  vm.builtin.alloc_tensor in: %340, i0, c[94], c[1275] dst: %1209
  call  transpose10      in: %170, %1209  dst: %void
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1276] dst: %1210
  call  matmul4          in: %1208, %1209, %1210 dst: %void
  call  vm.builtin.null_value in:              dst: %1208
  call  vm.builtin.null_value in:              dst: %1209
  call  vm.builtin.alloc_tensor in: %500, i0, c[96], c[1277] dst: %1211
  call  add7             in: %1210, %171, %1211 dst: %void
  call  vm.builtin.null_value in:              dst: %1210
  call  vm.builtin.alloc_tensor in: %367, i0, c[96], c[1278] dst: %1212
  call  gelu             in: %1211, %1212 dst: %void
  call  vm.builtin.null_value in:              dst: %1211
  call  vm.builtin.alloc_tensor in: %351, i0, c[100], c[1279] dst: %1213
  call  transpose11      in: %172, %1213  dst: %void
  call  vm.builtin.alloc_tensor in: %333, i0, c[11], c[1280] dst: %1214
  call  matmul5          in: %1212, %1213, %1214 dst: %void
  call  vm.builtin.null_value in:              dst: %1212
  call  vm.builtin.null_value in:              dst: %1213
  call  vm.builtin.alloc_tensor in: %349, i0, c[11], c[1281] dst: %1215
  call  add8             in: %1214, %173, %1215 dst: %void
  call  vm.builtin.null_value in:              dst: %1214
  call  vm.builtin.alloc_tensor in: %340, i0, c[11], c[1282] dst: %1216
  call  add1             in: %1207, %1215, %1216 dst: %void
  call  vm.builtin.null_value in:              dst: %1207
  call  vm.builtin.null_value in:              dst: %1215
  call  vm.builtin.alloc_tensor in: %351, i0, c[5], c[1283] dst: %1217
  call  transpose17      in: %1216, %1217 dst: %void
  call  vm.builtin.null_value in:              dst: %1216
  call  vm.builtin.alloc_tensor in: %333, i0, c[615], c[1284] dst: %1218
  call  conv2d1          in: %1217, %174, %1218 dst: %void
  call  vm.builtin.null_value in:              dst: %1217
  call  vm.builtin.alloc_tensor in: %316, i0, c[617], c[1285] dst: %1219
  call  mean             in: %1218, %1219 dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[615], c[1286] dst: %1220
  call  subtract2        in: %1218, %1219, %1220 dst: %void
  call  vm.builtin.null_value in:              dst: %1218
  call  vm.builtin.null_value in:              dst: %1219
  call  vm.builtin.alloc_tensor in: %349, i0, c[615], c[1287] dst: %1221
  call  power            in: %1220, %1221 dst: %void
  call  vm.builtin.alloc_tensor in: %320, i0, c[617], c[1288] dst: %1222
  call  mean             in: %1221, %1222 dst: %void
  call  vm.builtin.null_value in:              dst: %1221
  call  vm.builtin.alloc_tensor in: %318, i0, c[617], c[1289] dst: %1223
  call  add13            in: %1222, %1223 dst: %void
  call  vm.builtin.null_value in:              dst: %1222
  call  vm.builtin.alloc_tensor in: %316, i0, c[617], c[1290] dst: %1224
  call  tir_sqrt         in: %1223, %1224 dst: %void
  call  vm.builtin.null_value in:              dst: %1223
  call  vm.builtin.alloc_tensor in: %340, i0, c[615], c[1291] dst: %1225
  call  divide           in: %1220, %1224, %1225 dst: %void
  call  vm.builtin.null_value in:              dst: %1220
  call  vm.builtin.null_value in:              dst: %1224
  call  vm.builtin.reshape in: %175, c[625] dst: %1226
  call  vm.builtin.reshape in: %1226, c[626] dst: %1227
  call  vm.builtin.null_value in:              dst: %1226
  call  vm.builtin.reshape in: %176, c[625] dst: %1228
  call  vm.builtin.reshape in: %1228, c[626] dst: %1229
  call  vm.builtin.null_value in:              dst: %1228
  call  vm.builtin.alloc_tensor in: %351, i0, c[615], c[1292] dst: %1230
  call  multiply6        in: %1227, %1225, %1230 dst: %void
  call  vm.builtin.null_value in:              dst: %1227
  call  vm.builtin.null_value in:              dst: %1225
  call  vm.builtin.alloc_tensor in: %333, i0, c[615], c[1293] dst: %1231
  call  add14            in: %1230, %1229, %1231 dst: %void
  call  vm.builtin.null_value in:              dst: %1229
  call  vm.builtin.null_value in:              dst: %1230
  call  vm.builtin.alloc_tensor in: %349, i0, c[615], c[1294] dst: %1232
  call  conv2d2          in: %1231, %177, %1232 dst: %void
  call  vm.builtin.null_value in:              dst: %1231
  call  vm.builtin.alloc_tensor in: %320, i0, c[617], c[1295] dst: %1233
  call  mean             in: %1232, %1233 dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[615], c[1296] dst: %1234
  call  subtract2        in: %1232, %1233, %1234 dst: %void
  call  vm.builtin.null_value in:              dst: %1232
  call  vm.builtin.null_value in:              dst: %1233
  call  vm.builtin.alloc_tensor in: %340, i0, c[615], c[1297] dst: %1235
  call  power            in: %1234, %1235 dst: %void
  call  vm.builtin.alloc_tensor in: %318, i0, c[617], c[1298] dst: %1236
  call  mean             in: %1235, %1236 dst: %void
  call  vm.builtin.null_value in:              dst: %1235
  call  vm.builtin.alloc_tensor in: %316, i0, c[617], c[1299] dst: %1237
  call  add13            in: %1236, %1237 dst: %void
  call  vm.builtin.null_value in:              dst: %1236
  call  vm.builtin.alloc_tensor in: %320, i0, c[617], c[1300] dst: %1238
  call  tir_sqrt         in: %1237, %1238 dst: %void
  call  vm.builtin.null_value in:              dst: %1237
  call  vm.builtin.alloc_tensor in: %351, i0, c[615], c[1301] dst: %1239
  call  divide           in: %1234, %1238, %1239 dst: %void
  call  vm.builtin.null_value in:              dst: %1234
  call  vm.builtin.null_value in:              dst: %1238
  call  vm.builtin.reshape in: %178, c[625] dst: %1240
  call  vm.builtin.reshape in: %1240, c[626] dst: %1241
  call  vm.builtin.null_value in:              dst: %1240
  call  vm.builtin.reshape in: %179, c[625] dst: %1242
  call  vm.builtin.reshape in: %1242, c[626] dst: %1243
  call  vm.builtin.null_value in:              dst: %1242
  call  vm.builtin.alloc_tensor in: %333, i0, c[615], c[1302] dst: %1244
  call  multiply6        in: %1241, %1239, %1244 dst: %void
  call  vm.builtin.null_value in:              dst: %1241
  call  vm.builtin.null_value in:              dst: %1239
  call  vm.builtin.alloc_tensor in: %349, i0, c[615], c[1303] dst: %1245
  call  add14            in: %1244, %1243, %1245 dst: %void
  call  vm.builtin.null_value in:              dst: %1243
  call  vm.builtin.null_value in:              dst: %1244
  call  vm.builtin.alloc_storage in: %vm, c[647], i0, c[1304], c[4] dst: %1246
  call  vm.builtin.alloc_tensor in: %1246, i0, c[645], c[1305] dst: %1247
  call  take2            in: %1, c[1306], %1247 dst: %void
  call  vm.builtin.null_value in:              dst: %1247
  call  vm.builtin.alloc_storage in: %vm, c[643], i0, c[1307], c[4] dst: %1248
  call  vm.builtin.alloc_tensor in: %1248, i0, c[645], c[1308] dst: %1249
  call  ones             in: %1249        dst: %void
  call  vm.builtin.alloc_tensor in: %1246, i0, c[649], c[1309] dst: %1250
  call  add15            in: %1, %1250    dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[658], i0, c[1310], c[4] dst: %1251
  call  vm.builtin.alloc_tensor in: %1251, i0, c[649], c[1311] dst: %1252
  call  zeros            in: %1252        dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[653], i0, c[1312], c[4] dst: %1253
  call  vm.builtin.alloc_tensor in: %1253, i0, c[645], c[1313] dst: %1254
  call  ones             in: %1254        dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[653], i0, c[1314], c[4] dst: %1255
  call  vm.builtin.alloc_tensor in: %1255, i0, c[645], c[1315] dst: %1256
  call  multiply7        in: %1254, %1256 dst: %void
  call  vm.builtin.null_value in:              dst: %1254
  call  vm.builtin.alloc_storage in: %vm, c[647], i0, c[1316], c[4] dst: %1257
  call  vm.builtin.alloc_tensor in: %1257, i0, c[660], c[1317] dst: %1258
  call  concatenate      in: %1250, %1252, %1258 dst: %void
  call  vm.builtin.null_value in:              dst: %1250
  call  vm.builtin.null_value in:              dst: %1252
  call  vm.builtin.alloc_tensor in: %1253, i0, c[662], c[1318] dst: %1259
  call  concatenate1     in: %1249, %1256, %1259 dst: %void
  call  vm.builtin.null_value in:              dst: %1249
  call  vm.builtin.null_value in:              dst: %1256
  call  vm.builtin.alloc_tensor in: %1246, i0, c[664], c[1319] dst: %1260
  call  strided_slice1   in: %1258, %1260 dst: %void
  call  vm.builtin.alloc_tensor in: %1251, i0, c[664], c[1320] dst: %1261
  call  divide1          in: %1260, %1261 dst: %void
  call  vm.builtin.null_value in:              dst: %1260
  call  vm.builtin.alloc_tensor in: %1246, i0, c[664], c[1321] dst: %1262
  call  strided_slice2   in: %1258, %1262 dst: %void
  call  vm.builtin.null_value in:              dst: %1258
  call  vm.builtin.alloc_tensor in: %1257, i0, c[664], c[1322] dst: %1263
  call  divide1          in: %1262, %1263 dst: %void
  call  vm.builtin.null_value in:              dst: %1262
  call  vm.builtin.alloc_tensor in: %1246, i0, c[660], c[1323] dst: %1264
  call  concatenate2     in: %1261, %1263, %1264 dst: %void
  call  vm.builtin.null_value in:              dst: %1261
  call  vm.builtin.null_value in:              dst: %1263
  call  vm.builtin.alloc_tensor in: %1251, i0, c[660], c[1324] dst: %1265
  call  add16            in: %1264, %1264, %1265 dst: %void
  call  vm.builtin.null_value in:              dst: %1264
  call  vm.builtin.alloc_tensor in: %1257, i0, c[660], c[1325] dst: %1266
  call  subtract3        in: %1265, %1266 dst: %void
  call  vm.builtin.null_value in:              dst: %1265
  call  vm.builtin.alloc_tensor in: %331, i0, c[674], c[1326] dst: %1267
  call  ones1            in: %1267        dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[672], i0, c[1327], c[4] dst: %1268
  call  vm.builtin.alloc_tensor in: %1268, i0, c[678], c[1328] dst: %1269
  call  matmul10         in: %1266, %1267, %1269 dst: %void
  call  vm.builtin.null_value in:              dst: %1266
  call  vm.builtin.null_value in:              dst: %1267
  call  vm.builtin.alloc_tensor in: %331, i0, c[678], c[1329] dst: %1270
  call  multiply8        in: %1269, %1270 dst: %void
  call  vm.builtin.null_value in:              dst: %1269
  call  vm.builtin.alloc_storage in: %vm, c[672], i0, c[1330], c[4] dst: %1271
  call  vm.builtin.alloc_tensor in: %1271, i0, c[678], c[1331] dst: %1272
  call  tir_sin          in: %1270, %1272 dst: %void
  call  vm.builtin.alloc_tensor in: %1268, i0, c[678], c[1332] dst: %1273
  call  tir_cos          in: %1270, %1273 dst: %void
  call  vm.builtin.null_value in:              dst: %1270
  call  vm.builtin.alloc_tensor in: %331, i0, c[684], c[1333] dst: %1274
  call  concatenate3     in: %1272, %1273, %1274 dst: %void
  call  vm.builtin.null_value in:              dst: %1272
  call  vm.builtin.null_value in:              dst: %1273
  call  vm.builtin.null_value in:              dst: %1274
  call  vm.builtin.reshape in: %1259, c[664] dst: %1275
  call  vm.builtin.alloc_storage in: %vm, c[686], i0, c[1334], c[4] dst: %1276
  call  vm.builtin.alloc_tensor in: %1276, i0, c[664], c[1335] dst: %1277
  call  equal            in: %1275, %1277 dst: %void
  call  vm.builtin.alloc_tensor in: %1271, i0, c[684], c[1336] dst: %1278
  call  where            in: %1277, %195, %195, %1278 dst: %void
  call  vm.builtin.null_value in:              dst: %1277
  call  vm.builtin.alloc_storage in: %vm, c[686], i0, c[1337], c[4] dst: %1279
  call  vm.builtin.alloc_tensor in: %1279, i0, c[664], c[1338] dst: %1280
  call  not_equal        in: %1275, %1280 dst: %void
  call  vm.builtin.alloc_tensor in: %1268, i0, c[684], c[1339] dst: %1281
  call  where1           in: %1280, %1278, %1278, %1281 dst: %void
  call  vm.builtin.null_value in:              dst: %1280
  call  vm.builtin.null_value in:              dst: %1278
  call  vm.builtin.alloc_tensor in: %1276, i0, c[662], c[1340] dst: %1282
  call  equal1           in: %1259, %1282 dst: %void
  call  vm.builtin.alloc_tensor in: %1279, i0, c[662], c[1341] dst: %1283
  call  equal2           in: %1259, %1283 dst: %void
  call  vm.builtin.null_value in:              dst: %1259
  call  vm.builtin.null_value in:              dst: %1275
  call  vm.builtin.reshape in: %1282, c[664] dst: %1284
  call  vm.builtin.reshape in: %191, c[695] dst: %1285
  call  vm.builtin.reshape in: %1285, c[696] dst: %1286
  call  vm.builtin.null_value in:              dst: %1285
  call  vm.builtin.alloc_tensor in: %331, i0, c[684], c[1342] dst: %1287
  call  add17            in: %1281, %1286, %1287 dst: %void
  call  vm.builtin.null_value in:              dst: %1286
  call  vm.builtin.null_value in:              dst: %1281
  call  vm.builtin.alloc_tensor in: %1271, i0, c[684], c[1343] dst: %1288
  call  where1           in: %1284, %1287, %1287, %1288 dst: %void
  call  vm.builtin.null_value in:              dst: %1282
  call  vm.builtin.null_value in:              dst: %1284
  call  vm.builtin.null_value in:              dst: %1287
  call  vm.builtin.reshape in: %1283, c[664] dst: %1289
  call  vm.builtin.reshape in: %192, c[695] dst: %1290
  call  vm.builtin.reshape in: %1290, c[696] dst: %1291
  call  vm.builtin.null_value in:              dst: %1290
  call  vm.builtin.alloc_tensor in: %1268, i0, c[684], c[1344] dst: %1292
  call  add17            in: %1288, %1291, %1292 dst: %void
  call  vm.builtin.null_value in:              dst: %1291
  call  vm.builtin.null_value in:              dst: %1288
  call  vm.builtin.alloc_tensor in: %331, i0, c[684], c[1345] dst: %1293
  call  where1           in: %1289, %1292, %1292, %1293 dst: %void
  call  vm.builtin.null_value in:              dst: %1283
  call  vm.builtin.null_value in:              dst: %1289
  call  vm.builtin.null_value in:              dst: %1292
  call  vm.builtin.null_value in:              dst: %1293
  call  vm.builtin.reshape in: %190, c[703] dst: %1294
  call  vm.builtin.reshape in: %1294, c[703] dst: %1295
  call  vm.builtin.null_value in:              dst: %1294
  call  vm.builtin.alloc_tensor in: %320, i0, c[705], c[1346] dst: %1296
  call  repeat1          in: %1295, %1296 dst: %void
  call  vm.builtin.null_value in:              dst: %1295
  call  vm.builtin.alloc_tensor in: %340, i0, c[615], c[1347] dst: %1297
  call  repeat2          in: %1296, %1297 dst: %void
  call  vm.builtin.null_value in:              dst: %1296
  call  vm.builtin.alloc_tensor in: %318, i0, c[1348], c[1349] dst: %1298
  call  concatenate6     in: %196, %197, %1298 dst: %void
  call  vm.builtin.reshape in: %1298, c[1350] dst: %1299
  call  vm.builtin.alloc_tensor in: %346, i0, c[615], c[1351] dst: %1300
  call  add19            in: %1245, %1297, %1300 dst: %void
  call  vm.builtin.null_value in:              dst: %1245
  call  vm.builtin.null_value in:              dst: %1297
  call  vm.builtin.reshape in: %1300, c[615] dst: %1301
  call  vm.builtin.reshape in: %1301, c[615] dst: %1302
  call  vm.builtin.reshape in: %345, c[615] dst: %1303
  call  vm.builtin.reshape in: %1302, c[1352] dst: %1304
  call  vm.builtin.reshape in: %1304, c[1353] dst: %1305
  call  vm.builtin.alloc_tensor in: %351, i0, c[1354], c[1355] dst: %1306
  call  transpose19      in: %1305, %1306 dst: %void
  call  vm.builtin.null_value in:              dst: %1300
  call  vm.builtin.null_value in:              dst: %1301
  call  vm.builtin.null_value in:              dst: %1302
  call  vm.builtin.null_value in:              dst: %1304
  call  vm.builtin.null_value in:              dst: %1305
  call  vm.builtin.reshape in: %1306, c[1356] dst: %1307
  call  vm.builtin.reshape in: %1303, c[1352] dst: %1308
  call  vm.builtin.reshape in: %1308, c[1353] dst: %1309
  call  vm.builtin.alloc_tensor in: %333, i0, c[1354], c[1357] dst: %1310
  call  transpose19      in: %1309, %1310 dst: %void
  call  vm.builtin.null_value in:              dst: %343
  call  vm.builtin.null_value in:              dst: %344
  call  vm.builtin.null_value in:              dst: %345
  call  vm.builtin.null_value in:              dst: %1303
  call  vm.builtin.null_value in:              dst: %1308
  call  vm.builtin.null_value in:              dst: %1309
  call  vm.builtin.reshape in: %1310, c[1356] dst: %1311
  call  vm.builtin.alloc_tensor in: %335, i0, c[1358], c[1359] dst: %1312
  call  transpose20      in: %198, %1312  dst: %void
  call  vm.builtin.alloc_tensor in: %316, i0, c[1350], c[1360] dst: %1313
  call  matmul12         in: %1299, %1312, %1313 dst: %void
  call  vm.builtin.null_value in:              dst: %1312
  call  vm.builtin.alloc_tensor in: %320, i0, c[1350], c[1361] dst: %1314
  call  add20            in: %1313, %199, %1314 dst: %void
  call  vm.builtin.null_value in:              dst: %1313
  call  vm.builtin.alloc_tensor in: %335, i0, c[1358], c[1362] dst: %1315
  call  transpose20      in: %200, %1315  dst: %void
  call  vm.builtin.alloc_tensor in: %316, i0, c[1350], c[1363] dst: %1316
  call  matmul12         in: %1299, %1315, %1316 dst: %void
  call  vm.builtin.null_value in:              dst: %1315
  call  vm.builtin.alloc_tensor in: %331, i0, c[1350], c[1364] dst: %1317
  call  add20            in: %1316, %201, %1317 dst: %void
  call  vm.builtin.null_value in:              dst: %1316
  call  vm.builtin.alloc_tensor in: %335, i0, c[1358], c[1365] dst: %1318
  call  transpose20      in: %202, %1318  dst: %void
  call  vm.builtin.alloc_tensor in: %316, i0, c[1350], c[1366] dst: %1319
  call  matmul12         in: %1299, %1318, %1319 dst: %void
  call  vm.builtin.null_value in:              dst: %1318
  call  vm.builtin.alloc_tensor in: %1268, i0, c[1350], c[1367] dst: %1320
  call  add20            in: %1319, %203, %1320 dst: %void
  call  vm.builtin.null_value in:              dst: %1319
  call  vm.builtin.reshape in: %1314, c[1368] dst: %1321
  call  vm.builtin.alloc_tensor in: %316, i0, c[1369], c[1370] dst: %1322
  call  transpose21      in: %1321, %1322 dst: %void
  call  vm.builtin.null_value in:              dst: %1314
  call  vm.builtin.null_value in:              dst: %1321
  call  vm.builtin.reshape in: %1317, c[1368] dst: %1323
  call  vm.builtin.alloc_tensor in: %320, i0, c[1369], c[1371] dst: %1324
  call  transpose21      in: %1323, %1324 dst: %void
  call  vm.builtin.null_value in:              dst: %1317
  call  vm.builtin.null_value in:              dst: %1323
  call  vm.builtin.reshape in: %1320, c[1368] dst: %1325
  call  vm.builtin.alloc_tensor in: %331, i0, c[1369], c[1372] dst: %1326
  call  transpose21      in: %1325, %1326 dst: %void
  call  vm.builtin.null_value in:              dst: %1320
  call  vm.builtin.null_value in:              dst: %1325
  call  vm.builtin.alloc_tensor in: %1268, i0, c[1373], c[1374] dst: %1327
  call  transpose22      in: %1324, %1327 dst: %void
  call  vm.builtin.null_value in:              dst: %1324
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1375], c[1376] dst: %1328
  call  matmul13         in: %1322, %1327, %1328 dst: %void
  call  vm.builtin.null_value in:              dst: %1322
  call  vm.builtin.null_value in:              dst: %1327
  call  vm.builtin.alloc_tensor in: %1268, i0, c[1375], c[1377] dst: %1329
  call  divide3          in: %1328, %1329 dst: %void
  call  vm.builtin.null_value in:              dst: %1328
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1375], c[1378] dst: %1330
  call  softmax2         in: %1329, %1330 dst: %void
  call  vm.builtin.null_value in:              dst: %1329
  call  vm.builtin.alloc_tensor in: %1268, i0, c[1369], c[1379] dst: %1331
  call  matmul14         in: %1330, %1326, %1331 dst: %void
  call  vm.builtin.null_value in:              dst: %1330
  call  vm.builtin.null_value in:              dst: %1326
  call  vm.builtin.alloc_tensor in: %331, i0, c[1368], c[1380] dst: %1332
  call  transpose23      in: %1331, %1332 dst: %void
  call  vm.builtin.null_value in:              dst: %1331
  call  vm.builtin.reshape in: %1332, c[1350] dst: %1333
  call  vm.builtin.alloc_tensor in: %335, i0, c[1358], c[1381] dst: %1334
  call  transpose20      in: %204, %1334  dst: %void
  call  vm.builtin.alloc_tensor in: %1268, i0, c[1350], c[1382] dst: %1335
  call  matmul12         in: %1333, %1334, %1335 dst: %void
  call  vm.builtin.null_value in:              dst: %1332
  call  vm.builtin.null_value in:              dst: %1333
  call  vm.builtin.null_value in:              dst: %1334
  call  vm.builtin.alloc_tensor in: %331, i0, c[1350], c[1383] dst: %1336
  call  add20            in: %1335, %205, %1336 dst: %void
  call  vm.builtin.null_value in:              dst: %1335
  call  vm.builtin.alloc_tensor in: %1268, i0, c[1350], c[1384] dst: %1337
  call  layer_norm1      in: %1336, %206, %207, %1337 dst: %void
  call  vm.builtin.null_value in:              dst: %1336
  call  vm.builtin.alloc_tensor in: %331, i0, c[1350], c[1385] dst: %1338
  call  add21            in: %1337, %1299, %1338 dst: %void
  call  vm.builtin.alloc_tensor in: %349, i0, c[1356], c[1386] dst: %1339
  call  add22            in: %1307, %1311, %1339 dst: %void
  call  vm.builtin.alloc_tensor in: %335, i0, c[1387], c[1388] dst: %1340
  call  transpose24      in: %208, %1340  dst: %void
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1389], c[1390] dst: %1341
  call  matmul15         in: %1338, %1340, %1341 dst: %void
  call  vm.builtin.null_value in:              dst: %1338
  call  vm.builtin.null_value in:              dst: %1340
  call  vm.builtin.alloc_tensor in: %331, i0, c[1389], c[1391] dst: %1342
  call  add23            in: %1341, %209, %1342 dst: %void
  call  vm.builtin.null_value in:              dst: %1341
  call  vm.builtin.alloc_tensor in: %335, i0, c[1387], c[1392] dst: %1343
  call  transpose24      in: %210, %1343  dst: %void
  call  vm.builtin.alloc_tensor in: %338, i0, c[1393], c[1394] dst: %1344
  call  matmul16         in: %1339, %1343, %1344 dst: %void
  call  vm.builtin.null_value in:              dst: %1339
  call  vm.builtin.null_value in:              dst: %1343
  call  vm.builtin.alloc_tensor in: %335, i0, c[1393], c[1395] dst: %1345
  call  add24            in: %1344, %211, %1345 dst: %void
  call  vm.builtin.null_value in:              dst: %1344
  call  vm.builtin.alloc_tensor in: %320, i0, c[1387], c[1396] dst: %1346
  call  transpose24      in: %212, %1346  dst: %void
  call  vm.builtin.alloc_tensor in: %338, i0, c[1393], c[1397] dst: %1347
  call  matmul16         in: %1307, %1346, %1347 dst: %void
  call  vm.builtin.null_value in:              dst: %1346
  call  vm.builtin.alloc_tensor in: %320, i0, c[1393], c[1398] dst: %1348
  call  add24            in: %1347, %213, %1348 dst: %void
  call  vm.builtin.null_value in:              dst: %1347
  call  vm.builtin.reshape in: %1342, c[1399] dst: %1349
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1400], c[1401] dst: %1350
  call  transpose25      in: %1349, %1350 dst: %void
  call  vm.builtin.null_value in:              dst: %1342
  call  vm.builtin.null_value in:              dst: %1349
  call  vm.builtin.reshape in: %1345, c[1402] dst: %1351
  call  vm.builtin.alloc_tensor in: %338, i0, c[1403], c[1404] dst: %1352
  call  transpose26      in: %1351, %1352 dst: %void
  call  vm.builtin.null_value in:              dst: %1345
  call  vm.builtin.null_value in:              dst: %1351
  call  vm.builtin.reshape in: %1348, c[1402] dst: %1353
  call  vm.builtin.alloc_tensor in: %335, i0, c[1403], c[1405] dst: %1354
  call  transpose26      in: %1353, %1354 dst: %void
  call  vm.builtin.null_value in:              dst: %1348
  call  vm.builtin.null_value in:              dst: %1353
  call  vm.builtin.alloc_tensor in: %320, i0, c[1406], c[1407] dst: %1355
  call  transpose27      in: %1352, %1355 dst: %void
  call  vm.builtin.null_value in:              dst: %1352
  call  vm.builtin.alloc_tensor in: %338, i0, c[1408], c[1409] dst: %1356
  call  matmul17         in: %1350, %1355, %1356 dst: %void
  call  vm.builtin.null_value in:              dst: %1350
  call  vm.builtin.null_value in:              dst: %1355
  call  vm.builtin.alloc_tensor in: %320, i0, c[1408], c[1410] dst: %1357
  call  divide4          in: %1356, %1357 dst: %void
  call  vm.builtin.null_value in:              dst: %1356
  call  vm.builtin.alloc_tensor in: %338, i0, c[1408], c[1411] dst: %1358
  call  softmax3         in: %1357, %1358 dst: %void
  call  vm.builtin.null_value in:              dst: %1357
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1400], c[1412] dst: %1359
  call  matmul18         in: %1358, %1354, %1359 dst: %void
  call  vm.builtin.null_value in:              dst: %1358
  call  vm.builtin.null_value in:              dst: %1354
  call  vm.builtin.alloc_tensor in: %331, i0, c[1399], c[1413] dst: %1360
  call  transpose28      in: %1359, %1360 dst: %void
  call  vm.builtin.null_value in:              dst: %1359
  call  vm.builtin.reshape in: %1360, c[1389] dst: %1361
  call  vm.builtin.alloc_tensor in: %320, i0, c[1414], c[1415] dst: %1362
  call  transpose29      in: %214, %1362  dst: %void
  call  vm.builtin.alloc_tensor in: %316, i0, c[1350], c[1416] dst: %1363
  call  matmul19         in: %1361, %1362, %1363 dst: %void
  call  vm.builtin.null_value in:              dst: %1360
  call  vm.builtin.null_value in:              dst: %1361
  call  vm.builtin.null_value in:              dst: %1362
  call  vm.builtin.alloc_tensor in: %331, i0, c[1350], c[1417] dst: %1364
  call  add20            in: %1363, %215, %1364 dst: %void
  call  vm.builtin.null_value in:              dst: %1363
  call  vm.builtin.alloc_tensor in: %316, i0, c[1350], c[1418] dst: %1365
  call  add21            in: %1337, %1364, %1365 dst: %void
  call  vm.builtin.null_value in:              dst: %1337
  call  vm.builtin.null_value in:              dst: %1364
  call  vm.builtin.alloc_tensor in: %1268, i0, c[1350], c[1419] dst: %1366
  call  layer_norm1      in: %1365, %216, %217, %1366 dst: %void
  call  vm.builtin.null_value in:              dst: %1365
  call  vm.builtin.alloc_tensor in: %335, i0, c[1420], c[1421] dst: %1367
  call  transpose30      in: %218, %1367  dst: %void
  call  vm.builtin.alloc_tensor in: %316, i0, c[1422], c[1423] dst: %1368
  call  matmul20         in: %1366, %1367, %1368 dst: %void
  call  vm.builtin.null_value in:              dst: %1367
  call  vm.builtin.alloc_tensor in: %331, i0, c[1422], c[1424] dst: %1369
  call  add25            in: %1368, %219, %1369 dst: %void
  call  vm.builtin.null_value in:              dst: %1368
  call  vm.builtin.alloc_tensor in: %316, i0, c[1422], c[1425] dst: %1370
  call  relu             in: %1369, %1370 dst: %void
  call  vm.builtin.null_value in:              dst: %1369
  call  vm.builtin.alloc_tensor in: %320, i0, c[1426], c[1427] dst: %1371
  call  transpose31      in: %220, %1371  dst: %void
  call  vm.builtin.alloc_tensor in: %331, i0, c[1350], c[1428] dst: %1372
  call  matmul21         in: %1370, %1371, %1372 dst: %void
  call  vm.builtin.null_value in:              dst: %1370
  call  vm.builtin.null_value in:              dst: %1371
  call  vm.builtin.alloc_tensor in: %316, i0, c[1350], c[1429] dst: %1373
  call  add20            in: %1372, %221, %1373 dst: %void
  call  vm.builtin.null_value in:              dst: %1372
  call  vm.builtin.alloc_tensor in: %331, i0, c[1350], c[1430] dst: %1374
  call  add21            in: %1366, %1373, %1374 dst: %void
  call  vm.builtin.null_value in:              dst: %1366
  call  vm.builtin.null_value in:              dst: %1373
  call  vm.builtin.alloc_tensor in: %1268, i0, c[1350], c[1431] dst: %1375
  call  layer_norm1      in: %1374, %222, %223, %1375 dst: %void
  call  vm.builtin.null_value in:              dst: %1374
  call  vm.builtin.alloc_tensor in: %331, i0, c[1350], c[1432] dst: %1376
  call  add21            in: %1375, %1299, %1376 dst: %void
  call  vm.builtin.alloc_tensor in: %340, i0, c[1356], c[1433] dst: %1377
  call  add22            in: %1307, %1311, %1377 dst: %void
  call  vm.builtin.alloc_tensor in: %335, i0, c[1387], c[1434] dst: %1378
  call  transpose24      in: %226, %1378  dst: %void
  call  vm.builtin.alloc_tensor in: %320, i0, c[1393], c[1435] dst: %1379
  call  matmul16         in: %1377, %1378, %1379 dst: %void
  call  vm.builtin.null_value in:              dst: %1377
  call  vm.builtin.null_value in:              dst: %1378
  call  vm.builtin.alloc_tensor in: %335, i0, c[1393], c[1436] dst: %1380
  call  add24            in: %1379, %227, %1380 dst: %void
  call  vm.builtin.null_value in:              dst: %1379
  call  vm.builtin.alloc_tensor in: %320, i0, c[1387], c[1437] dst: %1381
  call  transpose24      in: %228, %1381  dst: %void
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1389], c[1438] dst: %1382
  call  matmul15         in: %1376, %1381, %1382 dst: %void
  call  vm.builtin.null_value in:              dst: %1376
  call  vm.builtin.null_value in:              dst: %1381
  call  vm.builtin.alloc_tensor in: %331, i0, c[1389], c[1439] dst: %1383
  call  add23            in: %1382, %229, %1383 dst: %void
  call  vm.builtin.null_value in:              dst: %1382
  call  vm.builtin.alloc_tensor in: %320, i0, c[1387], c[1440] dst: %1384
  call  transpose24      in: %230, %1384  dst: %void
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1389], c[1441] dst: %1385
  call  matmul15         in: %1375, %1384, %1385 dst: %void
  call  vm.builtin.null_value in:              dst: %1384
  call  vm.builtin.alloc_storage in: %vm, c[672], i0, c[1442], c[4] dst: %1386
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1389], c[1443] dst: %1387
  call  add23            in: %1385, %231, %1387 dst: %void
  call  vm.builtin.null_value in:              dst: %1385
  call  vm.builtin.reshape in: %1380, c[1402] dst: %1388
  call  vm.builtin.alloc_tensor in: %320, i0, c[1403], c[1444] dst: %1389
  call  transpose26      in: %1388, %1389 dst: %void
  call  vm.builtin.null_value in:              dst: %1380
  call  vm.builtin.null_value in:              dst: %1388
  call  vm.builtin.reshape in: %1383, c[1399] dst: %1390
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1400], c[1445] dst: %1391
  call  transpose25      in: %1390, %1391 dst: %void
  call  vm.builtin.null_value in:              dst: %1383
  call  vm.builtin.null_value in:              dst: %1390
  call  vm.builtin.reshape in: %1387, c[1399] dst: %1392
  call  vm.builtin.alloc_tensor in: %331, i0, c[1400], c[1446] dst: %1393
  call  transpose25      in: %1392, %1393 dst: %void
  call  vm.builtin.null_value in:              dst: %1387
  call  vm.builtin.null_value in:              dst: %1392
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1447], c[1448] dst: %1394
  call  transpose32      in: %1391, %1394 dst: %void
  call  vm.builtin.null_value in:              dst: %1391
  call  vm.builtin.alloc_tensor in: %335, i0, c[1449], c[1450] dst: %1395
  call  matmul22         in: %1389, %1394, %1395 dst: %void
  call  vm.builtin.null_value in:              dst: %1389
  call  vm.builtin.null_value in:              dst: %1394
  call  vm.builtin.alloc_tensor in: %320, i0, c[1449], c[1451] dst: %1396
  call  divide5          in: %1395, %1396 dst: %void
  call  vm.builtin.null_value in:              dst: %1395
  call  vm.builtin.alloc_tensor in: %335, i0, c[1449], c[1452] dst: %1397
  call  softmax4         in: %1396, %1397 dst: %void
  call  vm.builtin.null_value in:              dst: %1396
  call  vm.builtin.alloc_tensor in: %320, i0, c[1403], c[1453] dst: %1398
  call  matmul23         in: %1397, %1393, %1398 dst: %void
  call  vm.builtin.null_value in:              dst: %1397
  call  vm.builtin.null_value in:              dst: %1393
  call  vm.builtin.alloc_tensor in: %335, i0, c[1402], c[1454] dst: %1399
  call  transpose33      in: %1398, %1399 dst: %void
  call  vm.builtin.null_value in:              dst: %1398
  call  vm.builtin.reshape in: %1399, c[1393] dst: %1400
  call  vm.builtin.alloc_tensor in: %320, i0, c[1414], c[1455] dst: %1401
  call  transpose29      in: %232, %1401  dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[1356], c[1456] dst: %1402
  call  matmul24         in: %1400, %1401, %1402 dst: %void
  call  vm.builtin.null_value in:              dst: %1399
  call  vm.builtin.null_value in:              dst: %1400
  call  vm.builtin.null_value in:              dst: %1401
  call  vm.builtin.alloc_tensor in: %342, i0, c[1356], c[1457] dst: %1403
  call  add26            in: %1402, %233, %1403 dst: %void
  call  vm.builtin.null_value in:              dst: %1402
  call  vm.builtin.alloc_tensor in: %349, i0, c[1356], c[1458] dst: %1404
  call  add22            in: %1307, %1403, %1404 dst: %void
  call  vm.builtin.null_value in:              dst: %1306
  call  vm.builtin.null_value in:              dst: %1307
  call  vm.builtin.null_value in:              dst: %1403
  call  vm.builtin.alloc_tensor in: %340, i0, c[1356], c[1459] dst: %1405
  call  layer_norm2      in: %1404, %224, %225, %1405 dst: %void
  call  vm.builtin.null_value in:              dst: %1404
  call  vm.builtin.alloc_tensor in: %331, i0, c[1350], c[1460] dst: %1406
  call  add21            in: %1375, %1299, %1406 dst: %void
  call  vm.builtin.alloc_tensor in: %335, i0, c[1358], c[1461] dst: %1407
  call  transpose20      in: %234, %1407  dst: %void
  call  vm.builtin.alloc_tensor in: %316, i0, c[1350], c[1462] dst: %1408
  call  matmul12         in: %1406, %1407, %1408 dst: %void
  call  vm.builtin.null_value in:              dst: %1407
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1350], c[1463] dst: %1409
  call  add20            in: %1408, %235, %1409 dst: %void
  call  vm.builtin.null_value in:              dst: %1408
  call  vm.builtin.alloc_tensor in: %320, i0, c[1358], c[1464] dst: %1410
  call  transpose20      in: %236, %1410  dst: %void
  call  vm.builtin.alloc_tensor in: %316, i0, c[1350], c[1465] dst: %1411
  call  matmul12         in: %1406, %1410, %1411 dst: %void
  call  vm.builtin.null_value in:              dst: %1406
  call  vm.builtin.null_value in:              dst: %1410
  call  vm.builtin.alloc_tensor in: %331, i0, c[1350], c[1466] dst: %1412
  call  add20            in: %1411, %237, %1412 dst: %void
  call  vm.builtin.null_value in:              dst: %1411
  call  vm.builtin.alloc_tensor in: %335, i0, c[1358], c[1467] dst: %1413
  call  transpose20      in: %238, %1413  dst: %void
  call  vm.builtin.alloc_tensor in: %316, i0, c[1350], c[1468] dst: %1414
  call  matmul12         in: %1375, %1413, %1414 dst: %void
  call  vm.builtin.null_value in:              dst: %1413
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1350], c[1469] dst: %1415
  call  add20            in: %1414, %239, %1415 dst: %void
  call  vm.builtin.null_value in:              dst: %1414
  call  vm.builtin.reshape in: %1409, c[1368] dst: %1416
  call  vm.builtin.alloc_tensor in: %316, i0, c[1369], c[1470] dst: %1417
  call  transpose21      in: %1416, %1417 dst: %void
  call  vm.builtin.null_value in:              dst: %1409
  call  vm.builtin.null_value in:              dst: %1416
  call  vm.builtin.reshape in: %1412, c[1368] dst: %1418
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1369], c[1471] dst: %1419
  call  transpose21      in: %1418, %1419 dst: %void
  call  vm.builtin.null_value in:              dst: %1412
  call  vm.builtin.null_value in:              dst: %1418
  call  vm.builtin.reshape in: %1415, c[1368] dst: %1420
  call  vm.builtin.alloc_tensor in: %331, i0, c[1369], c[1472] dst: %1421
  call  transpose21      in: %1420, %1421 dst: %void
  call  vm.builtin.null_value in:              dst: %1415
  call  vm.builtin.null_value in:              dst: %1420
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1373], c[1473] dst: %1422
  call  transpose22      in: %1419, %1422 dst: %void
  call  vm.builtin.null_value in:              dst: %1419
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1375], c[1474] dst: %1423
  call  matmul13         in: %1417, %1422, %1423 dst: %void
  call  vm.builtin.null_value in:              dst: %1417
  call  vm.builtin.null_value in:              dst: %1422
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1375], c[1475] dst: %1424
  call  divide3          in: %1423, %1424 dst: %void
  call  vm.builtin.null_value in:              dst: %1423
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1375], c[1476] dst: %1425
  call  softmax2         in: %1424, %1425 dst: %void
  call  vm.builtin.null_value in:              dst: %1424
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1369], c[1477] dst: %1426
  call  matmul14         in: %1425, %1421, %1426 dst: %void
  call  vm.builtin.null_value in:              dst: %1425
  call  vm.builtin.null_value in:              dst: %1421
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1368], c[1478] dst: %1427
  call  transpose23      in: %1426, %1427 dst: %void
  call  vm.builtin.null_value in:              dst: %1426
  call  vm.builtin.reshape in: %1427, c[1350] dst: %1428
  call  vm.builtin.alloc_tensor in: %320, i0, c[1358], c[1479] dst: %1429
  call  transpose20      in: %240, %1429  dst: %void
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1350], c[1480] dst: %1430
  call  matmul12         in: %1428, %1429, %1430 dst: %void
  call  vm.builtin.null_value in:              dst: %1427
  call  vm.builtin.null_value in:              dst: %1428
  call  vm.builtin.null_value in:              dst: %1429
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1350], c[1481] dst: %1431
  call  add20            in: %1430, %241, %1431 dst: %void
  call  vm.builtin.null_value in:              dst: %1430
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1350], c[1482] dst: %1432
  call  add21            in: %1375, %1431, %1432 dst: %void
  call  vm.builtin.null_value in:              dst: %1375
  call  vm.builtin.null_value in:              dst: %1431
  call  vm.builtin.alloc_tensor in: %1268, i0, c[1350], c[1483] dst: %1433
  call  layer_norm1      in: %1432, %242, %243, %1433 dst: %void
  call  vm.builtin.null_value in:              dst: %1432
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1350], c[1484] dst: %1434
  call  add21            in: %1433, %1299, %1434 dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[1356], c[1485] dst: %1435
  call  add22            in: %1405, %1311, %1435 dst: %void
  call  vm.builtin.alloc_tensor in: %335, i0, c[1387], c[1486] dst: %1436
  call  transpose24      in: %244, %1436  dst: %void
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1389], c[1487] dst: %1437
  call  matmul15         in: %1434, %1436, %1437 dst: %void
  call  vm.builtin.null_value in:              dst: %1434
  call  vm.builtin.null_value in:              dst: %1436
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1389], c[1488] dst: %1438
  call  add23            in: %1437, %245, %1438 dst: %void
  call  vm.builtin.null_value in:              dst: %1437
  call  vm.builtin.alloc_tensor in: %320, i0, c[1387], c[1489] dst: %1439
  call  transpose24      in: %246, %1439  dst: %void
  call  vm.builtin.alloc_tensor in: %335, i0, c[1393], c[1490] dst: %1440
  call  matmul16         in: %1435, %1439, %1440 dst: %void
  call  vm.builtin.null_value in:              dst: %1435
  call  vm.builtin.null_value in:              dst: %1439
  call  vm.builtin.alloc_tensor in: %320, i0, c[1393], c[1491] dst: %1441
  call  add24            in: %1440, %247, %1441 dst: %void
  call  vm.builtin.null_value in:              dst: %1440
  call  vm.builtin.alloc_tensor in: %335, i0, c[1387], c[1492] dst: %1442
  call  transpose24      in: %248, %1442  dst: %void
  call  vm.builtin.alloc_tensor in: %338, i0, c[1393], c[1493] dst: %1443
  call  matmul16         in: %1405, %1442, %1443 dst: %void
  call  vm.builtin.null_value in:              dst: %1442
  call  vm.builtin.alloc_tensor in: %335, i0, c[1393], c[1494] dst: %1444
  call  add24            in: %1443, %249, %1444 dst: %void
  call  vm.builtin.null_value in:              dst: %1443
  call  vm.builtin.reshape in: %1438, c[1399] dst: %1445
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1400], c[1495] dst: %1446
  call  transpose25      in: %1445, %1446 dst: %void
  call  vm.builtin.null_value in:              dst: %1438
  call  vm.builtin.null_value in:              dst: %1445
  call  vm.builtin.reshape in: %1441, c[1402] dst: %1447
  call  vm.builtin.alloc_tensor in: %338, i0, c[1403], c[1496] dst: %1448
  call  transpose26      in: %1447, %1448 dst: %void
  call  vm.builtin.null_value in:              dst: %1441
  call  vm.builtin.null_value in:              dst: %1447
  call  vm.builtin.reshape in: %1444, c[1402] dst: %1449
  call  vm.builtin.alloc_tensor in: %320, i0, c[1403], c[1497] dst: %1450
  call  transpose26      in: %1449, %1450 dst: %void
  call  vm.builtin.null_value in:              dst: %1444
  call  vm.builtin.null_value in:              dst: %1449
  call  vm.builtin.alloc_tensor in: %335, i0, c[1406], c[1498] dst: %1451
  call  transpose27      in: %1448, %1451 dst: %void
  call  vm.builtin.null_value in:              dst: %1448
  call  vm.builtin.alloc_tensor in: %338, i0, c[1408], c[1499] dst: %1452
  call  matmul17         in: %1446, %1451, %1452 dst: %void
  call  vm.builtin.null_value in:              dst: %1446
  call  vm.builtin.null_value in:              dst: %1451
  call  vm.builtin.alloc_tensor in: %335, i0, c[1408], c[1500] dst: %1453
  call  divide4          in: %1452, %1453 dst: %void
  call  vm.builtin.null_value in:              dst: %1452
  call  vm.builtin.alloc_tensor in: %338, i0, c[1408], c[1501] dst: %1454
  call  softmax3         in: %1453, %1454 dst: %void
  call  vm.builtin.null_value in:              dst: %1453
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1400], c[1502] dst: %1455
  call  matmul18         in: %1454, %1450, %1455 dst: %void
  call  vm.builtin.null_value in:              dst: %1454
  call  vm.builtin.null_value in:              dst: %1450
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1399], c[1503] dst: %1456
  call  transpose28      in: %1455, %1456 dst: %void
  call  vm.builtin.null_value in:              dst: %1455
  call  vm.builtin.reshape in: %1456, c[1389] dst: %1457
  call  vm.builtin.alloc_tensor in: %335, i0, c[1414], c[1504] dst: %1458
  call  transpose29      in: %250, %1458  dst: %void
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1350], c[1505] dst: %1459
  call  matmul19         in: %1457, %1458, %1459 dst: %void
  call  vm.builtin.null_value in:              dst: %1456
  call  vm.builtin.null_value in:              dst: %1457
  call  vm.builtin.null_value in:              dst: %1458
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1350], c[1506] dst: %1460
  call  add20            in: %1459, %251, %1460 dst: %void
  call  vm.builtin.null_value in:              dst: %1459
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1350], c[1507] dst: %1461
  call  add21            in: %1433, %1460, %1461 dst: %void
  call  vm.builtin.null_value in:              dst: %1433
  call  vm.builtin.null_value in:              dst: %1460
  call  vm.builtin.alloc_tensor in: %1268, i0, c[1350], c[1508] dst: %1462
  call  layer_norm1      in: %1461, %252, %253, %1462 dst: %void
  call  vm.builtin.null_value in:              dst: %1461
  call  vm.builtin.alloc_tensor in: %320, i0, c[1420], c[1509] dst: %1463
  call  transpose30      in: %254, %1463  dst: %void
  call  vm.builtin.alloc_tensor in: %331, i0, c[1422], c[1510] dst: %1464
  call  matmul20         in: %1462, %1463, %1464 dst: %void
  call  vm.builtin.null_value in:              dst: %1463
  call  vm.builtin.alloc_tensor in: %316, i0, c[1422], c[1511] dst: %1465
  call  add25            in: %1464, %255, %1465 dst: %void
  call  vm.builtin.null_value in:              dst: %1464
  call  vm.builtin.alloc_tensor in: %331, i0, c[1422], c[1512] dst: %1466
  call  relu             in: %1465, %1466 dst: %void
  call  vm.builtin.null_value in:              dst: %1465
  call  vm.builtin.alloc_tensor in: %335, i0, c[1426], c[1513] dst: %1467
  call  transpose31      in: %256, %1467  dst: %void
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1350], c[1514] dst: %1468
  call  matmul21         in: %1466, %1467, %1468 dst: %void
  call  vm.builtin.null_value in:              dst: %1466
  call  vm.builtin.null_value in:              dst: %1467
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1350], c[1515] dst: %1469
  call  add20            in: %1468, %257, %1469 dst: %void
  call  vm.builtin.null_value in:              dst: %1468
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1350], c[1516] dst: %1470
  call  add21            in: %1462, %1469, %1470 dst: %void
  call  vm.builtin.null_value in:              dst: %1462
  call  vm.builtin.null_value in:              dst: %1469
  call  vm.builtin.alloc_tensor in: %1268, i0, c[1350], c[1517] dst: %1471
  call  layer_norm1      in: %1470, %258, %259, %1471 dst: %void
  call  vm.builtin.null_value in:              dst: %1470
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1350], c[1518] dst: %1472
  call  add21            in: %1471, %1299, %1472 dst: %void
  call  vm.builtin.alloc_tensor in: %351, i0, c[1356], c[1519] dst: %1473
  call  add22            in: %1405, %1311, %1473 dst: %void
  call  vm.builtin.alloc_tensor in: %320, i0, c[1387], c[1520] dst: %1474
  call  transpose24      in: %262, %1474  dst: %void
  call  vm.builtin.alloc_tensor in: %335, i0, c[1393], c[1521] dst: %1475
  call  matmul16         in: %1473, %1474, %1475 dst: %void
  call  vm.builtin.null_value in:              dst: %1473
  call  vm.builtin.null_value in:              dst: %1474
  call  vm.builtin.alloc_tensor in: %320, i0, c[1393], c[1522] dst: %1476
  call  add24            in: %1475, %263, %1476 dst: %void
  call  vm.builtin.null_value in:              dst: %1475
  call  vm.builtin.alloc_tensor in: %335, i0, c[1387], c[1523] dst: %1477
  call  transpose24      in: %264, %1477  dst: %void
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1389], c[1524] dst: %1478
  call  matmul15         in: %1472, %1477, %1478 dst: %void
  call  vm.builtin.null_value in:              dst: %1472
  call  vm.builtin.null_value in:              dst: %1477
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1389], c[1525] dst: %1479
  call  add23            in: %1478, %265, %1479 dst: %void
  call  vm.builtin.null_value in:              dst: %1478
  call  vm.builtin.alloc_tensor in: %335, i0, c[1387], c[1526] dst: %1480
  call  transpose24      in: %266, %1480  dst: %void
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1389], c[1527] dst: %1481
  call  matmul15         in: %1471, %1480, %1481 dst: %void
  call  vm.builtin.null_value in:              dst: %1480
  call  vm.builtin.alloc_tensor in: %331, i0, c[1389], c[1528] dst: %1482
  call  add23            in: %1481, %267, %1482 dst: %void
  call  vm.builtin.null_value in:              dst: %1481
  call  vm.builtin.reshape in: %1476, c[1402] dst: %1483
  call  vm.builtin.alloc_tensor in: %335, i0, c[1403], c[1529] dst: %1484
  call  transpose26      in: %1483, %1484 dst: %void
  call  vm.builtin.null_value in:              dst: %1476
  call  vm.builtin.null_value in:              dst: %1483
  call  vm.builtin.reshape in: %1479, c[1399] dst: %1485
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1400], c[1530] dst: %1486
  call  transpose25      in: %1485, %1486 dst: %void
  call  vm.builtin.null_value in:              dst: %1479
  call  vm.builtin.null_value in:              dst: %1485
  call  vm.builtin.reshape in: %1482, c[1399] dst: %1487
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1400], c[1531] dst: %1488
  call  transpose25      in: %1487, %1488 dst: %void
  call  vm.builtin.null_value in:              dst: %1482
  call  vm.builtin.null_value in:              dst: %1487
  call  vm.builtin.alloc_tensor in: %331, i0, c[1447], c[1532] dst: %1489
  call  transpose32      in: %1486, %1489 dst: %void
  call  vm.builtin.null_value in:              dst: %1486
  call  vm.builtin.alloc_tensor in: %320, i0, c[1449], c[1533] dst: %1490
  call  matmul22         in: %1484, %1489, %1490 dst: %void
  call  vm.builtin.null_value in:              dst: %1484
  call  vm.builtin.null_value in:              dst: %1489
  call  vm.builtin.alloc_tensor in: %335, i0, c[1449], c[1534] dst: %1491
  call  divide5          in: %1490, %1491 dst: %void
  call  vm.builtin.null_value in:              dst: %1490
  call  vm.builtin.alloc_tensor in: %320, i0, c[1449], c[1535] dst: %1492
  call  softmax4         in: %1491, %1492 dst: %void
  call  vm.builtin.null_value in:              dst: %1491
  call  vm.builtin.alloc_tensor in: %335, i0, c[1403], c[1536] dst: %1493
  call  matmul23         in: %1492, %1488, %1493 dst: %void
  call  vm.builtin.null_value in:              dst: %1492
  call  vm.builtin.null_value in:              dst: %1488
  call  vm.builtin.alloc_tensor in: %320, i0, c[1402], c[1537] dst: %1494
  call  transpose33      in: %1493, %1494 dst: %void
  call  vm.builtin.null_value in:              dst: %1493
  call  vm.builtin.reshape in: %1494, c[1393] dst: %1495
  call  vm.builtin.alloc_tensor in: %335, i0, c[1414], c[1538] dst: %1496
  call  transpose29      in: %268, %1496  dst: %void
  call  vm.builtin.alloc_tensor in: %342, i0, c[1356], c[1539] dst: %1497
  call  matmul24         in: %1495, %1496, %1497 dst: %void
  call  vm.builtin.null_value in:              dst: %1494
  call  vm.builtin.null_value in:              dst: %1495
  call  vm.builtin.null_value in:              dst: %1496
  call  vm.builtin.alloc_tensor in: %349, i0, c[1356], c[1540] dst: %1498
  call  add26            in: %1497, %269, %1498 dst: %void
  call  vm.builtin.null_value in:              dst: %1497
  call  vm.builtin.alloc_tensor in: %346, i0, c[1356], c[1541] dst: %1499
  call  add22            in: %1405, %1498, %1499 dst: %void
  call  vm.builtin.null_value in:              dst: %1405
  call  vm.builtin.null_value in:              dst: %1498
  call  vm.builtin.alloc_tensor in: %351, i0, c[1356], c[1542] dst: %1500
  call  layer_norm2      in: %1499, %260, %261, %1500 dst: %void
  call  vm.builtin.null_value in:              dst: %1499
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1350], c[1543] dst: %1501
  call  add21            in: %1471, %1299, %1501 dst: %void
  call  vm.builtin.null_value in:              dst: %1298
  call  vm.builtin.null_value in:              dst: %1299
  call  vm.builtin.alloc_tensor in: %342, i0, c[1356], c[1544] dst: %1502
  call  add22            in: %1500, %1311, %1502 dst: %void
  call  vm.builtin.null_value in:              dst: %1310
  call  vm.builtin.null_value in:              dst: %1311
  call  vm.builtin.alloc_tensor in: %320, i0, c[1387], c[1545] dst: %1503
  call  transpose24      in: %270, %1503  dst: %void
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1389], c[1546] dst: %1504
  call  matmul15         in: %1501, %1503, %1504 dst: %void
  call  vm.builtin.null_value in:              dst: %1501
  call  vm.builtin.null_value in:              dst: %1503
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1389], c[1547] dst: %1505
  call  add23            in: %1504, %271, %1505 dst: %void
  call  vm.builtin.null_value in:              dst: %1504
  call  vm.builtin.alloc_tensor in: %335, i0, c[1387], c[1548] dst: %1506
  call  transpose24      in: %272, %1506  dst: %void
  call  vm.builtin.alloc_tensor in: %320, i0, c[1393], c[1549] dst: %1507
  call  matmul16         in: %1502, %1506, %1507 dst: %void
  call  vm.builtin.null_value in:              dst: %1502
  call  vm.builtin.null_value in:              dst: %1506
  call  vm.builtin.alloc_tensor in: %335, i0, c[1393], c[1550] dst: %1508
  call  add24            in: %1507, %273, %1508 dst: %void
  call  vm.builtin.null_value in:              dst: %1507
  call  vm.builtin.alloc_tensor in: %320, i0, c[1387], c[1551] dst: %1509
  call  transpose24      in: %274, %1509  dst: %void
  call  vm.builtin.alloc_tensor in: %338, i0, c[1393], c[1552] dst: %1510
  call  matmul16         in: %1500, %1509, %1510 dst: %void
  call  vm.builtin.null_value in:              dst: %1509
  call  vm.builtin.alloc_tensor in: %320, i0, c[1393], c[1553] dst: %1511
  call  add24            in: %1510, %275, %1511 dst: %void
  call  vm.builtin.null_value in:              dst: %1510
  call  vm.builtin.reshape in: %1505, c[1399] dst: %1512
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1400], c[1554] dst: %1513
  call  transpose25      in: %1512, %1513 dst: %void
  call  vm.builtin.null_value in:              dst: %1505
  call  vm.builtin.null_value in:              dst: %1512
  call  vm.builtin.reshape in: %1508, c[1402] dst: %1514
  call  vm.builtin.alloc_tensor in: %338, i0, c[1403], c[1555] dst: %1515
  call  transpose26      in: %1514, %1515 dst: %void
  call  vm.builtin.null_value in:              dst: %1508
  call  vm.builtin.null_value in:              dst: %1514
  call  vm.builtin.reshape in: %1511, c[1402] dst: %1516
  call  vm.builtin.alloc_tensor in: %335, i0, c[1403], c[1556] dst: %1517
  call  transpose26      in: %1516, %1517 dst: %void
  call  vm.builtin.null_value in:              dst: %1511
  call  vm.builtin.null_value in:              dst: %1516
  call  vm.builtin.alloc_tensor in: %320, i0, c[1406], c[1557] dst: %1518
  call  transpose27      in: %1515, %1518 dst: %void
  call  vm.builtin.null_value in:              dst: %1515
  call  vm.builtin.alloc_tensor in: %338, i0, c[1408], c[1558] dst: %1519
  call  matmul17         in: %1513, %1518, %1519 dst: %void
  call  vm.builtin.null_value in:              dst: %1513
  call  vm.builtin.null_value in:              dst: %1518
  call  vm.builtin.alloc_tensor in: %320, i0, c[1408], c[1559] dst: %1520
  call  divide4          in: %1519, %1520 dst: %void
  call  vm.builtin.null_value in:              dst: %1519
  call  vm.builtin.alloc_tensor in: %338, i0, c[1408], c[1560] dst: %1521
  call  softmax3         in: %1520, %1521 dst: %void
  call  vm.builtin.null_value in:              dst: %1520
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1400], c[1561] dst: %1522
  call  matmul18         in: %1521, %1517, %1522 dst: %void
  call  vm.builtin.null_value in:              dst: %1521
  call  vm.builtin.null_value in:              dst: %1517
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1399], c[1562] dst: %1523
  call  transpose28      in: %1522, %1523 dst: %void
  call  vm.builtin.null_value in:              dst: %1522
  call  vm.builtin.reshape in: %1523, c[1389] dst: %1524
  call  vm.builtin.alloc_tensor in: %320, i0, c[1414], c[1563] dst: %1525
  call  transpose29      in: %276, %1525  dst: %void
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1350], c[1564] dst: %1526
  call  matmul19         in: %1524, %1525, %1526 dst: %void
  call  vm.builtin.null_value in:              dst: %1523
  call  vm.builtin.null_value in:              dst: %1524
  call  vm.builtin.null_value in:              dst: %1525
  call  vm.builtin.alloc_tensor in: %1386, i0, c[1350], c[1565] dst: %1527
  call  add20            in: %1526, %277, %1527 dst: %void
  call  vm.builtin.null_value in:              dst: %1526
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1350], c[1566] dst: %1528
  call  add21            in: %1471, %1527, %1528 dst: %void
  call  vm.builtin.null_value in:              dst: %1471
  call  vm.builtin.null_value in:              dst: %1527
  call  vm.builtin.alloc_tensor in: %1268, i0, c[1350], c[1567] dst: %1529
  call  layer_norm3      in: %1528, %278, %279, %1529 dst: %void
  call  vm.builtin.null_value in:              dst: %1528
  call  vm.builtin.alloc_tensor in: %1386, i0, c[695], c[1568] dst: %1530
  call  take3            in: %1529, c[1306], %1530 dst: %void
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1569], c[1570] dst: %1531
  call  strided_slice3   in: %1529, %1531 dst: %void
  call  vm.builtin.null_value in:              dst: %1529
  call  vm.builtin.alloc_tensor in: %340, i0, c[1571], c[1572] dst: %1532
  call  transpose34      in: %1500, %1532 dst: %void
  call  vm.builtin.null_value in:              dst: %1500
  call  vm.builtin.reshape in: %1532, c[615] dst: %1533
  call  vm.builtin.alloc_tensor in: %349, i0, c[1573], c[1574] dst: %1534
  call  conv2d_transpose in: %1533, %280, %1534 dst: %void
  call  vm.builtin.null_value in:              dst: %1532
  call  vm.builtin.null_value in:              dst: %1533
  call  vm.builtin.alloc_tensor in: %318, i0, c[1575], c[1576] dst: %1535
  call  mean1            in: %1534, %1535 dst: %void
  call  vm.builtin.alloc_tensor in: %346, i0, c[1573], c[1577] dst: %1536
  call  subtract6        in: %1534, %1535, %1536 dst: %void
  call  vm.builtin.null_value in:              dst: %1534
  call  vm.builtin.null_value in:              dst: %1535
  call  vm.builtin.alloc_tensor in: %333, i0, c[1573], c[1578] dst: %1537
  call  power1           in: %1536, %1537 dst: %void
  call  vm.builtin.alloc_tensor in: %318, i0, c[1575], c[1579] dst: %1538
  call  mean1            in: %1537, %1538 dst: %void
  call  vm.builtin.null_value in:              dst: %1537
  call  vm.builtin.alloc_tensor in: %316, i0, c[1575], c[1580] dst: %1539
  call  add27            in: %1538, %1539 dst: %void
  call  vm.builtin.null_value in:              dst: %1538
  call  vm.builtin.alloc_tensor in: %318, i0, c[1575], c[1581] dst: %1540
  call  tir_sqrt1        in: %1539, %1540 dst: %void
  call  vm.builtin.null_value in:              dst: %1539
  call  vm.builtin.alloc_tensor in: %342, i0, c[1573], c[1582] dst: %1541
  call  divide6          in: %1536, %1540, %1541 dst: %void
  call  vm.builtin.null_value in:              dst: %1536
  call  vm.builtin.null_value in:              dst: %1540
  call  vm.builtin.reshape in: %284, c[178] dst: %1542
  call  vm.builtin.reshape in: %1542, c[1583] dst: %1543
  call  vm.builtin.null_value in:              dst: %1542
  call  vm.builtin.reshape in: %285, c[178] dst: %1544
  call  vm.builtin.reshape in: %1544, c[1583] dst: %1545
  call  vm.builtin.null_value in:              dst: %1544
  call  vm.builtin.alloc_tensor in: %351, i0, c[1573], c[1584] dst: %1546
  call  multiply10       in: %1543, %1541, %1546 dst: %void
  call  vm.builtin.null_value in:              dst: %1543
  call  vm.builtin.null_value in:              dst: %1541
  call  vm.builtin.alloc_tensor in: %340, i0, c[1573], c[1585] dst: %1547
  call  add28            in: %1546, %1545, %1547 dst: %void
  call  vm.builtin.null_value in:              dst: %1545
  call  vm.builtin.null_value in:              dst: %1546
  call  vm.builtin.alloc_tensor in: %349, i0, c[1573], c[1586] dst: %1548
  call  gelu1            in: %1547, %1548 dst: %void
  call  vm.builtin.null_value in:              dst: %1547
  call  vm.builtin.alloc_tensor in: %333, i0, c[1587], c[1588] dst: %1549
  call  conv2d_transpose1 in: %1548, %282, %1549 dst: %void
  call  vm.builtin.null_value in:              dst: %1548
  call  vm.builtin.alloc_tensor in: %346, i0, c[1587], c[1589] dst: %1550
  call  gelu2            in: %1549, %1550 dst: %void
  call  vm.builtin.null_value in:              dst: %1549
  call  vm.builtin.alloc_tensor in: %1268, i0, c[695], c[1590] dst: %1551
  call  take4            in: %1531, c[1306], %1551 dst: %void
  call  vm.builtin.alloc_tensor in: %335, i0, c[1358], c[1591] dst: %1552
  call  transpose20      in: %286, %1552  dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[658], i0, c[1592], c[4] dst: %1553
  call  vm.builtin.alloc_tensor in: %1553, i0, c[695], c[1593] dst: %1554
  call  matmul25         in: %1551, %1552, %1554 dst: %void
  call  vm.builtin.null_value in:              dst: %1551
  call  vm.builtin.null_value in:              dst: %1552
  call  vm.builtin.alloc_tensor in: %1268, i0, c[695], c[1594] dst: %1555
  call  add29            in: %1554, %287, %1555 dst: %void
  call  vm.builtin.null_value in:              dst: %1554
  call  vm.builtin.alloc_tensor in: %1553, i0, c[695], c[1595] dst: %1556
  call  relu1            in: %1555, %1556 dst: %void
  call  vm.builtin.null_value in:              dst: %1555
  call  vm.builtin.alloc_tensor in: %320, i0, c[1358], c[1596] dst: %1557
  call  transpose20      in: %290, %1557  dst: %void
  call  vm.builtin.alloc_tensor in: %1268, i0, c[695], c[1597] dst: %1558
  call  matmul25         in: %1556, %1557, %1558 dst: %void
  call  vm.builtin.null_value in:              dst: %1556
  call  vm.builtin.null_value in:              dst: %1557
  call  vm.builtin.alloc_tensor in: %1553, i0, c[695], c[1598] dst: %1559
  call  add29            in: %1558, %291, %1559 dst: %void
  call  vm.builtin.null_value in:              dst: %1558
  call  vm.builtin.alloc_tensor in: %1268, i0, c[695], c[1599] dst: %1560
  call  relu1            in: %1559, %1560 dst: %void
  call  vm.builtin.null_value in:              dst: %1559
  call  vm.builtin.alloc_tensor in: %331, i0, c[1600], c[1601] dst: %1561
  call  transpose35      in: %288, %1561  dst: %void
  call  vm.builtin.alloc_tensor in: %1553, i0, c[1602], c[1603] dst: %1562
  call  matmul26         in: %1560, %1561, %1562 dst: %void
  call  vm.builtin.null_value in:              dst: %1560
  call  vm.builtin.null_value in:              dst: %1561
  call  vm.builtin.alloc_tensor in: %1257, i0, c[1602], c[1604] dst: %1563
  call  add30            in: %1562, %289, %1563 dst: %void
  call  vm.builtin.null_value in:              dst: %1562
  call  vm.builtin.alloc_tensor in: %1553, i0, c[695], c[1605] dst: %1564
  call  take4            in: %1531, c[1606], %1564 dst: %void
  call  vm.builtin.alloc_tensor in: %335, i0, c[1358], c[1607] dst: %1565
  call  transpose20      in: %292, %1565  dst: %void
  call  vm.builtin.alloc_tensor in: %1268, i0, c[695], c[1608] dst: %1566
  call  matmul25         in: %1564, %1565, %1566 dst: %void
  call  vm.builtin.null_value in:              dst: %1564
  call  vm.builtin.null_value in:              dst: %1565
  call  vm.builtin.alloc_tensor in: %1553, i0, c[695], c[1609] dst: %1567
  call  add29            in: %1566, %293, %1567 dst: %void
  call  vm.builtin.null_value in:              dst: %1566
  call  vm.builtin.alloc_tensor in: %1268, i0, c[695], c[1610] dst: %1568
  call  relu1            in: %1567, %1568 dst: %void
  call  vm.builtin.null_value in:              dst: %1567
  call  vm.builtin.alloc_tensor in: %320, i0, c[1358], c[1611] dst: %1569
  call  transpose20      in: %296, %1569  dst: %void
  call  vm.builtin.alloc_tensor in: %1553, i0, c[695], c[1612] dst: %1570
  call  matmul25         in: %1568, %1569, %1570 dst: %void
  call  vm.builtin.null_value in:              dst: %1568
  call  vm.builtin.null_value in:              dst: %1569
  call  vm.builtin.alloc_tensor in: %1268, i0, c[695], c[1613] dst: %1571
  call  add29            in: %1570, %297, %1571 dst: %void
  call  vm.builtin.null_value in:              dst: %1570
  call  vm.builtin.alloc_tensor in: %1553, i0, c[695], c[1614] dst: %1572
  call  relu1            in: %1571, %1572 dst: %void
  call  vm.builtin.null_value in:              dst: %1571
  call  vm.builtin.alloc_tensor in: %331, i0, c[1600], c[1615] dst: %1573
  call  transpose35      in: %294, %1573  dst: %void
  call  vm.builtin.alloc_tensor in: %1251, i0, c[1602], c[1616] dst: %1574
  call  matmul26         in: %1572, %1573, %1574 dst: %void
  call  vm.builtin.null_value in:              dst: %1572
  call  vm.builtin.null_value in:              dst: %1573
  call  vm.builtin.alloc_tensor in: %1553, i0, c[1602], c[1617] dst: %1575
  call  add30            in: %1574, %295, %1575 dst: %void
  call  vm.builtin.null_value in:              dst: %1574
  call  vm.builtin.alloc_tensor in: %1268, i0, c[695], c[1618] dst: %1576
  call  take4            in: %1531, c[1619], %1576 dst: %void
  call  vm.builtin.alloc_tensor in: %335, i0, c[1358], c[1620] dst: %1577
  call  transpose20      in: %298, %1577  dst: %void
  call  vm.builtin.alloc_tensor in: %1251, i0, c[695], c[1621] dst: %1578
  call  matmul25         in: %1576, %1577, %1578 dst: %void
  call  vm.builtin.null_value in:              dst: %1576
  call  vm.builtin.null_value in:              dst: %1577
  call  vm.builtin.alloc_tensor in: %1268, i0, c[695], c[1622] dst: %1579
  call  add29            in: %1578, %299, %1579 dst: %void
  call  vm.builtin.null_value in:              dst: %1578
  call  vm.builtin.alloc_tensor in: %1251, i0, c[695], c[1623] dst: %1580
  call  relu1            in: %1579, %1580 dst: %void
  call  vm.builtin.null_value in:              dst: %1579
  call  vm.builtin.alloc_tensor in: %320, i0, c[1358], c[1624] dst: %1581
  call  transpose20      in: %302, %1581  dst: %void
  call  vm.builtin.alloc_tensor in: %1268, i0, c[695], c[1625] dst: %1582
  call  matmul25         in: %1580, %1581, %1582 dst: %void
  call  vm.builtin.null_value in:              dst: %1580
  call  vm.builtin.null_value in:              dst: %1581
  call  vm.builtin.alloc_tensor in: %1251, i0, c[695], c[1626] dst: %1583
  call  add29            in: %1582, %303, %1583 dst: %void
  call  vm.builtin.null_value in:              dst: %1582
  call  vm.builtin.alloc_tensor in: %1268, i0, c[695], c[1627] dst: %1584
  call  relu1            in: %1583, %1584 dst: %void
  call  vm.builtin.null_value in:              dst: %1583
  call  vm.builtin.alloc_tensor in: %331, i0, c[1600], c[1628] dst: %1585
  call  transpose35      in: %300, %1585  dst: %void
  call  vm.builtin.alloc_tensor in: %1251, i0, c[1602], c[1629] dst: %1586
  call  matmul26         in: %1584, %1585, %1586 dst: %void
  call  vm.builtin.null_value in:              dst: %1584
  call  vm.builtin.null_value in:              dst: %1585
  call  vm.builtin.alloc_tensor in: %1246, i0, c[1602], c[1630] dst: %1587
  call  add30            in: %1586, %301, %1587 dst: %void
  call  vm.builtin.null_value in:              dst: %1586
  call  vm.builtin.alloc_tensor in: %1251, i0, c[695], c[1631] dst: %1588
  call  take4            in: %1531, c[1632], %1588 dst: %void
  call  vm.builtin.null_value in:              dst: %1531
  call  vm.builtin.alloc_tensor in: %335, i0, c[1358], c[1633] dst: %1589
  call  transpose20      in: %304, %1589  dst: %void
  call  vm.builtin.alloc_tensor in: %1268, i0, c[695], c[1634] dst: %1590
  call  matmul25         in: %1588, %1589, %1590 dst: %void
  call  vm.builtin.null_value in:              dst: %1588
  call  vm.builtin.null_value in:              dst: %1589
  call  vm.builtin.alloc_tensor in: %1251, i0, c[695], c[1635] dst: %1591
  call  add29            in: %1590, %305, %1591 dst: %void
  call  vm.builtin.null_value in:              dst: %1590
  call  vm.builtin.alloc_tensor in: %1271, i0, c[695], c[1636] dst: %1592
  call  relu1            in: %1591, %1592 dst: %void
  call  vm.builtin.null_value in:              dst: %1591
  call  vm.builtin.alloc_tensor in: %320, i0, c[1358], c[1637] dst: %1593
  call  transpose20      in: %308, %1593  dst: %void
  call  vm.builtin.alloc_tensor in: %1251, i0, c[695], c[1638] dst: %1594
  call  matmul25         in: %1592, %1593, %1594 dst: %void
  call  vm.builtin.null_value in:              dst: %1592
  call  vm.builtin.null_value in:              dst: %1593
  call  vm.builtin.alloc_tensor in: %1268, i0, c[695], c[1639] dst: %1595
  call  add29            in: %1594, %309, %1595 dst: %void
  call  vm.builtin.null_value in:              dst: %1594
  call  vm.builtin.alloc_tensor in: %1251, i0, c[695], c[1640] dst: %1596
  call  relu1            in: %1595, %1596 dst: %void
  call  vm.builtin.null_value in:              dst: %1595
  call  vm.builtin.alloc_tensor in: %331, i0, c[1600], c[1641] dst: %1597
  call  transpose35      in: %306, %1597  dst: %void
  call  vm.builtin.alloc_storage in: %vm, c[647], i0, c[1642], c[4] dst: %1598
  call  vm.builtin.alloc_tensor in: %1598, i0, c[1602], c[1643] dst: %1599
  call  matmul26         in: %1596, %1597, %1599 dst: %void
  call  vm.builtin.null_value in:              dst: %1596
  call  vm.builtin.null_value in:              dst: %1597
  call  vm.builtin.alloc_tensor in: %1251, i0, c[1602], c[1644] dst: %1600
  call  add30            in: %1599, %307, %1600 dst: %void
  call  vm.builtin.null_value in:              dst: %1599
  call  vm.builtin.reshape in: %1563, c[1645] dst: %1601
  call  vm.builtin.reshape in: %1575, c[1645] dst: %1602
  call  vm.builtin.reshape in: %1587, c[1645] dst: %1603
  call  vm.builtin.reshape in: %1600, c[1645] dst: %1604
  call  vm.builtin.alloc_tensor in: %1271, i0, c[1646], c[1647] dst: %1605
  call  concatenate7     in: %1601, %1602, %1603, %1604, %1605 dst: %void
  call  vm.builtin.null_value in:              dst: %1563
  call  vm.builtin.null_value in:              dst: %1601
  call  vm.builtin.null_value in:              dst: %1575
  call  vm.builtin.null_value in:              dst: %1602
  call  vm.builtin.null_value in:              dst: %1587
  call  vm.builtin.null_value in:              dst: %1603
  call  vm.builtin.null_value in:              dst: %1600
  call  vm.builtin.null_value in:              dst: %1604
  call  vm.builtin.reshape in: %1550, c[1648] dst: %1606
  call  vm.builtin.alloc_tensor in: %335, i0, c[1649], c[1650] dst: %1607
  call  matmul27         in: %1605, %1606, %1607 dst: %void
  call  vm.builtin.null_value in:              dst: %1605
  call  vm.builtin.null_value in:              dst: %1550
  call  vm.builtin.null_value in:              dst: %1606
  call  vm.builtin.reshape in: %1607, c[1651] dst: %1608
  call  vm.builtin.alloc_tensor in: %320, i0, c[1358], c[1652] dst: %1609
  call  transpose20      in: %310, %1609  dst: %void
  call  vm.builtin.alloc_tensor in: %1553, i0, c[695], c[1653] dst: %1610
  call  matmul25         in: %1530, %1609, %1610 dst: %void
  call  vm.builtin.null_value in:              dst: %1530
  call  vm.builtin.null_value in:              dst: %1609
  call  vm.builtin.alloc_tensor in: %1251, i0, c[695], c[1654] dst: %1611
  call  add29            in: %1610, %311, %1611 dst: %void
  call  vm.builtin.null_value in:              dst: %1610
  call  vm.builtin.alloc_tensor in: %1553, i0, c[695], c[1655] dst: %1612
  call  relu1            in: %1611, %1612 dst: %void
  call  vm.builtin.null_value in:              dst: %1611
  call  vm.builtin.alloc_tensor in: %320, i0, c[1358], c[1656] dst: %1613
  call  transpose20      in: %314, %1613  dst: %void
  call  vm.builtin.alloc_tensor in: %1251, i0, c[695], c[1657] dst: %1614
  call  matmul25         in: %1612, %1613, %1614 dst: %void
  call  vm.builtin.null_value in:              dst: %1612
  call  vm.builtin.null_value in:              dst: %1613
  call  vm.builtin.alloc_tensor in: %1553, i0, c[695], c[1658] dst: %1615
  call  add29            in: %1614, %315, %1615 dst: %void
  call  vm.builtin.null_value in:              dst: %1614
  call  vm.builtin.alloc_tensor in: %1251, i0, c[695], c[1659] dst: %1616
  call  relu1            in: %1615, %1616 dst: %void
  call  vm.builtin.null_value in:              dst: %1615
  call  vm.builtin.alloc_tensor in: %1268, i0, c[1660], c[1661] dst: %1617
  call  transpose36      in: %312, %1617  dst: %void
  call  vm.builtin.alloc_tensor in: %1598, i0, c[1662], c[1663] dst: %1618
  call  matmul28         in: %1616, %1617, %1618 dst: %void
  call  vm.builtin.null_value in:              dst: %1616
  call  vm.builtin.null_value in:              dst: %1617
  call  vm.builtin.alloc_tensor in: %1257, i0, c[1662], c[1664] dst: %1619
  call  add31            in: %1618, %313, %1619 dst: %void
  call  vm.builtin.null_value in:              dst: %1618
  call  vm.builtin.alloc_storage in: %vm, c[1665], i0, c[1666], c[4] dst: %1620
  call  vm.builtin.alloc_tensor in: %1620, i0, c[1667], c[1668] dst: %1621
  call  vm.builtin.null_value in:              dst: %1620
  call  strided_slice4   in: %1608, %1621 dst: %void
  call  vm.builtin.null_value in:              dst: %1607
  call  vm.builtin.null_value in:              dst: %1608
  call  vm.builtin.alloc_storage in: %vm, c[1669], i0, c[1670], c[4] dst: %1622
  call  vm.builtin.alloc_tensor in: %1622, i0, c[1671], c[1672] dst: %1623
  call  vm.builtin.null_value in:              dst: %1622
  call  strided_slice5   in: %1619, %1623 dst: %void
  call  vm.builtin.null_value in:              dst: %1619
  call  vm.builtin.make_tuple in: %1623, %1621 dst: %1624
  call  vm.builtin.make_tuple in: %2           dst: %1625
  call  vm.builtin.make_tuple in: %1624, %1625 dst: %1626
  call  vm.builtin.null_value in:              dst: %1621
  call  vm.builtin.null_value in:              dst: %1623
  call  vm.builtin.null_value in:              dst: %316
  call  vm.builtin.null_value in:              dst: %318
  call  vm.builtin.null_value in:              dst: %320
  call  vm.builtin.null_value in:              dst: %331
  call  vm.builtin.null_value in:              dst: %333
  call  vm.builtin.null_value in:              dst: %335
  call  vm.builtin.null_value in:              dst: %338
  call  vm.builtin.null_value in:              dst: %340
  call  vm.builtin.null_value in:              dst: %342
  call  vm.builtin.null_value in:              dst: %346
  call  vm.builtin.null_value in:              dst: %349
  call  vm.builtin.null_value in:              dst: %351
  call  vm.builtin.null_value in:              dst: %367
  call  vm.builtin.null_value in:              dst: %384
  call  vm.builtin.null_value in:              dst: %386
  call  vm.builtin.null_value in:              dst: %425
  call  vm.builtin.null_value in:              dst: %500
  call  vm.builtin.null_value in:              dst: %532
  call  vm.builtin.null_value in:              dst: %534
  call  vm.builtin.null_value in:              dst: %1246
  call  vm.builtin.null_value in:              dst: %1248
  call  vm.builtin.null_value in:              dst: %1251
  call  vm.builtin.null_value in:              dst: %1253
  call  vm.builtin.null_value in:              dst: %1255
  call  vm.builtin.null_value in:              dst: %1257
  call  vm.builtin.null_value in:              dst: %1268
  call  vm.builtin.null_value in:              dst: %1271
  call  vm.builtin.null_value in:              dst: %1276
  call  vm.builtin.null_value in:              dst: %1279
  call  vm.builtin.null_value in:              dst: %1386
  call  vm.builtin.null_value in:              dst: %1553
  call  vm.builtin.null_value in:              dst: %1598
  ret   %1626

@ones2 packed_func;

@cumsum packed_func;

@subtract4 packed_func;

@cumsum1 packed_func;

@divide2 packed_func;

@concatenate4 packed_func;

@add18 packed_func;

@subtract5 packed_func;

@matmul11 packed_func;

@multiply9 packed_func;

@tir_sin1 packed_func;

@tir_cos1 packed_func;

@concatenate5 packed_func;

@transpose18 packed_func;

@take2 packed_func;

@concatenate6 packed_func;

@add19 packed_func;

@transpose19 packed_func;

@transpose20 packed_func;

@matmul12 packed_func;

@add20 packed_func;

@transpose21 packed_func;

@transpose22 packed_func;

@matmul13 packed_func;

@divide3 packed_func;

@softmax2 packed_func;

@matmul14 packed_func;

@transpose23 packed_func;

@layer_norm1 packed_func;

@add21 packed_func;

@add22 packed_func;

@transpose24 packed_func;

@matmul15 packed_func;

@add23 packed_func;

@matmul16 packed_func;

@add24 packed_func;

@transpose25 packed_func;

@transpose26 packed_func;

@transpose27 packed_func;

@matmul17 packed_func;

@divide4 packed_func;

@softmax3 packed_func;

@matmul18 packed_func;

@transpose28 packed_func;

@transpose29 packed_func;

@matmul19 packed_func;

@transpose30 packed_func;

@matmul20 packed_func;

@add25 packed_func;

@relu packed_func;

@transpose31 packed_func;

@matmul21 packed_func;

@transpose32 packed_func;

@matmul22 packed_func;

@divide5 packed_func;

@softmax4 packed_func;

@matmul23 packed_func;

@transpose33 packed_func;

@matmul24 packed_func;

@add26 packed_func;

@layer_norm2 packed_func;

@layer_norm3 packed_func;

@take3 packed_func;

@strided_slice3 packed_func;

@transpose34 packed_func;

@conv2d_transpose packed_func;

@mean1 packed_func;

@subtract6 packed_func;

@power1 packed_func;

@add27 packed_func;

@tir_sqrt1 packed_func;

@divide6 packed_func;

@multiply10 packed_func;

@add28 packed_func;

@gelu1 packed_func;

@conv2d_transpose1 packed_func;

@gelu2 packed_func;

@take4 packed_func;

@matmul25 packed_func;

@add29 packed_func;

@relu1 packed_func;

@transpose35 packed_func;

@matmul26 packed_func;

@add30 packed_func;

@concatenate7 packed_func;

@matmul27 packed_func;

@transpose36 packed_func;

@matmul28 packed_func;

@add31 packed_func;

@strided_slice4 packed_func;

@strided_slice5 packed_func;

@_initialize_effect:
  call  vm.builtin.make_tuple in: %void        dst: %0
  call  vm.builtin.null_value in:              dst: %void
  ret   %0


