from mat import Mat
from hw3 import * 

#M = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 0): -1, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 3, (2, 0): 2, (2, 1): 2, (2, 2): 1})
#v = Vec({0, 1, 2}, {0:1,1:2})
#vec = lin_comb_mat_vec_mult(M,v)
#print (vec)

M = Mat(({0, 1, 2}, {0, 1}), {(0, 1): 1, (2, 0): 8, (1, 0): 4, (0, 0): 3, (2, 1): -2})
print(mat2coldict(M))
