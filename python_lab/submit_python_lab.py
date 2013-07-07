########                                     ######## 
# Hi there, curious student.                        #
#                                                   #
# This submission script runs some tests on your    #
# code and then uploads it to Coursera for grading. #
#                                                   #
# Changing anything in this script might cause your #
# submissions to fail.                              #
########                                     ########

import io, os, sys, doctest, traceback, importlib, urllib.request, urllib.parse, urllib.error, base64, hashlib, random, ast

URL               = 'matrix-001'
partFriendlyNames = ['Minutes in a Week', 'Remainder', 'Divisibility', 'Assign y', 'Squares Comprehension', 'Powers of 2 Comprehension', 'Nine Element Set', 'Five Element Set', 'Base 10 Three Digit Numbers', 'Intersection of Sets', 'Average', 'Sum of Three Lists', 'Cartesian-Product Lists', 'Three Element Tuples', 'Remove (0,0,0)', 'First Element', 'List and Set Differences', 'Odd Numbers', 'Range and Zip', 'Zip Sum', 'Generate Dictionary', 'Modify Missing Key', 'Range Squared', 'Identity', 'List Integers', 'Names to Salaries', 'Next Ints', 'Cubes', 'dict2list', 'list2dict']
groups            = [[('fFZfuj5BSf0z9vju', 'Minutes in a Week', '>>> print(test_format(minutes_in_week))\n')], [('RCTi7BRCbNnUGLrE', 'Remainder', '>>> print(test_format(remainder_without_mod))\n>>> print(test_format(line_contains_substr("remainder_without_mod", "%")))\n')], [('3ngJR6j6I6xGkMb6', 'Divisibility', '>>> print(test_format(divisible_by_3))\n')], [('SqKKP5oqXdJNQR54', 'Assign y', '>>> print(test_format(statement_val))\n')], [('LUxaUjsmC7dF6lFR', 'Squares Comprehension', '>>> print(test_format(first_five_squares))\n>>> print(test_format(use_comprehension("first_five_squares")))\n')], [('OO0ctDZZKI72zUu7', 'Powers of 2 Comprehension', '>>> print(test_format(first_five_pows_two))\n>>> print(test_format(use_comprehension("first_five_pows_two")))\n')], [('6jcpLOvzpLmsTSVm', 'Nine Element Set', '>>> nine_elements_set = {x*y for x in X1 for y in Y1}\n>>> print(test_format(len(nine_elements_set)))\n>>> print(test_format(len(X1)))\n>>> print(test_format(len(Y1)))\n')], [('Yc7Syvika5HHSjWY', 'Five Element Set', '>>> five_elements_set = {x*y for x in X2 for y in Y2}\n>>> print(test_format(len(five_elements_set)))\n>>> print(test_format(len(X2)))\n>>> print(test_format(len(Y2)))\n>>> print(test_format(len(X2 & Y2)))\n')], [('q4059GW7SFmhlnuV', 'Base 10 Three Digit Numbers', '>>> digits = {0,1,2,3,4,5,6,7,8,9}\n>>> base = 10\n>>> print(test_format(three_digits_set == set(range(1000))))\n>>> print(test_format(use_comprehension("three_digits_set")))\n>>> print(test_format(line_contains_substr("three_digits_set", "base")))\n')], [('apLtHTyCikXLtyrF', 'Intersection of Sets', '>>> print(test_format(S_intersect_T))\n>>> print(test_format(use_comprehension("S_intersect_T")))\n')], [('FnRTEV9wumMHDSRk', 'Average', '>>> print(test_format(L_average))\n')], [('xvF1K4mjiljgnWFv', 'Sum of Three Lists', '>>> print(test_format(LofL_sum))\n>>> print(test_format(use_comprehension("LofL_sum")))\n')], [('cXHf573AUNrEoFxH', 'Cartesian-Product Lists', '>>> print(test_format(set(map(tuple, cartesian_product))))\n>>> print(test_format(use_comprehension("cartesian_product")))\n')], [('Y4tuZGBVfLcQt8lN', 'Three Element Tuples', '>>> print(test_format(zero_sum_list == [(0, 0, 0), (0, 2, -2), (0, -2, 2), (1, 1, -2), (1, -2, 1), (2, 0, -2), (2, 2, -4), (2, -4, 2), (2, -2, 0), (-4, 2, 2), (-2, 0, 2), (-2, 1, 1), (-2, 2, 0)]))\n>>> print(test_format(use_comprehension("zero_sum_list")))\n')], [('S8w9l4cmOKXbgCfe', 'Remove (0,0,0)', '>>> print(test_format(exclude_zero_list))\n>>> print(test_format(use_comprehension("exclude_zero_list")))\n')], [('Qnq4vQ5vW6mORoqE', 'First Element', '>>> print(test_format(first_of_tuples_list == (0,0,0)))\n>>> print(test_format(len(first_of_tuples_list)))\n>>> print(test_format(sum(first_of_tuples_list)))\n>>> print(test_format(use_comprehension("first_of_tuples_list")))\n')], [('yoiJUxauMefcohSi', 'List and Set Differences', '>>> print(test_format(len(L1) == len(list(set(L1))) ))\n>>> L2_new = list(set(L2)) \n>>> print(test_format(len(L2) == len(L2_new)))\n>>> print(test_format(L2 == L2_new))\n')], [('3I5KzAun0uzowUp4', 'Odd Numbers', '>>> print(test_format(odd_num_list_range))\n>>> print(test_format(use_comprehension("odd_num_list_range")))\n')], [('D8ygxQYLerbhMhMX', 'Range and Zip', '>>> print(test_format(range_and_zip))\n>>> print(test_format(use_comprehension("range_and_zip")))\n')], [('klnmJrHwxgXXLTYT', 'Zip Sum', '>>> print(test_format(list_sum_zip))\n>>> print(test_format(use_comprehension("list_sum_zip")))\n')], [('FdPpEhCqyxB5Bt8S', 'Generate Dictionary', '>>> print(test_format(set(value_list)))\n>>> print(test_format(use_comprehension("value_list")))\n')], [('14cqsN8TvrYGNLVu', 'Modify Missing Key', '>>> print(test_format(use_comprehension("value_list_modified_1")))\n>>> print(test_format(use_comprehension("value_list_modified_2")))\n>>> print(test_format(value_list_modified_1))\n>>> print(test_format(value_list_modified_2))\n')], [('C5kNoKaPB4ApgbT7', 'Range Squared', '>>> print(test_format(square_dict == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400, 21: 441, 22: 484, 23: 529, 24: 576, 25: 625, 26: 676, 27: 729, 28: 784, 29: 841, 30: 900, 31: 961, 32: 1024, 33: 1089, 34: 1156, 35: 1225, 36: 1296, 37: 1369, 38: 1444, 39: 1521, 40: 1600, 41: 1681, 42: 1764, 43: 1849, 44: 1936, 45: 2025, 46: 2116, 47: 2209, 48: 2304, 49: 2401, 50: 2500, 51: 2601, 52: 2704, 53: 2809, 54: 2916, 55: 3025, 56: 3136, 57: 3249, 58: 3364, 59: 3481, 60: 3600, 61: 3721, 62: 3844, 63: 3969, 64: 4096, 65: 4225, 66: 4356, 67: 4489, 68: 4624, 69: 4761, 70: 4900, 71: 5041, 72: 5184, 73: 5329, 74: 5476, 75: 5625, 76: 5776, 77: 5929, 78: 6084, 79: 6241, 80: 6400, 81: 6561, 82: 6724, 83: 6889, 84: 7056, 85: 7225, 86: 7396, 87: 7569, 88: 7744, 89: 7921, 90: 8100, 91: 8281, 92: 8464, 93: 8649, 94: 8836, 95: 9025, 96: 9216, 97: 9409, 98: 9604, 99: 9801}))\n>>> print(test_format(use_comprehension("square_dict")))\n')], [('tShbyCCphwno07CP', 'Identity', '>>> print(test_format(identity_dict))\n>>> print(test_format(use_comprehension("identity_dict")))\n')], [('pRtDJVxpnw3d5lFi', 'List Integers', '>>> print(test_format(representation_dict[135]))\n>>> print(test_format(representation_dict[291]))\n>>> print(test_format(use_comprehension("representation_dict")))\n>>> print(test_format(line_contains_substr("representation_dict", "base")))\n')], [('lZLRqgDYLYKTNaEx', 'Names to Salaries', '>>> print(test_format(listdict2dict))\n>>> print(test_format(use_comprehension("listdict2dict")))\n')], [('tGNwBWZTFRhlJgVe', 'Next Ints', '>>> print(test_format(nextInts([1, 5, 7])))\n>>> print(test_format(nextInts([0, 0, 0, 0, 0])))\n>>> print(test_format(nextInts([570, 968, 723, 179, 762, 377, 845, 320, 475, 952, 680, 874, 708, 493, 901, 896, 164, 165, 404, 147, 917, 936, 205, 615, 518, 254, 856, 584, 287, 336, 452, 551, 914, 706, 558, 842, 52, 593, 733, 398, 119, 874, 769, 585, 572, 261, 440, 404, 293, 176, 575, 224, 647, 241, 319, 974, 5, 373, 367, 609, 661, 691, 47, 64, 79, 744, 606, 205, 424, 88, 648, 419, 165, 399, 594, 760, 348, 638, 385, 754, 491, 284, 531, 258, 745, 634, 51, 557, 346, 577, 375, 979, 773, 523, 441, 952, 50, 534, 641, 621, 813, 511, 279, 565, 228, 86, 187, 395, 261, 287, 717, 989, 614, 92, 8, 229, 372, 378, 53, 350, 936, 654, 74, 750, 20, 978, 506, 793, 148, 944, 23, 962, 996, 586, 404, 216, 148, 284, 797, 805, 501, 161, 64, 608, 287, 127, 136, 902, 879, 433, 553, 366, 155, 763, 728, 117, 300, 990, 345, 982, 767, 279, 814, 516, 342, 291, 410, 612, 961, 445, 472, 507, 251, 832, 737, 62, 384, 273, 352, 752, 455, 216, 731, 7, 868, 111, 42, 190, 841, 283, 215, 860, 628, 835, 145, 97, 337, 57, 791, 443, 271, 925, 666, 452, 601, 571, 218, 901, 479, 75, 912, 708, 33, 575, 252, 753, 857, 150, 625, 852, 921, 178, 832, 126, 929, 16, 427, 533, 119, 256, 937, 107, 740, 607, 801, 827, 667, 776, 95, 940, 66, 982, 930, 825, 878, 512, 961, 701, 657, 584, 204, 348, 564, 505, 303, 562, 399, 415, 784, 588, 2, 729, 478, 396, 314, 130, 493, 947, 724, 540, 608, 431, 107, 497, 68, 791, 521, 583, 359, 221, 713, 683, 945, 274, 568, 666, 517, 241, 401, 437, 958, 572, 561, 929, 342, 149, 971, 762, 249, 538, 277, 761, 489, 728, 372, 131, 366, 702, 73, 382, 58, 223, 423, 642, 628, 6, 158, 946, 710, 232, 211, 747, 215, 579, 396, 521, 597, 966, 401, 749, 546, 310, 786, 691, 333, 817, 162, 961, 674, 132, 235, 481, 410, 477, 311, 932, 352, 64, 771, 837, 609, 654, 535, 530, 346, 294, 441, 532, 824, 422, 912, 99, 894, 246, 99, 111, 806, 360, 652, 753, 489, 735, 996, 8, 742, 793, 341, 498, 790, 402, 542, 892, 573, 78, 994, 676, 225, 675, 904, 196, 156, 819, 959, 501, 554, 381, 525, 608, 401, 937, 875, 373, 803, 258, 530, 901, 175, 656, 533, 91, 304, 497, 321, 906, 893, 995, 238, 51, 419, 70, 673, 479, 852, 864, 143, 224, 911, 207, 41, 603, 824, 764, 257, 653, 521, 28, 673, 333, 536, 748, 92, 98, 951, 655, 278, 437, 167, 253, 849, 343, 554, 313, 333, 556, 919, 636, 21, 841, 854, 550, 993, 291, 324, 224, 48, 927, 784, 387, 276, 652, 860, 100, 386, 153, 988, 805, 419, 75, 365, 920, 957, 23, 592, 280, 814, 800, 154, 776, 169, 635, 379, 919, 742, 145, 784, 201, 711, 209, 36, 317, 718, 84, 974, 768, 518, 884, 374, 447, 160, 295, 29, 23, 421, 384, 104, 123, 40, 945, 765, 32, 243, 696, 603, 129, 650, 957, 659, 863, 582, 165, 681, 33, 738, 917, 410, 803, 821, 636, 162, 662, 231, 75, 799, 591, 258, 722, 131, 805, 600, 704, 995, 793, 502, 624, 656, 43, 597, 353, 867, 116, 568, 26, 16, 251, 78, 764, 799, 287, 575, 190, 718, 619, 377, 465, 267, 688, 772, 359, 451, 459, 139, 71, 821, 312, 334, 988, 929, 797, 830, 26, 3, 90, 450, 715, 174, 910, 258, 229, 325, 517, 37, 260, 950, 20, 881, 156, 231, 114, 670, 287, 631, 982, 855, 841, 72, 561, 368, 289, 829, 428, 815, 207, 844, 68, 143, 707, 259, 669, 362, 943, 550, 133, 367, 900, 233, 109, 504, 803, 985, 333, 318, 680, 952, 408, 268, 890, 101, 423, 261, 641, 500, 389, 885, 76, 682, 811, 941, 142, 552, 401, 429, 973, 287, 472, 630, 383, 569, 630, 135, 823, 49, 507, 433, 550, 660, 403, 88, 879, 697, 571, 790, 896, 252, 172, 911, 485, 30, 657, 821, 412, 204, 801, 763, 329, 199, 315, 940, 515, 29, 22, 66, 221, 63, 678, 368, 545, 560, 301, 292, 987, 673, 573, 399, 148, 326, 418, 687, 85, 167, 774, 657, 754, 168, 113, 412, 353, 234, 923, 720, 691, 319, 711, 1000, 188, 969, 123, 547, 127, 69, 782, 533, 898, 574, 214, 848, 599, 112, 833, 26, 750, 462, 480, 511, 644, 929, 725, 310, 41, 559, 961, 399, 527, 960, 352, 468, 755, 732, 944, 115, 408, 642, 888, 922, 780, 727, 459, 473, 122, 716, 908, 576, 498, 196, 647, 912, 275, 238, 79, 75, 427, 299, 470, 347, 792, 969, 21, 424, 596, 88, 98, 475, 917, 683, 47, 843, 742, 673, 702, 983, 996, 430, 53, 327, 769, 666, 453, 93, 498, 942, 299, 200, 968, 202, 193, 508, 706, 247, 51, 721, 327, 484, 855, 565, 777, 33, 816, 827, 36, 962, 235, 297, 666, 111, 453, 445, 111, 653, 690, 325, 36, 187, 633, 854, 829, 74, 840, 744, 375, 124, 694, 236, 222, 88, 449, 134, 542, 812, 325, 373, 975, 131, 78, 390, 114, 969, 633, 57, 110, 635, 396, 947, 913, 148, 215, 465, 72, 463, 830, 885, 532, 728, 701, 31, 541, 54, 411, 916, 268, 596, 72, 971, 907, 856, 65, 55, 108, 222, 24, 482, 150, 864, 768, 332, 40, 961, 80, 745, 984, 170, 424, 28, 442, 146, 724, 32, 786, 985, 386, 326, 840, 416, 931, 606, 746, 39, 295, 355, 80, 663, 463, 716, 849, 606, 83, 512, 144, 854, 384, 976, 675, 549, 318, 893, 193, 562, 419, 444, 427, 612, 362, 567, 529, 273, 807, 381, 120, 66, 397, 738, 948, 99, 427, 560, 916, 283, 722, 111, 740, 156, 942, 215, 67, 944, 161, 544, 597, 468, 441, 483, 961, 503, 162, 706, 57, 37, 307, 142, 537, 861, 944])    ))\n>>> print(test_format(use_comprehension("nextInts")))\n')], [('gbXfwMbLBL6ySr10', 'Cubes', '>>> print(test_format(cubes([0, 0, 0, 0])))\n>>> print(test_format(cubes([4, 5, 6])))\n>>> print(test_format(cubes([0.5, 1.5, 2.5, 3.5])))\n>>> print(test_format(cubes([768, 275, 645, 106, 332, 836, 109, 268, 721, 711, 642, 393, 671, 263, 480, 211, 819, 735, 797, 394, 625, 199, 308, 937, 552, 435, 70, 316, 987, 188, 291, 387, 844, 939, 781, 329, 484, 678, 223, 598, 135, 717, 444, 650, 40, 740, 799, 315, 933, 321, 81, 410, 512, 651, 471, 867, 910, 769, 657, 588, 769, 174, 347, 759, 222, 904, 248, 547, 158, 254, 966, 47, 980, 948, 461, 234, 266, 976, 105, 125, 468, 612, 468, 521, 828, 93, 562, 135, 751, 160, 159, 812, 212, 553, 456, 704, 683, 849, 529, 795])))\n>>> print(test_format(use_comprehension("cubes")))\n')], [('HikXLgYM3rySDfdy', 'dict2list', '>>> dct1 = {}\n>>> keylist1 = []\n>>> print(test_format(dict2list(dct1, keylist1)))\n>>> dct2 = {\'a\':\'A\', \'b\':\'B\', \'c\':\'C\'}\n>>> keylist2 = [\'b\',\'c\',\'a\']\n>>> print(test_format(dict2list(dct2, keylist2)))\n>>> dct3 = {3: 395, 8: 816, 9: 370, 10: 102, 11: 746, 18: 477, 20: 284, 26: 783, 27: 55, 35: 108, 43: 621, 45: 225, 46: 56, 51: 503, 54: 24, 55: 742, 62: 491, 64: 317, 66: 739, 70: 972, 71: 372, 74: 312, 76: 826, 77: 215, 78: 507, 80: 970, 87: 966, 90: 798, 91: 353, 94: 358, 101: 880, 102: 730, 105: 514, 106: 867, 108: 723, 117: 412, 120: 870, 124: 511, 126: 904, 127: 196, 128: 758, 130: 89, 131: 631, 133: 45, 137: 345, 138: 246, 139: 141, 142: 963, 143: 583, 146: 626, 148: 615, 149: 581, 150: 889, 154: 662, 155: 993, 157: 765, 158: 7, 160: 67, 162: 862, 172: 212, 174: 493, 175: 676, 176: 915, 177: 220, 179: 7, 180: 362, 186: 586, 191: 632, 194: 755, 196: 537, 198: 398, 201: 330, 202: 337, 207: 767, 212: 41, 214: 341, 223: 84, 224: 651, 226: 898, 227: 926, 231: 801, 232: 751, 235: 216, 236: 234, 238: 445, 243: 534, 244: 81, 246: 860, 248: 478, 249: 659, 250: 107, 254: 609, 255: 488, 256: 108, 257: 497, 260: 649, 264: 684, 267: 964, 268: 294, 269: 327, 271: 621, 276: 713, 278: 195, 281: 559, 283: 858, 287: 931, 289: 89, 293: 850, 294: 277, 295: 537, 298: 430, 301: 244, 302: 950, 305: 594, 306: 98, 307: 438, 308: 564, 310: 643, 311: 363, 314: 109, 315: 295, 316: 604, 317: 268, 324: 166, 331: 853, 336: 123, 346: 46, 348: 186, 349: 404, 350: 426, 352: 34, 353: 741, 355: 385, 356: 115, 357: 613, 366: 369, 367: 513, 369: 36, 370: 755, 375: 77, 377: 780, 378: 57, 380: 123, 381: 914, 384: 575, 386: 866, 387: 377, 389: 915, 393: 36, 398: 895, 399: 215, 404: 317, 406: 711, 411: 490, 412: 752, 413: 879, 414: 344, 417: 723, 419: 431, 421: 279, 422: 518, 425: 346, 427: 992, 429: 758, 433: 48, 435: 66, 436: 349, 437: 429, 438: 616, 439: 186, 449: 917, 452: 807, 457: 916, 458: 548, 459: 601, 463: 891, 464: 897, 465: 404, 467: 241, 469: 510, 471: 66, 472: 688, 473: 797, 475: 252, 476: 408, 479: 79, 484: 307, 485: 462, 494: 492, 497: 841, 499: 200, 501: 451, 502: 494, 504: 754, 505: 56, 506: 234, 507: 849, 509: 984, 511: 902, 512: 156, 516: 721, 517: 905, 518: 728, 521: 505, 523: 29, 534: 256, 537: 179, 539: 820, 540: 199, 543: 358, 545: 626, 547: 21, 549: 456, 550: 447, 553: 316, 559: 997, 560: 513, 561: 171, 563: 231, 565: 913, 573: 330, 575: 697, 579: 682, 581: 92, 584: 65, 590: 393, 591: 258, 592: 0, 593: 978, 597: 407, 598: 497, 599: 420, 601: 13, 603: 460, 611: 710, 614: 228, 623: 837, 626: 98, 629: 363, 630: 510, 634: 339, 635: 625, 637: 787, 639: 774, 642: 401, 643: 187, 644: 35, 646: 183, 647: 872, 651: 901, 652: 399, 654: 635, 659: 762, 660: 358, 661: 537, 664: 639, 665: 49, 672: 121, 675: 909, 676: 369, 679: 901, 680: 409, 685: 694, 688: 979, 690: 604, 692: 212, 695: 856, 696: 722, 697: 493, 699: 340, 700: 706, 701: 549, 702: 129, 708: 222, 709: 433, 710: 872, 711: 874, 713: 197, 714: 109, 715: 463, 716: 47, 717: 5, 718: 639, 719: 900, 722: 467, 723: 785, 725: 993, 726: 89, 727: 428, 729: 47, 731: 178, 732: 74, 735: 82, 736: 68, 737: 953, 739: 490, 740: 399, 744: 489, 747: 83, 751: 178, 756: 982, 758: 343, 759: 346, 762: 600, 775: 424, 776: 669, 781: 214, 785: 438, 789: 616, 790: 852, 791: 444, 795: 671, 796: 909, 797: 331, 798: 534, 800: 782, 803: 570, 804: 638, 807: 535, 808: 852, 809: 424, 812: 75, 816: 303, 818: 730, 824: 501, 827: 138, 828: 700, 829: 475, 834: 858, 844: 814, 846: 269, 848: 258, 851: 144, 856: 585, 857: 427, 858: 136, 862: 59, 864: 981, 868: 591, 870: 754, 871: 778, 874: 77, 875: 809, 877: 198, 878: 712, 880: 699, 881: 978, 882: 301, 883: 51, 885: 453, 888: 881, 889: 758, 890: 786, 891: 329, 893: 280, 894: 594, 897: 410, 898: 567, 901: 764, 902: 528, 904: 191, 909: 664, 911: 582, 912: 945, 915: 1000, 917: 818, 922: 165, 924: 111, 925: 624, 928: 215, 930: 304, 931: 625, 933: 621, 935: 625, 937: 685, 938: 477, 939: 857, 940: 471, 941: 720, 944: 516, 945: 27, 947: 216, 948: 926, 950: 78, 954: 391, 957: 260, 958: 461, 961: 415, 962: 374, 965: 516, 968: 832, 970: 121, 975: 181, 984: 834, 987: 517, 988: 752, 989: 241, 993: 7, 997: 523}\n>>> keylist3 = [3, 8, 9, 10, 11, 18, 20, 26, 27, 35, 43, 45, 46, 51, 54, 55, 62, 64, 66, 70, 71, 74, 76, 77, 78, 80, 87, 90, 91, 94, 101, 102, 105, 106, 108, 117, 120, 124, 126, 127, 128, 130, 131, 133, 137, 138, 139, 142, 143, 146, 148, 149, 150, 154, 155, 157, 158, 160, 162, 172, 174, 175, 176, 177, 179, 180, 186, 191, 194, 196, 198, 201, 202, 207, 212, 214, 223, 224, 226, 227, 231, 232, 235, 236, 238, 243, 244, 246, 248, 249, 250, 254, 255, 256, 257, 260, 264, 267, 268, 269, 271, 276, 278, 281, 283, 287, 289, 293, 294, 295, 298, 301, 302, 305, 306, 307, 308, 310, 311, 314, 315, 316, 317, 324, 331, 336, 346, 348, 349, 350, 352, 353, 355, 356, 357, 366, 367, 369, 370, 375, 377, 378, 380, 381, 384, 386, 387, 389, 393, 398, 399, 404, 406, 411, 412, 413, 414, 417, 419, 421, 422, 425, 427, 429, 433, 435, 436, 437, 438, 439, 449, 452, 457, 458, 459, 463, 464, 465, 467, 469, 471, 472, 473, 475, 476, 479, 484, 485, 494, 497, 499, 501, 502, 504, 505, 506, 507, 509, 511, 512, 516, 517, 518, 521, 523, 534, 537, 539, 540, 543, 545, 547, 549, 550, 553, 559, 560, 561, 563, 565, 573, 575, 579, 581, 584, 590, 591, 592, 593, 597, 598, 599, 601, 603, 611, 614, 623, 626, 629, 630, 634, 635, 637, 639, 642, 643, 644, 646, 647, 651, 652, 654, 659, 660, 661, 664, 665, 672, 675, 676, 679, 680, 685, 688, 690, 692, 695, 696, 697, 699, 700, 701, 702, 708, 709, 710, 711, 713, 714, 715, 716, 717, 718, 719, 722, 723, 725, 726, 727, 729, 731, 732, 735, 736, 737, 739, 740, 744, 747, 751, 756, 758, 759, 762, 775, 776, 781, 785, 789, 790, 791, 795, 796, 797, 798, 800, 803, 804, 807, 808, 809, 812, 816, 818, 824, 827, 828, 829, 834, 844, 846, 848, 851, 856, 857, 858, 862, 864, 868, 870, 871, 874, 875, 877, 878, 880, 881, 882, 883, 885, 888, 889, 890, 891, 893, 894, 897, 898, 901, 902, 904, 909, 911, 912, 915, 917, 922, 924, 925, 928, 930, 931, 933, 935, 937, 938, 939, 940, 941, 944, 945, 947, 948, 950, 954, 957, 958, 961, 962, 965, 968, 970, 975, 984, 987, 988, 989, 993, 997]\n>>> print(test_format(dict2list(dct3, keylist3)))\n>>> print(test_format(use_comprehension("dict2list")))\n')], [('SgCJwpfcAVel9YfA', 'list2dict', '>>> L1 = []\n>>> keylist1 = []\n>>> print(test_format(list2dict(L1, keylist1)))\n>>> L2 =[\'A\',\'B\',\'C\']\n>>> keylist2 = [\'a\',\'b\',\'c\']\n>>> print(test_format(list2dict(L2, keylist2)))\n>>> L3 = [395, 816, 370, 102, 746, 477, 284, 783, 55, 108, 621, 225, 56, 503, 24, 742, 491, 317, 739, 972, 372, 312, 826, 215, 507, 970, 966, 798, 353, 358, 880, 730, 514, 867, 723, 412, 870, 511, 904, 196, 758, 89, 631, 45, 345, 246, 141, 963, 583, 626, 615, 581, 889, 662, 993, 765, 7, 67, 862, 212, 493, 676, 915, 220, 7, 362, 586, 632, 755, 537, 398, 330, 337, 767, 41, 341, 84, 651, 898, 926, 801, 751, 216, 234, 445, 534, 81, 860, 478, 659, 107, 609, 488, 108, 497, 649, 684, 964, 294, 327, 621, 713, 195, 559, 858, 931, 89, 850, 277, 537, 430, 244, 950, 594, 98, 438, 564, 643, 363, 109, 295, 604, 268, 166, 853, 123, 46, 186, 404, 426, 34, 741, 385, 115, 613, 369, 513, 36, 755, 77, 780, 57, 123, 914, 575, 866, 377, 915, 36, 895, 215, 317, 711, 490, 752, 879, 344, 723, 431, 279, 518, 346, 992, 758, 48, 66, 349, 429, 616, 186, 917, 807, 916, 548, 601, 891, 897, 404, 241, 510, 66, 688, 797, 252, 408, 79, 307, 462, 492, 841, 200, 451, 494, 754, 56, 234, 849, 984, 902, 156, 721, 905, 728, 505, 29, 256, 179, 820, 199, 358, 626, 21, 456, 447, 316, 997, 513, 171, 231, 913, 330, 697, 682, 92, 65, 393, 258, 0, 978, 407, 497, 420, 13, 460, 710, 228, 837, 98, 363, 510, 339, 625, 787, 774, 401, 187, 35, 183, 872, 901, 399, 635, 762, 358, 537, 639, 49, 121, 909, 369, 901, 409, 694, 979, 604, 212, 856, 722, 493, 340, 706, 549, 129, 222, 433, 872, 874, 197, 109, 463, 47, 5, 639, 900, 467, 785, 993, 89, 428, 47, 178, 74, 82, 68, 953, 490, 399, 489, 83, 178, 982, 343, 346, 600, 424, 669, 214, 438, 616, 852, 444, 671, 909, 331, 534, 782, 570, 638, 535, 852, 424, 75, 303, 730, 501, 138, 700, 475, 858, 814, 269, 258, 144, 585, 427, 136, 59, 981, 591, 754, 778, 77, 809, 198, 712, 699, 978, 301, 51, 453, 881, 758, 786, 329, 280, 594, 410, 567, 764, 528, 191, 664, 582, 945, 1000, 818, 165, 111, 624, 215, 304, 625, 621, 625, 685, 477, 857, 471, 720, 516, 27, 216, 926, 78, 391, 260, 461, 415, 374, 516, 832, 121, 181, 834, 517, 752, 241, 7, 523]\n>>> keylist3 = [3, 8, 9, 10, 11, 18, 20, 26, 27, 35, 43, 45, 46, 51, 54, 55, 62, 64, 66, 70, 71, 74, 76, 77, 78, 80, 87, 90, 91, 94, 101, 102, 105, 106, 108, 117, 120, 124, 126, 127, 128, 130, 131, 133, 137, 138, 139, 142, 143, 146, 148, 149, 150, 154, 155, 157, 158, 160, 162, 172, 174, 175, 176, 177, 179, 180, 186, 191, 194, 196, 198, 201, 202, 207, 212, 214, 223, 224, 226, 227, 231, 232, 235, 236, 238, 243, 244, 246, 248, 249, 250, 254, 255, 256, 257, 260, 264, 267, 268, 269, 271, 276, 278, 281, 283, 287, 289, 293, 294, 295, 298, 301, 302, 305, 306, 307, 308, 310, 311, 314, 315, 316, 317, 324, 331, 336, 346, 348, 349, 350, 352, 353, 355, 356, 357, 366, 367, 369, 370, 375, 377, 378, 380, 381, 384, 386, 387, 389, 393, 398, 399, 404, 406, 411, 412, 413, 414, 417, 419, 421, 422, 425, 427, 429, 433, 435, 436, 437, 438, 439, 449, 452, 457, 458, 459, 463, 464, 465, 467, 469, 471, 472, 473, 475, 476, 479, 484, 485, 494, 497, 499, 501, 502, 504, 505, 506, 507, 509, 511, 512, 516, 517, 518, 521, 523, 534, 537, 539, 540, 543, 545, 547, 549, 550, 553, 559, 560, 561, 563, 565, 573, 575, 579, 581, 584, 590, 591, 592, 593, 597, 598, 599, 601, 603, 611, 614, 623, 626, 629, 630, 634, 635, 637, 639, 642, 643, 644, 646, 647, 651, 652, 654, 659, 660, 661, 664, 665, 672, 675, 676, 679, 680, 685, 688, 690, 692, 695, 696, 697, 699, 700, 701, 702, 708, 709, 710, 711, 713, 714, 715, 716, 717, 718, 719, 722, 723, 725, 726, 727, 729, 731, 732, 735, 736, 737, 739, 740, 744, 747, 751, 756, 758, 759, 762, 775, 776, 781, 785, 789, 790, 791, 795, 796, 797, 798, 800, 803, 804, 807, 808, 809, 812, 816, 818, 824, 827, 828, 829, 834, 844, 846, 848, 851, 856, 857, 858, 862, 864, 868, 870, 871, 874, 875, 877, 878, 880, 881, 882, 883, 885, 888, 889, 890, 891, 893, 894, 897, 898, 901, 902, 904, 909, 911, 912, 915, 917, 922, 924, 925, 928, 930, 931, 933, 935, 937, 938, 939, 940, 941, 944, 945, 947, 948, 950, 954, 957, 958, 961, 962, 965, 968, 970, 975, 984, 987, 988, 989, 993, 997]\n>>> print(test_format(list2dict(L3, keylist3)))\n>>> print(test_format(use_comprehension("dict2list")))\n')]]
sourceFiles       = ['python_lab.py'] * len(sum(groups,[]))

try:
    import python_lab as solution
    test_vars = vars(solution).copy()
except Exception as exc:
    print(exc)
    print("!! It seems like you have an error in your stencil file. Please fix before submitting.")
    sys.exit(1)

def find_lines(varname):
    return list(filter(lambda l: varname in l, list(open("python_lab.py"))))

def find_line(varname):
    ls = find_lines(varname)
    return ls[0] if len(ls) else None


def use_comprehension(varname):
    lines = find_lines(varname)
    for line in lines:
        try:
            if "comprehension" in ast.dump(ast.parse(line)):
                return True
        except: pass
    return False

def double_comprehension(varname):
    line = find_line(varname)
    return ast.dump(ast.parse(line)).count("comprehension") == 2

def line_contains_substr(varname, word):
    lines = find_line(varname)
    for line in lines:
        if word in line:
            return True
    return False

def test_format(obj, precision=6):
    tf = lambda o: test_format(o, precision)
    delimit = lambda o: ', '.join(o)
    otype = type(obj)
    if otype is str:
        return "'%s'" % obj
    elif otype is float:
        fstr = '%%.%dg' % precision
        return fstr % obj
    elif otype is set:
        return '{%s}' % delimit(sorted(map(tf, obj)))
    elif otype is dict:
        return '{%s}' % delimit(sorted(tf(k)+': '+tf(v) for k,v in obj.items()))
    elif otype is list:
        return '[%s]' % delimit(map(tf, obj))
    elif otype is tuple:
        return '(%s%s)' % (delimit(map(tf, obj)), ',' if len(obj) is 1 else '')
    elif otype.__name__ in ['Vec','Mat']:
        entries = delimit(map(tf, sorted(filter(lambda o: o[1] != 0, obj.f.items()))))
        return '<%s %s {%s}>' % (otype.__name__, test_format(obj.D), entries)
    else:
        return str(obj)



def output(tests):
    dtst = doctest.DocTestParser().get_doctest(tests, test_vars, 0, '<string>', 0)
    runner = ModifiedDocTestRunner()
    runner.run(dtst)
    return ''.join(map(str.rstrip, runner.results))

test_vars['test_format'] = test_vars['tf'] = test_format
test_vars['find_lines'] = find_lines
test_vars['find_line'] = find_line
test_vars['use_comprehension'] = use_comprehension
test_vars['double_comprehension'] = double_comprehension
test_vars['line_contains_substr'] = line_contains_substr


class ModifiedDocTestRunner(doctest.DocTestRunner):
    def __init__(self, *args, **kwargs):
        self.results = []
        return super(ModifiedDocTestRunner, self).__init__(*args, checker=OutputAccepter(), **kwargs)
    
    def report_success(self, out, test, example, got):
        self.results.append(got)
    
    def report_unexpected_exception(self, out, test, example, exc_info):
        exf = traceback.format_exception_only(exc_info[0], exc_info[1])[-1]
        self.results.append(exf)

class OutputAccepter(doctest.OutputChecker):
    def check_output(self, want, got, optionflags):
        return True

challenge_url = 'https://class.coursera.org/%s/assignment/challenge' % URL
submit_url    = 'https://class.coursera.org/%s/assignment/submit'    % URL

def submit():   
    print('==\n== Submitting Solutions \n==\n')
    
    (login, password) = loginPrompt()
    if not login:
        print('!! Submission Cancelled')
        return
    
    print('\n== Connecting to Coursera ... \n')

    parts = partPrompt()
    if parts is None: return

    while len(parts) == 0:
        print('\n!! Cannot submit ungraded parts')
        parts = partPrompt()

    for (sid, name, part_tests) in parts:
        print('\n== Submitting "%s" \n' % name)

        if 'DEV' in os.environ: sid += '-dev'

        (login, ch, state, ch_aux) = getChallenge(login, sid)

        if (not login) or (not ch) or (not state):
            print('\n!! Error: %s\n' % login)
            return

        # to stop Coursera's strip() from doing anything, we surround in parens
        prog_out = '(%s)' % output(part_tests) 
        token    = challengeResponse(login, password, ch)
        src      = source(sid)

        if 'DEBUG' in os.environ: print('==== Output: %s' % prog_out.replace('\n','\\n'))
        
        feedback = submitSolution(login, token, sid, prog_out, src, state, ch_aux)

        if len(feedback.strip()) > 0:
            print('==== Feedback: %s\n' % feedback.strip())


def loginPrompt():
    """Prompt the user for login credentials. Returns a tuple (login, password)."""
    if 'COURSERA_EMAIL' in os.environ:
        login = os.environ['COURSERA_EMAIL']
    else:
        login = input('Login email address: ')

    if 'COURSERA_PASS' in os.environ:
        password = os.environ['COURSERA_PASS']
    else:
        password = input("One-time password from the assignment page (NOT your own account\'s password): ")
    return login, password

def partPrompt():
    print('These are the assignment parts that you can submit:\n')

    for i, name in enumerate(filter(lambda n: len(n), partFriendlyNames)):
        print('  %d) %s' % (i+1, name))

    def extract_range(s):
        s = s.split('-')
        if len(s) == 1: return [int(s[0])]
        else: return list(range(int(s[0]), 1+int(s[1])))

    their_input = input('\nWhich parts do you want to submit? (Ex: 1, 4-7): ')
    parts = map(extract_range, their_input.split(','))
    flat_parts = sum(parts, [])
    return sum(list(map(lambda p: groups[p-1], flat_parts)),[])

def getChallenge(email, sid):
    """Gets the challenge salt from the server. Returns (email,ch,state,ch_aux)."""
    values = {'email_address' : email,
              'assignment_part_sid' : sid,
              'response_encoding' : 'delim'
             }
  
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(challenge_url, data)
    response = urllib.request.urlopen(req)
    text = response.readall().decode('utf-8').strip()
  
    # text is of the form email|ch|signature
    splits = text.split('|')
    if len(splits) != 9:
        print('Badly formatted challenge response: %s' % text)
        sys.exit(1)
    return (splits[2], splits[4], splits[6], splits[8])

def challengeResponse(email, passwd, challenge):
    sha1 = hashlib.sha1()
    sha1.update(('%s%s' % (challenge, passwd)).encode('utf-8'))
    return ''.join(sha1.hexdigest())


def submitSolution(email_address, ch_resp, sid, output, source, state, ch_aux):
    """Submits a solution to the server. Returns (result, string)."""

    source_64 = str(base64.encodebytes(source.encode('utf-8')), 'ascii')
    output_64 = str(base64.encodebytes(output.encode('utf-8')), 'ascii')

    values = { 'assignment_part_sid' : sid,
               'email_address'       : email_address,
               'submission'          : output_64,
               'submission_aux'      : source_64,
               'challenge_response'  : ch_resp,
               'state'               : state
             }

    data     = urllib.parse.urlencode(values).encode('utf-8')
    req      = urllib.request.Request(submit_url, data)
    response = urllib.request.urlopen(req)
    string   = response.readall().decode('utf-8').strip()

    return string

def source(sid):
    """ This collects the source code, for logging purposes. """
    f = open(sourceFiles[0])
    src = f.read() 
    f.close()
    return src

if __name__ == '__main__':
    submit()
