# version code 893
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

URL                 = 'matrix-001'
part_friendly_names = ['Computing Matrix Vector Products', 'Reflexive Vector Matrix Multiplication', '[z+x, y, x] Matrix Vector Multiplication', '[2x, 4y, 3z] Matrix Vector Multiplication', 'Matrix Multiplication: Dimension of Matrices', 'Small Matrix Multiplication', 'AB and BA Matrix Multiplication', 'Repeated Matrix Multiplication', 'Matrix Multiplication by Sparse Matrices', 'Column Vector and Row Vector Matrix Multiplications', 'linear-combinations matrix-vector multiply', 'linear-combinations vector-matrix multiply', 'dot-product matrix-vector multiply', 'dot-product vector-matrix multiply', 'Matrix-vector matrix-matrix multiply', 'Vector-matrix matrix-matrix multiply', 'Dot-product matrix-matrix multiply', 'Solving Linear Systems', 'Matrix Inverse Criterion']
groups              = [[('cQ3p1gJm23kyNFfut92oDfNa7wPXp8Wz', 'Computing Matrix Vector Products, Part 1', '>>> print(test_format(vector_matrix_product_1))\n'), ('cQ3p1gJm23kyNFfuqEk5ldDFBxmfpwoQ', 'Computing Matrix Vector Products, Part 2', '>>> print(test_format(vector_matrix_product_2))\n'), ('cQ3p1gJm23kyNFfukGySxDBtatyGHbnm', 'Computing Matrix Vector Products, Part 3', '>>> print(test_format(vector_matrix_product_3))\n')], [('cQ3p1gJm23kyNFfuH7yzeEHG0zmOYwXV', 'Reflexive Vector Matrix Multiplication', '>>> print(test_format(M_swap_two_vector))\n')], [('cQ3p1gJm23kyNFfuOSyFYwoG3jMxvZpa', '[z+x, y, x] Matrix Vector Multiplication', '>>> print(test_format(three_by_three_matrix))\n')], [('cQ3p1gJm23kyNFfuaGsQByzVTzCU48oQ', '[2x, 4y, 3z] Matrix Vector Multiplication', '>>> print(test_format(multiplied_matrix))\n')], [('cQ3p1gJm23kyNFfuN9ffK3gkHKsWSJSo', 'Matrix Multiplication: Dimension of Matrices', '>>> print(test_format(part_1_valid))\n>>> print(test_format(part_1_number_rows))\n>>> print(test_format(part_1_number_cols))\n>>> print(test_format(part_2_valid))\n>>> print(test_format(part_2_number_rows))\n>>> print(test_format(part_2_number_cols))\n>>> print(test_format(part_3_valid))\n>>> print(test_format(part_3_number_rows))\n>>> print(test_format(part_3_number_cols))\n>>> print(test_format(part_4_valid))\n>>> print(test_format(part_4_number_rows))\n>>> print(test_format(part_4_number_cols))\n>>> print(test_format(part_5_valid))\n>>> print(test_format(part_5_number_rows))\n>>> print(test_format(part_5_number_cols))\n>>> print(test_format(part_6_valid))\n>>> print(test_format(part_6_number_rows))\n>>> print(test_format(part_6_number_cols))\n>>> print(test_format(part_7_valid))\n>>> print(test_format(part_7_number_rows))\n>>> print(test_format(part_7_number_cols))\n')], [('cQ3p1gJm23kyNFfuQRlJ2zFPBsrpn2y4', 'Small Matrix Multiplication', '>>> print(test_format(small_mat_mult_1))\n>>> print(test_format(small_mat_mult_2))\n>>> print(test_format(small_mat_mult_3))\n>>> print(test_format(small_mat_mult_4))\n>>> print(test_format(small_mat_mult_5))\n>>> print(test_format(small_mat_mult_6))\n')], [('cQ3p1gJm23kyNFfu34xtpNCI4aSi0H92', 'AB and BA Matrix Multiplication', '>>> print(test_format(part_1_AB))\n>>> print(test_format(part_1_BA))\n>>> print(test_format(part_2_AB))\n>>> print(test_format(part_2_BA))\n>>> print(test_format(part_3_AB))\n>>> print(test_format(part_3_BA))\n')], [('cQ3p1gJm23kyNFfuCbXwETX5EPu1amSk', 'Repeated Matrix Multiplication, Part 1', '>>> print(test_format(matrix_matrix_mult_1))\n'), ('cQ3p1gJm23kyNFfur0QEhAHcT0fD2ZgZ', 'Repeated Matrix Multiplication, Part 2', '>>> print(test_format(matrix_matrix_mult_2_A2))\n'), ('cQ3p1gJm23kyNFfuEUrUBUN8m6DY4GU8', 'Repeated Matrix Multiplication, Part 3', '>>> print(test_format(matrix_matrix_mult_2_A3))\n'), ('cQ3p1gJm23kyNFfuJvSfUTVQ8KREPa6k', 'Repeated Matrix Multiplication, Part 4', '>>> print(test_format(matrix_matrix_mult_2_An))\n')], [('cQ3p1gJm23kyNFfuMVLfqHStz752FZQW', 'Matrix Multiplication by Sparse Matrices, Part 1', '>>> print(test_format(your_answer_a_AB))\n'), ('cQ3p1gJm23kyNFfualqDBR1EpEXP765g', 'Matrix Multiplication by Sparse Matrices, Part 2', '>>> print(test_format(your_answer_a_BA))\n'), ('cQ3p1gJm23kyNFfuFv5j9o0ayaDzZy9g', 'Matrix Multiplication by Sparse Matrices, Part 3', '>>> print(test_format(your_answer_b_AB))\n'), ('cQ3p1gJm23kyNFfuAaeYiiaKUpjlkvPA', 'Matrix Multiplication by Sparse Matrices, Part 4', '>>> print(test_format(your_answer_b_BA))\n'), ('cQ3p1gJm23kyNFfuM5nymKqcf4tkYnMQ', 'Matrix Multiplication by Sparse Matrices, Part 5', '>>> print(test_format(your_answer_c_AB))\n'), ('cQ3p1gJm23kyNFfuCUIMrlwYvCZVfI7k', 'Matrix Multiplication by Sparse Matrices, Part 6', '>>> print(test_format(your_answer_c_BA))\n'), ('cQ3p1gJm23kyNFfuCV4ORCyZ4R1LrW1M', 'Matrix Multiplication by Sparse Matrices, Part 7', '>>> print(test_format(your_answer_d_AB))\n'), ('cQ3p1gJm23kyNFfuC9TMkdu8ATDSn21X', 'Matrix Multiplication by Sparse Matrices, Part 8', '>>> print(test_format(your_answer_d_BA))\n'), ('cQ3p1gJm23kyNFfuBo37du3OZbnVUGYG', 'Matrix Multiplication by Sparse Matrices, Part 9', '>>> print(test_format(your_answer_e_AB))\n'), ('cQ3p1gJm23kyNFfuuuWgrLw4MhDLMfBl', 'Matrix Multiplication by Sparse Matrices, Part 10', '>>> print(test_format(your_answer_e_BA))\n'), ('cQ3p1gJm23kyNFfuA0BprMBmi3XtG6Tc', 'Matrix Multiplication by Sparse Matrices, Part 11', '>>> print(test_format(your_answer_f_AB))\n'), ('cQ3p1gJm23kyNFfu7ibhXlGYqTVqSPnV', 'Matrix Multiplication by Sparse Matrices, Part 12', '>>> print(test_format(your_answer_f_BA))\n')], [('cQ3p1gJm23kyNFfuadrZQ52SZTPl9Gre', 'Column Vector and Row Vector Matrix Multiplications, Part 1', '>>> print(test_format(column_row_vector_multiplication1))\n'), ('cQ3p1gJm23kyNFfuYKjDKwzdewnqWvbD', 'Column Vector and Row Vector Matrix Multiplications, Part 2', '>>> print(test_format(column_row_vector_multiplication2))\n'), ('cQ3p1gJm23kyNFfuAWVYDenraIMhQtqv', 'Column Vector and Row Vector Matrix Multiplications, Part 3', '>>> print(test_format(column_row_vector_multiplication3))\n'), ('cQ3p1gJm23kyNFfudbEFuxmxxVgF73rY', 'Column Vector and Row Vector Matrix Multiplications, Part 4', '>>> print(test_format(column_row_vector_multiplication4))\n'), ('cQ3p1gJm23kyNFfu7kQSk254hQDPiCP9', 'Column Vector and Row Vector Matrix Multiplications, Part 5', '>>> print(test_format(column_row_vector_multiplication5))\n')], [('cQ3p1gJm23kyNFfukD2AFojWW52LzOZ2', 'linear-combinations matrix-vector multiply', ">>> f = lin_comb_mat_vec_mult\n>>> from vec import Vec\n>>> from mat import Mat\n>>> from tester_classes import VecTester, dummy\n>>> d1 = {0, 1, 2, 3, 4}\n>>> d2 = {'a','b','c','d'}\n>>> D1 = (d1, d2)\n>>> M1 = Mat(D1, {(3, 'd'): 27, (1, 'c'): 26, (3, 'c'): 35, (3, 'a'): 20, (4, 'd'): 26, (1, 'd'): 5, (2, 'a'): 50, (2, 'b'): 11, (1, 'a'): 27, (2, 'c'): 34, (2, 'd'): 40, (4, 'a'): 33, (0, 'b'): 31}) \n>>> M2 = Mat(D1, {(0, 'c'): 1, (3, 'd'): 2, (1, 'c'): 1, (0, 'a'): 1, (3, 'b'): 2, (1, 'b'): 2, (4, 'd'): 2, (1, 'd'): 2, (2, 'a'): 0, (2, 'b'): 2, (0, 'd'): 1, (2, 'c'): 2, (4, 'c'): 0, (4, 'a'): 1, (0, 'b'): 0})\n>>> M3 = Mat(D1, {(0, 'a'): 3, (4, 'd'): 4, (3, 'a'): 5, (2, 'a'): 5, (0, 'd'): 1, (1, 'a'): 3, (4, 'b'): 4, (2, 'c'): 3, (0, 'b'): 4, (3, 'b'): 5, (4, 'a'): 3, (2, 'd'): 3, (4, 'c'): 5})\n>>> M4 = Mat(D1, {(0, 'c'): 0, (3, 'c'): 2, (1, 'b'): 0, (4, 'd'): 2, (3, 'a'): 1, (1, 'd'): 1, (2, 'b'): 2, (2, 'a'): 2, (0, 'd'): 2, (1, 'a'): 0, (2, 'c'): 0, (4, 'c'): 0, (3, 'b'): 0, (3, 'd'): 1, (0, 'b'): 1})\n>>> V1 = Vec(d2, {'b': 12, 'c': 0, 'a': 2, 'd': 6})\n>>> V2 = Vec(d2, {'b': 19, 'c': 19, 'a': 19, 'd': 3})\n>>> V3 = Vec(d2, {'b': 18, 'c': 19})\n>>> matrices = [M1, M2, M3, M4]\n>>> vectors  = [V1, V2, V3]\n>>> print(test_format([f(M, V) for M in matrices for V in vectors]))\n>>> results = []\n>>> for M in matrices:\n...    V_test = Vec(d2, {i: dummy for i in d2})\n...    _ = f(M, V_test)\n...    results.append(sorted(dummy.multiplications, key=tf))\n...    dummy.multiplications = []\n>>> print(test_format(results))\n")], [('cQ3p1gJm23kyNFfuyD3nHHZHfH8ps8He', 'linear-combinations vector-matrix multiply', ">>> f = lin_comb_vec_mat_mult\n>>> from vec import Vec\n>>> from mat import Mat\n>>> from tester_classes import VecTester, dummy\n>>> d1 = {0, 1, 2, 3, 4}\n>>> d2 = {'a','b','c','d'}\n>>> D1 = (d1, d2)\n>>> M1 = Mat(D1, {(3, 'd'): 27, (1, 'c'): 26, (3, 'c'): 35, (3, 'a'): 20, (4, 'd'): 26, (1, 'd'): 5, (2, 'a'): 50, (2, 'b'): 11, (1, 'a'): 27, (2, 'c'): 34, (2, 'd'): 40, (4, 'a'): 33, (0, 'b'): 31}) \n>>> M2 = Mat(D1, {(0, 'c'): 1, (3, 'd'): 2, (1, 'c'): 1, (0, 'a'): 1, (3, 'b'): 2, (1, 'b'): 2, (4, 'd'): 2, (1, 'd'): 2, (2, 'a'): 0, (2, 'b'): 2, (0, 'd'): 1, (2, 'c'): 2, (4, 'c'): 0, (4, 'a'): 1, (0, 'b'): 0})\n>>> M3 = Mat(D1, {(0, 'a'): 3, (4, 'd'): 4, (3, 'a'): 5, (2, 'a'): 5, (0, 'd'): 1, (1, 'a'): 3, (4, 'b'): 4, (2, 'c'): 3, (0, 'b'): 4, (3, 'b'): 5, (4, 'a'): 3, (2, 'd'): 3, (4, 'c'): 5})\n>>> M4 = Mat(D1, {(0, 'c'): 0, (3, 'c'): 2, (1, 'b'): 0, (4, 'd'): 2, (3, 'a'): 1, (1, 'd'): 1, (2, 'b'): 2, (2, 'a'): 2, (0, 'd'): 2, (1, 'a'): 0, (2, 'c'): 0, (4, 'c'): 0, (3, 'b'): 0, (3, 'd'): 1, (0, 'b'): 1})\n>>> U1 = Vec(d1, {0: 1, 1: 0, 2: 1, 3: 2, 4: 0})\n>>> U2 = Vec(d1, {0: 2, 2: 2, 4: 2})\n>>> U3 = Vec(d1, {0: 1, 1: 3, 3: 2})\n>>> matrices = [M1, M2, M3, M4]\n>>> vectors  = [U1, U2, U3]\n>>> print(test_format([f(U, M) for M in matrices for U in vectors]))\n>>> results = []\n>>> for M in matrices:\n...    U_test = Vec(d1, {i: dummy for i in d1})\n...    _ = f(U_test, M)\n...    results.append(sorted(dummy.multiplications, key=tf))\n...    dummy.multiplications = []\n>>> print(test_format(results))\n")], [('cQ3p1gJm23kyNFfuuRaUKf6IRkesMuTw', 'dot-product matrix-vector multiply', ">>> f = dot_product_mat_vec_mult\n>>> from vec import Vec\n>>> from mat import Mat\n>>> from tester_classes import VecTester\n>>> d1 = {0, 1, 2, 3, 4}\n>>> d2 = {'a','b','c','d'}\n>>> D1 = (d1, d2)\n>>> M1 = Mat(D1, {(3, 'd'): 27, (1, 'c'): 26, (3, 'c'): 35, (3, 'a'): 20, (4, 'd'): 26, (1, 'd'): 5, (2, 'a'): 50, (2, 'b'): 11, (1, 'a'): 27, (2, 'c'): 34, (2, 'd'): 40, (4, 'a'): 33, (0, 'b'): 31}) \n>>> M2 = Mat(D1, {(0, 'c'): 1, (3, 'd'): 2, (1, 'c'): 1, (0, 'a'): 1, (3, 'b'): 2, (1, 'b'): 2, (4, 'd'): 2, (1, 'd'): 2, (2, 'a'): 0, (2, 'b'): 2, (0, 'd'): 1, (2, 'c'): 2, (4, 'c'): 0, (4, 'a'): 1, (0, 'b'): 0})\n>>> M3 = Mat(D1, {(0, 'a'): 3, (4, 'd'): 4, (3, 'a'): 5, (2, 'a'): 5, (0, 'd'): 1, (1, 'a'): 3, (4, 'b'): 4, (2, 'c'): 3, (0, 'b'): 4, (3, 'b'): 5, (4, 'a'): 3, (2, 'd'): 3, (4, 'c'): 5})\n>>> M4 = Mat(D1, {(0, 'c'): 0, (3, 'c'): 2, (1, 'b'): 0, (4, 'd'): 2, (3, 'a'): 1, (1, 'd'): 1, (2, 'b'): 2, (2, 'a'): 2, (0, 'd'): 2, (1, 'a'): 0, (2, 'c'): 0, (4, 'c'): 0, (3, 'b'): 0, (3, 'd'): 1, (0, 'b'): 1})\n>>> V1 = Vec(d2, {'b': 12, 'c': 0, 'a': 2, 'd': 6})\n>>> V2 = Vec(d2, {'b': 19, 'c': 19, 'a': 19, 'd': 3})\n>>> V3 = Vec(d2, {'b': 18, 'c': 19})\n>>> matrices = [M1, M2, M3, M4]\n>>> vectors  = [V1, V2, V3]\n>>> print(test_format([f(M, V) for M in matrices for V in vectors]))\n>>> results = []\n>>> V_test = VecTester(d2)\n>>> _ = f(M1, V_test)\n>>> results.append(sorted(V_test.left+V_test.right, key=tf))\n>>> V_test = VecTester(d2)\n>>> _ = f(M2, V_test)\n>>> results.append(sorted(V_test.left+V_test.right, key=tf))\n>>> V_test = VecTester(d2)\n>>> _ = f(M3, V_test)\n>>> results.append(sorted(V_test.left+V_test.right, key=tf))\n>>> V_test = VecTester(d2)\n>>> _ = f(M4, V_test)\n>>> results.append(sorted(V_test.left+V_test.right, key=tf))\n>>> print(test_format(results))\n")], [('cQ3p1gJm23kyNFfusk1N6DUZfVQBt7Pa', 'dot-product vector-matrix multiply', ">>> f = dot_product_vec_mat_mult\n>>> from vec import Vec\n>>> from mat import Mat\n>>> from tester_classes import VecTester\n>>> d1 = {0, 1, 2, 3, 4}\n>>> d2 = {'a','b','c','d'}\n>>> D1 = (d1, d2)\n>>> M1 = Mat(D1, {(3, 'd'): 27, (1, 'c'): 26, (3, 'c'): 35, (3, 'a'): 20, (4, 'd'): 26, (1, 'd'): 5, (2, 'a'): 50, (2, 'b'): 11, (1, 'a'): 27, (2, 'c'): 34, (2, 'd'): 40, (4, 'a'): 33, (0, 'b'): 31}) \n>>> M2 = Mat(D1, {(0, 'c'): 1, (3, 'd'): 2, (1, 'c'): 1, (0, 'a'): 1, (3, 'b'): 2, (1, 'b'): 2, (4, 'd'): 2, (1, 'd'): 2, (2, 'a'): 0, (2, 'b'): 2, (0, 'd'): 1, (2, 'c'): 2, (4, 'c'): 0, (4, 'a'): 1, (0, 'b'): 0})\n>>> M3 = Mat(D1, {(0, 'a'): 3, (4, 'd'): 4, (3, 'a'): 5, (2, 'a'): 5, (0, 'd'): 1, (1, 'a'): 3, (4, 'b'): 4, (2, 'c'): 3, (0, 'b'): 4, (3, 'b'): 5, (4, 'a'): 3, (2, 'd'): 3, (4, 'c'): 5})\n>>> M4 = Mat(D1, {(0, 'c'): 0, (3, 'c'): 2, (1, 'b'): 0, (4, 'd'): 2, (3, 'a'): 1, (1, 'd'): 1, (2, 'b'): 2, (2, 'a'): 2, (0, 'd'): 2, (1, 'a'): 0, (2, 'c'): 0, (4, 'c'): 0, (3, 'b'): 0, (3, 'd'): 1, (0, 'b'): 1})\n>>> U1 = Vec(d1, {0: 1, 1: 0, 2: 1, 3: 2, 4: 0})\n>>> U2 = Vec(d1, {0: 2, 2: 2, 4: 2})\n>>> U3 = Vec(d1, {0: 1, 1: 3, 3: 2})\n>>> matrices = [M1, M2, M3, M4]\n>>> vectors  = [U1, U2, U3]\n>>> print(test_format([f(U, M) for M in matrices for U in vectors]))\n>>> results = []\n>>> for M in matrices:\n...    U_test = VecTester(d1)\n...    _ = f(U_test, M)\n...    results.append(sorted(U_test.left+U_test.right, key=tf))\n>>> print(test_format(results))\n")], [('cQ3p1gJm23kyNFfu9e9M3WHUPc0C1Cv7', 'Matrix-vector matrix-matrix multiply', ">>> from vec import Vec\n>>> from mat import Mat\n>>> from tester_classes import MatTester\n>>> from hashlib import md5\n>>> d1 = {0, 1, 2, 3, 4}\n>>> d2 = {'a','b','c','d'}\n>>> d3 = {True, False}\n>>> D1 = (d1, d2)\n>>> D2 = (d2, d3)\n>>> M1 = Mat(D1, {(3, 'd'): 27, (1, 'c'): 26, (3, 'c'): 35, (3, 'a'): 20, (4, 'd'): 26, (1, 'd'): 5, (2, 'a'): 50, (2, 'b'): 11, (1, 'a'): 27, (2, 'c'): 34, (2, 'd'): 40, (4, 'a'): 33, (0, 'b'): 31}) \n>>> M2 = Mat(D1, {(0, 'c'): 1, (3, 'd'): 2, (1, 'c'): 1, (0, 'a'): 1, (3, 'b'): 2, (1, 'b'): 2, (4, 'd'): 2, (1, 'd'): 2, (2, 'a'): 0, (2, 'b'): 2, (0, 'd'): 1, (2, 'c'): 2, (4, 'c'): 0, (4, 'a'): 1, (0, 'b'): 0})\n>>> M3 = Mat(D1, {(0, 'a'): 3, (4, 'd'): 4, (3, 'a'): 5, (2, 'a'): 5, (0, 'd'): 1, (1, 'a'): 3, (4, 'b'): 4, (2, 'c'): 3, (0, 'b'): 4, (3, 'b'): 5, (4, 'a'): 3, (2, 'd'): 3, (4, 'c'): 5})\n>>> M4 = Mat(D1, {(0, 'c'): 0, (3, 'c'): 2, (1, 'b'): 0, (4, 'd'): 2, (3, 'a'): 1, (1, 'd'): 1, (2, 'b'): 2, (2, 'a'): 2, (0, 'd'): 2, (1, 'a'): 0, (2, 'c'): 0, (4, 'c'): 0, (3, 'b'): 0, (3, 'd'): 1, (0, 'b'): 1})\n>>> N1 = Mat(D2, {('d', True): 2, ('b', False): 0, ('c', True): 0, ('a', True): 1, ('c', False): 0, ('d', False): 2, ('a', False): 1})\n>>> N2 = Mat(D2, {('b', False): 0, ('b', True): 0, ('c', True): 0, ('a', False): 0, ('a', True): 1, ('d', False): 0, ('d', True): 1})\n>>> N3 = Mat(D2, {('c', False): 0, ('b', False): 1, ('b', True): 1, ('d', False): 2, ('a', True): 2, ('d', True): 1, ('a', False): 1})\n>>> N4 = Mat(D2, {('b', True): 2, ('c', True): 2, ('a', False): 2, ('a', True): 1, ('c', False): 0, ('d', False): 1, ('d', True): 1})\n>>> f = Mv_mat_mat_mult\n>>> Ms = [M1, M2, M3, M4]\n>>> Ns = [N1, N2, N3, N4]\n>>> print(test_format(md5(test_format([f(M, N) for M in Ms for N in Ns]).encode()).hexdigest()))\n>>> results = []\n>>> for N in Ns:\n...    M_test = MatTester(D1)\n...    _ = f(M_test, N)\n...    results.append(sorted(M_test.left + M_test.right, key=tf))\n>>> print(test_format(results))\n")], [('cQ3p1gJm23kyNFfu1woixeIj40ZbdmZe', 'Vector-matrix matrix-matrix multiply', ">>> from vec import Vec\n>>> from mat import Mat\n>>> from tester_classes import MatTester\n>>> from hashlib import md5\n>>> d1 = {0, 1, 2, 3, 4}\n>>> d2 = {'a','b','c','d'}\n>>> d3 = {True, False}\n>>> D1 = (d1, d2)\n>>> D2 = (d2, d3)\n>>> M1 = Mat(D1, {(3, 'd'): 27, (1, 'c'): 26, (3, 'c'): 35, (3, 'a'): 20, (4, 'd'): 26, (1, 'd'): 5, (2, 'a'): 50, (2, 'b'): 11, (1, 'a'): 27, (2, 'c'): 34, (2, 'd'): 40, (4, 'a'): 33, (0, 'b'): 31}) \n>>> M2 = Mat(D1, {(0, 'c'): 1, (3, 'd'): 2, (1, 'c'): 1, (0, 'a'): 1, (3, 'b'): 2, (1, 'b'): 2, (4, 'd'): 2, (1, 'd'): 2, (2, 'a'): 0, (2, 'b'): 2, (0, 'd'): 1, (2, 'c'): 2, (4, 'c'): 0, (4, 'a'): 1, (0, 'b'): 0})\n>>> M3 = Mat(D1, {(0, 'a'): 3, (4, 'd'): 4, (3, 'a'): 5, (2, 'a'): 5, (0, 'd'): 1, (1, 'a'): 3, (4, 'b'): 4, (2, 'c'): 3, (0, 'b'): 4, (3, 'b'): 5, (4, 'a'): 3, (2, 'd'): 3, (4, 'c'): 5})\n>>> M4 = Mat(D1, {(0, 'c'): 0, (3, 'c'): 2, (1, 'b'): 0, (4, 'd'): 2, (3, 'a'): 1, (1, 'd'): 1, (2, 'b'): 2, (2, 'a'): 2, (0, 'd'): 2, (1, 'a'): 0, (2, 'c'): 0, (4, 'c'): 0, (3, 'b'): 0, (3, 'd'): 1, (0, 'b'): 1})\n>>> N1 = Mat(D2, {('d', True): 2, ('b', False): 0, ('c', True): 0, ('a', True): 1, ('c', False): 0, ('d', False): 2, ('a', False): 1})\n>>> N2 = Mat(D2, {('b', False): 0, ('b', True): 0, ('c', True): 0, ('a', False): 0, ('a', True): 1, ('d', False): 0, ('d', True): 1})\n>>> N3 = Mat(D2, {('c', False): 0, ('b', False): 1, ('b', True): 1, ('d', False): 2, ('a', True): 2, ('d', True): 1, ('a', False): 1})\n>>> N4 = Mat(D2, {('b', True): 2, ('c', True): 2, ('a', False): 2, ('a', True): 1, ('c', False): 0, ('d', False): 1, ('d', True): 1})\n>>> f = vM_mat_mat_mult\n>>> Ms = [M1, M2, M3, M4]\n>>> Ns = [N1, N2, N3, N4]\n>>> print(test_format(md5(tf([f(M, N) for M in Ms for N in Ns]).encode()).hexdigest()))\n>>> results = []\n>>> for M in Ms:\n...    N_test = MatTester(D2)\n...    _ = f(M, N_test)\n...    results.append(sorted(N_test.left + N_test.right, key=tf))\n>>> print(test_format(results))\n")], [('cQ3p1gJm23kyNFfu6hzDHlIEpiWvPGEs', 'Dot-product matrix-matrix multiply', ">>> from vec import Vec\n>>> from mat import Mat\n>>> from tester_classes import MatTester\n>>> from hashlib import md5\n>>> d1 = {0, 1, 2, 3, 4}\n>>> d2 = {'a','b','c','d'}\n>>> d3 = {True, False}\n>>> D1 = (d1, d2)\n>>> D2 = (d2, d3)\n>>> M1 = Mat(D1, {(3, 'd'): 27, (1, 'c'): 26, (3, 'c'): 35, (3, 'a'): 20, (4, 'd'): 26, (1, 'd'): 5, (2, 'a'): 50, (2, 'b'): 11, (1, 'a'): 27, (2, 'c'): 34, (2, 'd'): 40, (4, 'a'): 33, (0, 'b'): 31}) \n>>> M2 = Mat(D1, {(0, 'c'): 1, (3, 'd'): 2, (1, 'c'): 1, (0, 'a'): 1, (3, 'b'): 2, (1, 'b'): 2, (4, 'd'): 2, (1, 'd'): 2, (2, 'a'): 0, (2, 'b'): 2, (0, 'd'): 1, (2, 'c'): 2, (4, 'c'): 0, (4, 'a'): 1, (0, 'b'): 0})\n>>> M3 = Mat(D1, {(0, 'a'): 3, (4, 'd'): 4, (3, 'a'): 5, (2, 'a'): 5, (0, 'd'): 1, (1, 'a'): 3, (4, 'b'): 4, (2, 'c'): 3, (0, 'b'): 4, (3, 'b'): 5, (4, 'a'): 3, (2, 'd'): 3, (4, 'c'): 5})\n>>> M4 = Mat(D1, {(0, 'c'): 0, (3, 'c'): 2, (1, 'b'): 0, (4, 'd'): 2, (3, 'a'): 1, (1, 'd'): 1, (2, 'b'): 2, (2, 'a'): 2, (0, 'd'): 2, (1, 'a'): 0, (2, 'c'): 0, (4, 'c'): 0, (3, 'b'): 0, (3, 'd'): 1, (0, 'b'): 1})\n>>> N1 = Mat(D2, {('d', True): 2, ('b', False): 0, ('c', True): 0, ('a', True): 1, ('c', False): 0, ('d', False): 2, ('a', False): 1})\n>>> N2 = Mat(D2, {('b', False): 0, ('b', True): 0, ('c', True): 0, ('a', False): 0, ('a', True): 1, ('d', False): 0, ('d', True): 1})\n>>> N3 = Mat(D2, {('c', False): 0, ('b', False): 1, ('b', True): 1, ('d', False): 2, ('a', True): 2, ('d', True): 1, ('a', False): 1})\n>>> N4 = Mat(D2, {('b', True): 2, ('c', True): 2, ('a', False): 2, ('a', True): 1, ('c', False): 0, ('d', False): 1, ('d', True): 1})\n>>> print(test_format(md5(tf([dot_prod_mat_mat_mult(M, N) for M in [M1, M2, M3, M4] for N in [N1, N2, N3, N4]]).encode()).hexdigest()))\n")], [('cQ3p1gJm23kyNFfuaAQObbsANewdaIbC', 'Solving Linear Systems, Part 1', '>>> print(test_format(solving_systems_x1))\n'), ('cQ3p1gJm23kyNFfusweM2vAQ9VW259Yn', 'Solving Linear Systems, Part 2', '>>> print(test_format(solving_systems_x2))\n'), ('cQ3p1gJm23kyNFfug21wGuRlvPaa2Xxk', 'Solving Linear Systems, Part 3', '>>> print(test_format(solving_systems_y1))\n'), ('cQ3p1gJm23kyNFfuoibcgwa0VmwiyNPZ', 'Solving Linear Systems, Part 4', '>>> print(test_format(solving_systems_y2))\n'), ('cQ3p1gJm23kyNFfure4wHp2wegQihQqk', 'Solving Linear Systems, Part 5', '>>> from mat import Mat\n>>> print(test_format(solving_systems_m))\n'), ('cQ3p1gJm23kyNFfuf7xNsWmF5yWetlpb', 'Solving Linear Systems, Part 6', '>>> from mat import Mat\n>>> print(test_format(solving_systems_a))\n'), ('cQ3p1gJm23kyNFfu3fteeHh2yAA9KZbo', 'Solving Linear Systems, Part 7', '>>> from mat import Mat\n>>> print(test_format(solving_systems_a_times_m))\n'), ('cQ3p1gJm23kyNFfutJF7OLOKcMkakjFS', 'Solving Linear Systems, Part 8', '>>> from mat import Mat\n>>> print(test_format(solving_systems_m_times_a))\n')], [('cQ3p1gJm23kyNFfuojPrPB8evSiK6S2E', 'Matrix Inverse Criterion', '>>> print(test_format(are_inverses1))\n>>> print(test_format(are_inverses2))\n>>> print(test_format(are_inverses3))\n>>> print(test_format(are_inverses4))\n')]]
source_files        = ['hw3.py'] * len(sum(groups,[]))

try:
    import hw3 as solution
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
    elif otype is float or otype is int:
        if otype is int:
            obj = float(obj)
        fstr = '%%.%df' % precision
        return fstr % obj
    elif otype is set:
        if len(obj) == 0:
            return 'set()'
        return '{%s}' % delimit(sorted(map(tf, obj)))
    elif otype is dict:
        return '{%s}' % delimit(sorted(tf(k)+': '+tf(v) for k,v in obj.items()))
    elif otype is list:
        return '[%s]' % delimit(map(tf, obj))
    elif otype is tuple:
        return '(%s%s)' % (delimit(map(tf, obj)), ',' if len(obj) is 1 else '')
    elif otype.__name__ in ['Vec','Mat']:
        entries = tf({x:obj.f[x] for x in obj.f if obj.f[x] != 0})
        return '%s(%s, %s)' % (otype.__name__, test_format(obj.D), entries)
    else:
        return str(obj)



def output(tests):
    dtst = doctest.DocTestParser().get_doctest(tests, test_vars, 0, '<string>', 0)
    runner = ModifiedDocTestRunner()
    runner.run(dtst)
    return runner.results

test_vars['test_format'] = test_vars['tf'] = test_format
test_vars['find_lines'] = find_lines
test_vars['find_line'] = find_line
test_vars['use_comprehension'] = use_comprehension
test_vars['double_comprehension'] = double_comprehension
test_vars['line_contains_substr'] = line_contains_substr

base_url = '://class.coursera.org/%s/assignment/' % URL
protocol = 'https'
colorize = False
verbose  = False

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

def submit(parts_string, login, password):   
    print('= Coding the Matrix Homework and Lab Submission')
    
    if not login:
        login = login_prompt()
    if not password:
        password = password_prompt()
    if not parts_string: 
        parts_string = parts_prompt()

    parts = parse_parts(parts_string)

    if not all([parts, login, password]):
        return

    for sid, name, part_tests in parts:
        sys.stdout.write('== Submitting "%s"' % name)

        if 'DEV' in os.environ: sid += '-dev'

        (login, ch, state, ch_aux) = get_challenge(login, sid)

        if not all([login, ch, state]):
            print('  !! Error: %s\n' % login)
            return

        # to stop Coursera's strip() from doing anything, we surround in parens
        results  = output(part_tests)
        prog_out = '(%s)' % ''.join(map(str.rstrip, results))
        token    = challenge_response(login, password, ch)
        src      = source(sid)

        feedback = submit_solution(login, token, sid, prog_out, src, state, ch_aux)

        if len(feedback.strip()) > 0:
            if colorize:
                good = 'incorrect' not in feedback.lower()
                print(': \033[1;3%dm%s\033[0m' % (2 if good else 1, feedback.strip()))
            else:
                print(': %s' % feedback.strip())
        
        if verbose:
            for t, r in zip(part_tests.split('\n'), results):
                sys.stdout.write('%s\n%s' % (t, r))
            sys.stdout.write('\n\n')


def login_prompt():
    return input('Login email address: ')


def password_prompt():
    return input("One-time password from the assignment page (NOT your own account's password): ")


def parts_prompt():
    print('These are the assignment parts that you can submit:')

    for i, name in enumerate(part_friendly_names):
        print('  %d) %s' % (i+1, name))

    return input('\nWhich parts do you want to submit? (Ex: 1, 4-7): ')

def parse_parts(string):
    def extract_range(s):
        s = s.split('-')
        if len(s) == 1: return [int(s[0])]
        else: return list(range(int(s[0]), 1+int(s[1])))
    parts = map(extract_range, string.split(','))
    flat_parts = sum(parts, [])
    return sum(list(map(lambda p: groups[p-1], flat_parts)),[])

def get_challenge(email, sid):
    """Gets the challenge salt from the server. Returns (email,ch,state,ch_aux)."""
    params = {'email_address': email, 'assignment_part_sid': sid, 'response_encoding': 'delim'}

    challenge_url = '%s%schallenge' % (protocol, base_url)
    data = urllib.parse.urlencode(params).encode('utf-8')
    req  = urllib.request.Request(challenge_url, data)
    resp = urllib.request.urlopen(req)
    text = resp.readall().decode('utf-8').strip().split('|')

    if len(text) != 9:
        print('  !! %s' % '|'.join(text))
        sys.exit(1)
  
    return tuple(text[x] for x in [2,4,6,8])


def challenge_response(email, passwd, challenge):
    return hashlib.sha1((challenge+passwd).encode('utf-8')).hexdigest()


def submit_solution(email_address, ch_resp, sid, output, source, state, ch_aux):
    b64ize = lambda s: str(base64.encodebytes(s.encode('utf-8')), 'ascii')

    values = { 'assignment_part_sid' : sid
             , 'email_address'       : email_address
             , 'submission'          : b64ize(output) 
             , 'submission_aux'      : b64ize(source)
             , 'challenge_response'  : ch_resp
             , 'state'               : state
             }

    submit_url = '%s%ssubmit' % (protocol, base_url)
    data     = urllib.parse.urlencode(values).encode('utf-8')
    req      = urllib.request.Request(submit_url, data)
    response = urllib.request.urlopen(req)

    return response.readall().decode('utf-8').strip()


def source(sid):
    src = []
    for fn in set(source_files):
        with open(fn) as source_f:
            src.append(source_f.read())
    return '\n\n'.join(src)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    env = os.environ
    helps = [ 'numbers or ranges of tasks to submit'
            , 'the email address on your Coursera account'
            , 'your ONE-TIME password'
            , 'use ANSI color escape sequences'
            , 'show the test\'s interaction with your code'
            , 'use an encrypted connection to Coursera'
            , 'use an unencrypted connection to Coursera'
            ]
    parser.add_argument('tasks',      default=env.get('COURSERA_TASKS'), nargs='*', help=helps[0])
    parser.add_argument('--email',    default=env.get('COURSERA_EMAIL'),            help=helps[1])
    parser.add_argument('--password', default=env.get('COURSERA_PASS'),             help=helps[2])
    parser.add_argument('--colorize', default=False, action='store_true',           help=helps[3])
    parser.add_argument('--verbose',  default=False, action='store_true',           help=helps[4])
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--https', dest="protocol", const="https", action="store_const", help=helps[-2])
    group.add_argument('--http',  dest="protocol", const="http",  action="store_const", help=helps[-1])
    args = parser.parse_args()
    if args.protocol: protocol = args.protocol
    colorize = args.colorize
    verbose = args.verbose
    submit(','.join(args.tasks), args.email, args.password)

