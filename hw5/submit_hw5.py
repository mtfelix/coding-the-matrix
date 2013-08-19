# version code 941
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

SUBMIT_VERSION      = "941"
URL                 = 'matrix-001'
part_friendly_names = ['Iterative Exchange Lemma', 'Another Iterative Exchange Lemma', 'Morph Lemma Coding', 'Row and Column Rank Practice', 'My Is Independent Procedure', 'Subset Basis', 'My Rank', 'Direct Sum Validity', 'Direct Sum Unique Representation', 'Is Invertible Function', 'Inverse of a Matrix over GF(2)', 'Inverse of a Triangular Matrix']
groups              = [[('ikTo4RnnZJT4gzCi9374j37KggFkFnBz', 'Iterative Exchange Lemma', '>>> from solver import solve\n>>> from vec import Vec\n>>> from vecutil import list2vec\n>>> import independence\n>>> w0 = list2vec([1,0,0])\n>>> w1 = list2vec([0,1,0])\n>>> w2 = list2vec([0,0,1])\n>>> v0 = list2vec([1,2,3])\n>>> v1 = list2vec([1,3,3])\n>>> v2 = list2vec([0,3,3])\n>>> print(test_format(list(map(len, [exchange_S0, exchange_S1, exchange_S2, exchange_S3]))))\n>>> print(test_format(len(set(map(tf, exchange_S1)) & set(map(tf,[w0,w1,w2])))))\n>>> print(test_format(len(set(map(tf, exchange_S1)) & set(map(tf,[v0,v1,v2])))))\n>>> print(test_format(len(set(map(tf, exchange_S2)) & set(map(tf,[w0,w1,w2])))))\n>>> print(test_format(len(set(map(tf, exchange_S2)) & set(map(tf,[v0,v1,v2])))))\n>>> es = [exchange_S0, exchange_S1, exchange_S2, exchange_S3]\n>>> print(test_format(list(map(independence.is_independent, es))))\n')], [('ikTo4RnnZJT4gzCiU8r9hKTHrA1ZyViy', 'Another Iterative Exchange Lemma', '>>> from solver import solve\n>>> from vec import Vec\n>>> import independence\n>>> from vecutil import list2vec\n>>> from GF2 import one\n>>> w0 = list2vec([0,one,0])\n>>> w1 = list2vec([0,0,one])\n>>> w2 = list2vec([one,one,one])\n>>> v0 = list2vec([one,0,one])\n>>> v1 = list2vec([one,0,0])\n>>> v2 = list2vec([one,one,0])\n>>> print(test_format(list(map(len, [exchange_2_S0, exchange_2_S1, exchange_2_S2, exchange_2_S3]))))\n>>> print(test_format(len(set(map(tf, exchange_2_S1)) & set(map(tf,[w0,w1,w2])))))\n>>> print(test_format(len(set(map(tf, exchange_2_S1)) & set(map(tf,[v0,v1,v2])))))\n>>> print(test_format(len(set(map(tf, exchange_2_S2)) & set(map(tf,[w0,w1,w2])))))\n>>> print(test_format(len(set(map(tf, exchange_2_S2)) & set(map(tf,[v0,v1,v2])))))\n>>> es = [exchange_2_S0, exchange_2_S1, exchange_2_S2, exchange_2_S3]\n>>> print(test_format([independence.is_independent(e) for e in es]))\n')], [('ikTo4RnnZJT4gzCi4XeYoFwOTWCdATpi', 'Morph Lemma Coding', '>>> from vecutil import list2vec\n>>> from independence import rank\n>>> S = [list2vec(v) for v in [[2,4,0],[1,0,3],[0,4,4],[1,1,1]]]\n>>> B = [list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]\n>>> m = morph(S, B)\n>>> injs, ejs = zip(*m)\n>>> print(test_format(S))\n>>> print(test_format([rank([x for x in S+list(injs[:i]) if x not in ejs[:i]]) for i in range(len(m))]))\n>>> print(test_format([(x in [y for y in injs if y not in ejs]) for x in B]))\n>>> S = [list2vec(v) for v in [[1,0,0,0],[0,3,0,0],[2,0,9,0],[0,2,0,1],[0,0,0,4]]]\n>>> B = [list2vec(v) for v in [[3,0,0,0],[0,7,0,0],[0,0,2,0],[0,0,0,6]]]\n>>> m = morph(S, B)\n>>> injs, ejs = zip(*m)\n>>> print(test_format([rank([x for x in S+list(injs[:i]) if x not in ejs[:i]]) for i in range(len(m))]))\n>>> print(test_format([(x in [y for y in injs if y not in ejs]) for x in B]))\n')], [('ikTo4RnnZJT4gzCicL0au22tGBfpPuPh', 'Row and Column Rank Practice, Part 1', '>>> import independence\n>>> from matutil import coldict2mat\n>>> from vecutil import list2vec \n>>> print(test_format(independence.is_independent(row_space_1)))\n>>> print(test_format(independence.rank(row_space_1)))\n>>> A = coldict2mat(row_space_1)\n>>> x =(list2vec([1,1,1]) - A*solve(A, list2vec([1,1,1])))\n>>> print(test_format(x*x < 1E-15))\n'), ('ikTo4RnnZJT4gzCisG3apsIrG7mV0uGC', 'Row and Column Rank Practice, Part 2', '>>> import independence\n>>> from matutil import coldict2mat\n>>> from vecutil import list2vec \n>>> print(test_format(independence.is_independent(col_space_1)))\n>>> print(test_format(independence.rank(col_space_1)))\n>>> A = coldict2mat(col_space_1)\n>>> x =(list2vec([1,1]) - A*solve(A, list2vec([1,1])))\n>>> print(test_format(x*x < 1E-15))\n'), ('ikTo4RnnZJT4gzCiKV9RTcf4fnnBnULX', 'Row and Column Rank Practice, Part 3', '>>> import independence\n>>> from matutil import coldict2mat\n>>> from vecutil import list2vec \n>>> print(test_format(independence.is_independent(row_space_2)))\n>>> print(test_format(independence.rank(row_space_2)))\n>>> A = coldict2mat(row_space_2)\n>>> x =(list2vec([1,1,1,1]) - A*solve(A, list2vec([1,1,1,1])))\n>>> print(test_format(x*x < 1E-15))\n'), ('ikTo4RnnZJT4gzCiJs86NKatUNhENDp1', 'Row and Column Rank Practice, Part 4', '>>> import independence\n>>> from matutil import coldict2mat\n>>> from vecutil import list2vec \n>>> print(test_format(independence.is_independent(col_space_2)))\n>>> print(test_format(independence.rank(col_space_2)))\n>>> A = coldict2mat(col_space_2)\n>>> x =(list2vec([1,1,1]) - A*solve(A, list2vec([1,1,1])))\n>>> print(test_format(x*x < 1E-15))\n'), ('ikTo4RnnZJT4gzCiQPscHcpNbgIu0acT', 'Row and Column Rank Practice, Part 5', '>>> import independence\n>>> from matutil import coldict2mat\n>>> from vecutil import list2vec \n>>> print(test_format(independence.is_independent(row_space_3)))\n>>> print(test_format(independence.rank(row_space_3)))\n>>> A = coldict2mat(row_space_3)\n>>> x =(list2vec([1]) - A*solve(A, list2vec([1])))\n>>> print(test_format(x*x < 1E-15))\n'), ('ikTo4RnnZJT4gzCijdpk57hlKnRunpLK', 'Row and Column Rank Practice, Part 6', '>>> import independence\n>>> from matutil import coldict2mat\n>>> from vecutil import list2vec \n>>> print(test_format(independence.is_independent(col_space_3)))\n>>> print(test_format(independence.rank(col_space_3)))\n>>> A = coldict2mat(col_space_3)\n>>> x =(list2vec([1,1,1]) - A*solve(A, list2vec([1,1,1])))\n>>> print(test_format(x*x < 1E-15))\n'), ('ikTo4RnnZJT4gzCixAyv0O1i7oPY9YJV', 'Row and Column Rank Practice, Part 7', '>>> import independence\n>>> from matutil import coldict2mat\n>>> from vecutil import list2vec \n>>> print(test_format(independence.is_independent(row_space_4)))\n>>> print(test_format(independence.rank(row_space_4)))\n>>> A = coldict2mat(row_space_4)\n>>> x =(list2vec([1,1]) - A*solve(A, list2vec([1,1])))\n>>> print(test_format(x*x < 1E-15))\n'), ('ikTo4RnnZJT4gzCiG7oDHFsETjfUQf61', 'Row and Column Rank Practice, Part 8', '>>> import independence\n>>> from matutil import coldict2mat\n>>> from vecutil import list2vec \n>>> print(test_format(independence.is_independent(col_space_4)))\n>>> print(test_format(independence.rank(col_space_4)))\n>>> A = coldict2mat(col_space_4)\n>>> x =(list2vec([1,1,1]) - A*solve(A, list2vec([1,1,1])))\n>>> print(test_format(x*x < 1E-15))\n')], [('ikTo4RnnZJT4gzCiTaizIiN0APYs8nr8', 'My Is Independent Procedure', '>>> import independence\n>>> independence.is_independent.__calls__ = 0\n>>> print(test_format(my_is_independent([list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]])))\n>>> print(test_format(my_is_independent([list2vec(v) for v in [[1,0,0],[0,1,0],[0,1,1]]])))\n>>> print(test_format(my_is_independent([list2vec(v) for v in [[1,0,0],[0,1,0],[1,1,1]]])))\n>>> print(test_format(my_is_independent([list2vec(v) for v in [[1,0,0],[0,1,0],[1,1,0]]])))\n>>> print(test_format(my_is_independent([list2vec(v) for v in [[1]]])))\n>>> from GF2 import one\n>>> print(test_format(my_is_independent([list2vec(v) for v in [[one,0,0,one],[one,one,one,0],[0,one,0,one]]])))\n>>> print(test_format(my_is_independent([list2vec(v) for v in [[one,one,one,one],[one,0,one,one],[0,one,0,0]]])))\n>>> print(test_format(independence.is_independent.__calls__))\n')], [('ikTo4RnnZJT4gzCi74CF90AgCuncUw8L', 'Subset Basis', ">>> from vec import Vec\n>>> a0 = Vec({'a','b','c','d'}, {'a':1})\n>>> a1 = Vec({'a','b','c','d'}, {'b':1})\n>>> a2 = Vec({'a','b','c','d'}, {'c':1})\n>>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})\n>>> print(test_format(subset_basis([a0,a1,a2,a3])))\n>>> print(test_format(subset_basis([a0,a3,a1,a2])))\n")], [('ikTo4RnnZJT4gzCiFHQD6oJoQyLhtRhT', 'My Rank', '>>> from vec import Vec\n>>> import independence\n>>> independence.rank.__calls__ = 0\n>>> independence.is_independent.__calls__ = 0\n>>> print(test_format(independence.rank([])))\n>>> L = [Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 21, 1: 21, 2: 15, 3: 30, 4: 1, 5: 16, 6: 15, 7: 13, 8: 20, 9: 7}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 20, 1: 7, 2: 9, 3: 11, 4: 24, 5: 24, 6: 15, 7: 10, 8: 30, 9: 8}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 12, 1: 24, 2: 15, 3: 3, 4: 1, 5: 13, 6: 22, 7: 26, 8: 15, 9: 28}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 13, 1: 16, 2: 25, 3: 2, 4: 21, 5: 2, 6: 10, 7: 12, 8: 24, 9: 18}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 24, 1: 16, 2: 11, 3: 17, 4: 20, 5: 28, 6: 4, 7: 2, 8: 13, 9: 7}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 14, 1: 6, 2: 5, 3: 20, 4: 23, 5: 2, 6: 29, 7: 29, 8: 17, 9: 14}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 10, 1: 5, 2: 9, 3: 24, 4: 7, 5: 16, 6: 17, 7: 27, 8: 29, 9: 1}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 3, 1: 19, 2: 14, 3: 18, 4: 22, 5: 10, 6: 16, 7: 17, 8: 25, 9: 16}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 23, 1: 16, 2: 28, 3: 12, 4: 16, 5: 16, 6: 10, 7: 12, 8: 12, 9: 20}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 28, 1: 5, 2: 21, 3: 9, 4: 10, 5: 27, 6: 15, 7: 30, 8: 27, 9: 19}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 12, 1: 11, 2: 24, 3: 4, 4: 14, 5: 27, 6: 23, 7: 24, 8: 6, 9: 10}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 6, 1: 14, 2: 20, 3: 5, 4: 27, 5: 15, 6: 8, 7: 8, 8: 1, 9: 26}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 23, 1: 13, 2: 28, 3: 21, 4: 8, 5: 18, 6: 25, 7: 12, 8: 12, 9: 21}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 7, 1: 11, 2: 19, 3: 24, 4: 18, 5: 17, 6: 5, 7: 0, 8: 18, 9: 4}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 25, 1: 24, 2: 21, 3: 3, 4: 30, 5: 21, 6: 17, 7: 3, 8: 9, 9: 9}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 10, 1: 22, 2: 4, 3: 19, 4: 6, 5: 25, 6: 27, 7: 21, 8: 14, 9: 7}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 27, 1: 1, 2: 21, 3: 0, 4: 19, 5: 10, 6: 16, 7: 0, 8: 3, 9: 4}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 12, 1: 6, 2: 7, 3: 30, 4: 26, 5: 6, 6: 23, 7: 18, 8: 22, 9: 26}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 27, 1: 15, 2: 19, 3: 20, 4: 1, 5: 15, 6: 6, 7: 6, 8: 4, 9: 4}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 6, 1: 18, 2: 12, 3: 27, 4: 23, 5: 13, 6: 13, 7: 21, 8: 13, 9: 14})]\n>>> print(test_format(my_rank(L)))\n>>> L = [Vec({0, 1, 2},{0: 1, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 2, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 2}), Vec({0, 1, 2},{0: 1, 1: 0, 2: 1})]\n>>> print(test_format(my_rank(L)))\n>>> print(test_format(independence.rank.__calls__ - independence.is_independent.__calls__ < 0))\n')], [('ikTo4RnnZJT4gzCiGikUmXaRhxBTXbD2', 'Direct Sum Validity, Part 1', '>>> print(test_format(only_share_the_zero_vector_1))\n'), ('ikTo4RnnZJT4gzCiF5iUMzJrxwjJrgXK', 'Direct Sum Validity, Part 2', '>>> print(test_format(only_share_the_zero_vector_2))\n'), ('ikTo4RnnZJT4gzCiu9YmBZJGWB19JHOA', 'Direct Sum Validity, Part 3', '>>> print(test_format(only_share_the_zero_vector_3))\n')], [('ikTo4RnnZJT4gzCiY6uQO7PyIvdw3ShY', 'Direct Sum Unique Representation', '>>> from vec import Vec\n>>> d = {0,1,2,3,4,5}\n>>> dikt = lambda o: dict(enumerate(o))\n>>> u_basis = [Vec(d, dikt(f)) for f in [(2,1,0,0,6,0),(11,5,0,0,1,0),(3,1.5,0,0,7.5,0)]]\n>>> v_basis = [Vec(d, dikt(f)) for f in [(0,0,7,0,0,1),(0,0,15,0,0,2)]]\n>>> w1 = Vec(d, {0:2, 1:5, 4:1})\n>>> w2 = Vec(d, {2:3, 5:-4})\n>>> w3 = Vec(d, {0:1, 1:2, 4:2, 5:1})\n>>> w4 = Vec(d, {0:-6, 1:2, 2:4, 4:4, 5:5})\n>>> print(test_format(direct_sum_decompose(u_basis, v_basis, w1)))\n>>> print(test_format(direct_sum_decompose(u_basis, v_basis, w2)))\n>>> print(test_format(direct_sum_decompose(u_basis, v_basis, w3)))\n>>> print(test_format(direct_sum_decompose(u_basis, v_basis, w4)))\n')], [('ikTo4RnnZJT4gzCisePwrVxfXVpiAXYy', 'Is Invertible Function', '>>> A = Mat(({0, 1}, {0, 1, 2}), {(0, 1): 2, (1, 2): 1, (0, 0): 1, (1, 0): 3, (0, 2): 3, (1, 1): 1})\n>>> B = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 0, (1, 2): 1, (3, 2): 0, (0, 0): 1, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 1, (2, 0): 0, (1, 3): 0, (2, 3): 1, (2, 2): 3, (1, 0): 0, (0, 3): 0})\n>>> C = Mat(({0, 1, 2}, {0, 1}), {(0, 1): 0, (2, 0): 2, (0, 0): 1, (1, 0): 0, (1, 1): 1, (2, 1): 1})\n>>> D = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 5, (1, 2): 2, (0, 0): 1, (2, 0): 4, (1, 0): 2, (2, 2): 7, (0, 2): 8, (2, 1): 6, (1, 1): 5})\n>>> E = Mat(({0, 1, 2, 3, 4}, {0, 1, 2, 3, 4}), {(1, 2): 7, (3, 2): 7, (0, 0): 3, (3, 0): 1, (0, 4): 3, (1, 4): 2, (1, 3): 4, (2, 3): 0, (2, 1): 56, (2, 4): 5, (4, 2): 6, (1, 0): 2, (0, 3): 7, (4, 0): 2, (0, 1): 5, (3, 3): 4, (4, 1): 4, (3, 1): 23, (4, 4): 5, (0, 2): 7, (2, 0): 2, (4, 3): 8, (2, 2): 9, (3, 4): 2, (1, 1): 4})\n>>> print(test_format(is_invertible(A)))\n>>> print(test_format(is_invertible(B)))\n>>> print(test_format(is_invertible(C)))\n>>> print(test_format(is_invertible(D)))\n>>> print(test_format(is_invertible(E)))\n')], [('ikTo4RnnZJT4gzCihpi0EGyxJVEXZ7SN', 'Inverse of a Matrix over GF(2)', '>>> from matutil import listlist2mat\n>>> from GF2 import one\n>>> I5 = [[one]+[0]*4, [0,one,0,0,0], [0,0,one,0,0], [0,0,0,one,0], [0,0,0,0,one]]\n>>> M5 = Mat(({0, 1, 2, 3, 4}, {0, 1, 2, 3, 4}), {(1, 2): 0, (3, 2): 0, (0, 0): one, (3, 0): 0, (0, 4): 0, (1, 4): 0, (1, 3): 0, (2, 3): 0, (2, 1): 0, (2, 4): 0, (4, 2): 0, (1, 0): 0, (0, 3): 0, (4, 0): 0, (0, 1): 0, (3, 3): one, (4, 1): 0, (3, 1): 0, (4, 4): one, (0, 2): 0, (2, 0): 0, (4, 3): 0, (2, 2): one, (3, 4): 0, (1, 1): one})\n>>> print(test_format(find_matrix_inverse(M5)))\n>>> M2 = listlist2mat([list(map(sum,zip(I5[0],I5[1]))), I5[1], I5[2], I5[3], I5[4]])\n>>> N = find_matrix_inverse(M2)\n>>> print(test_format(M2 * N == M5))\n>>> print(test_format(M2 == N))\n>>> M3 = listlist2mat([I5[0], I5[2], I5[1], I5[3], I5[4]])\n>>> N = find_matrix_inverse(M3)\n>>> print(test_format(M3 * N == M5))\n>>> print(test_format(M3 == M2))\n>>> M23 = M2 * M3\n>>> N23 = find_matrix_inverse(M23)\n>>> print(test_format(M23 * N23 == M5))\n>>> print(test_format(N23))\n>>> M233 = M23 * M3\n>>> N233 = find_matrix_inverse(M233)\n>>> print(test_format(N233))\n>>> buckets = {0:[27,14,15,6,3,29,20,7,1,0,21,22,16,12,23,26],1:[21,19,0,5,13,2,17,6,12,25,3,4,9,27],2:[6,24,7,13,4,5,17,28,8,3,20,0],3:[2,23,11,17,4,29,10,13,7,24,12,1,18,21,26,28,8,9],4:[10,5,16,12,17,11,7,15,9,0,19,23,26,1,8,27,22,20,2,29],5:[24,21,10,20,0,6,15,28,5,18,14,23,16,12,25],6:[9,28,23,14,29,1,27,15,6,21,7,13,16,4,17,5],7:[5,2,15,29,26,6,19,28,11,20,13,14],8:[24,18,6,0,1,27,15,2,28,22,10,11],9:[0,21,9,19,7,8,29,18,15,28,17,5,26,3,16,13,23,11,24,12,1,22],10:[8,14,9,15,26,16,12,27,13,23,10,20,0,6,21,1,28],11:[5,22,27,16,9,14,7,18,6,28,0,10,20,2,24,17],12:[17,28,27,18,29,20,10,1,12,11,22,2,4,25,5,14,15],13:[13,26,3,12,11,10,29,15,28,8,27],14:[1,21,19,26,27,14,4,15,2,13],15:[11,4,16,25,8,14,29,15,23,22],16:[6,19,1,11,2,0,13,4,26,14,27,18],17:[25,13,18,24,5,10,16,4,9,2,23,8,1,0,21,26,19],18:[4,10,25,5,11,2,23,14,29,20,0,15,26,1],19:[19,4,24,18,7,27,12,21,26,15,0,20,29,17,2,22,11,25,10],20:[25,20,14,26,0,28,22,29,23,2,9,16,3,10,12,17,11],21:[6,15,5,14,26,23,3,12,21,10,19],22:[19,6,25,16,10,13,17,11,5,8,28,3,9,29,27,14,24],23:[28,6,27,18,8,11,23,0,25,10,22,3,24,17,2,15,4,16,29,14],24:[27,8,28,15,2,22,16,3,10,4,24,11,5,25,6,13,0],25:[15,3,28,27,2,11,1,10,0,4,20,9,5,29,18,8],26:[24,13,20,10,21,0,14,1,29,8,7,26,16,15,9,27,22],27:[21,6,24,12,16,5,10,19,14,18,4],28:[7,1,26,5,24,11,13,25,4,15,28,18,22,20,19,21,12,9,0],29:[26,16,8,10,21,2,15,20,1,7,13,18,12,24]}\n>>> keys = [(k,v) for k in buckets for v in buckets[k]]\n>>> M = Mat((set(range(30)),)*2, {k:one for k in keys})\n>>> N = find_matrix_inverse(M)\n>>> print(test_format([(1 if N[x] == one else 0) for x in [(0, 22), (18, 12), (17, 22), (23, 24), (4, 7), (9, 22)]]))\n')], [('ikTo4RnnZJT4gzCif1nv2o6uJGOYafNs', 'Inverse of a Triangular Matrix', '>>> from mat import Mat\n>>> A = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 2, (1, 2): 3, (3, 2): 0, (0, 0): 1, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 3, (2, 0): 0, (1, 3): 4, (2, 3): 4, (2, 2): 3, (1, 0): 0, (0, 3): 4})\n>>> B = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 4, (1, 2): 5, (3, 2): 0, (0, 0): 7, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 2, (2, 0): 0, (1, 3): 6, (2, 3): 4, (2, 2): 7, (1, 0): 0, (0, 3): 5})\n>>> C = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 3, (1, 2): 6, (3, 2): 0, (0, 0): 6, (3, 3): 2345, (3, 0): 0, (3, 1): 0, (1, 1): 4, (2, 1): 0, (0, 2): 4, (2, 0): 0, (1, 3): 23, (2, 3): 2, (2, 2): 6, (1, 0): 0, (0, 3): 8})\n>>> print(test_format(find_triangular_matrix_inverse(A)))\n>>> print(test_format(find_triangular_matrix_inverse(B)))\n>>> print(test_format(find_triangular_matrix_inverse(C)))\n')]]
source_files        = ['hw5.py'] * len(sum(groups,[]))

try:
    import hw5 as solution
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
        if -0.000001 < obj < 0.000001:
            obj = 0.0
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
        entries = tf({x:obj.f[x] for x in obj.f if tf(obj.f[x]) != tf(0)})
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
    src = ['# submit version: %s' % SUBMIT_VERSION]
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

