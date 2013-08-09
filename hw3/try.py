from mat import Mat
from hw3 import * 

#M = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 0): -1, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 3, (2, 0): 2, (2, 1): 2, (2, 2): 1})
#v = Vec({0, 1, 2}, {0:1,1:2})
#vec = lin_comb_mat_vec_mult(M,v)
#print (vec)

A = Mat(({0, 1}, {'a', 'b', 'c'}), {(0, 'a'): 1, (0, 'b'): 2, (0, 'c'): 3, (1, 'a'): 4, (1, 'b'): 5})
B = Mat(({'a', 'b', 'c'}, {'x', 'y'}), {('a', 'x'): 1, ('b', 'y'): 1, ('c', 'x'): 1})
print(A)
print(B)
print(dot_prod_mat_mat_mult(A,B))
