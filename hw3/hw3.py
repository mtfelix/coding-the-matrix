# version code 893
# Please fill out this stencil and submit using the provided submission script.

from mat import Mat
from vec import Vec



## Problem 1
# Please represent your solutions as lists.
vector_matrix_product_1 = ...
vector_matrix_product_2 = ...
vector_matrix_product_3 = ... 



## Problem 2
# Represent your solution as a list of rows.
# For example, the identity matrix would be [[1,0],[0,1]].

M_swap_two_vector = ...



## Problem 3
three_by_three_matrix = ... # Represent with a list of rows lists.



## Problem 4
multiplied_matrix = ... # Represent with a list of row lists.



## Problem 5
# Please enter a boolean representing if the multiplication is valid.
# If it is not valid, please enter None for the dimensions.

part_1_valid = ... # True or False
part_1_number_rows = ... # Integer or None
part_1_number_cols = ... # Integer or None

part_2_valid = ...
part_2_number_rows = ...
part_2_number_cols = ...

part_3_valid = ...
part_3_number_rows = ...
part_3_number_cols = ...

part_4_valid = ...
part_4_number_rows = ...
part_4_number_cols = ...

part_5_valid = ...
part_5_number_rows = ...
part_5_number_cols = ...

part_6_valid = ...
part_6_number_rows = ...
part_6_number_cols = ...

part_7_valid = ...
part_7_number_rows = ...
part_7_number_cols = ...




## Problem 6
# Please represent your answer as a list of row lists.

small_mat_mult_1 = ...
small_mat_mult_2 = ...
small_mat_mult_3 = ...
small_mat_mult_4 = ...
small_mat_mult_5 = ...
small_mat_mult_6 = ...



## Problem 7
# Please represent your solution as a list of row lists.

part_1_AB = ...
part_1_BA = ...

part_2_AB = ...
part_2_BA = ...

part_3_AB = ...
part_3_BA = ...



## Problem 8
# Please represent your answer as a list of row lists.
# Please represent the variables a and b as strings.
# Represent multiplication of the variables, make them one string.
# For example, the sum of 'a' and 'b' would be 'a+b'.

matrix_matrix_mult_1    = ...
matrix_matrix_mult_2_A2 = ...
matrix_matrix_mult_2_A3 = ...

# Use the string 'n' to represent variable the n in A^n.
matrix_matrix_mult_2_An = ...



## Problem 9
# Please represent your answer as a list of row lists.

your_answer_a_AB = ...
your_answer_a_BA = ...

your_answer_b_AB = ...
your_answer_b_BA = ...

your_answer_c_AB = ...
your_answer_c_BA = ...

your_answer_d_AB = ...
your_answer_d_BA = ...

your_answer_e_AB = ...
your_answer_e_BA = ...

your_answer_f_AB = ...
your_answer_f_BA = ...



## Problem 10
column_row_vector_multiplication1 = Vec({0, 1}, {...})

column_row_vector_multiplication2 = Vec({0, 1, 2}, {...})

column_row_vector_multiplication3 = Vec({0, 1, 2, 3}, {...})

column_row_vector_multiplication4 = Vec({0,1}, {...})

column_row_vector_multiplication5 = Vec({0, 1, 2}, {...})



## Problem 11
def lin_comb_mat_vec_mult(M, v):
    assert(M.D[1] == v.D)
    pass



## Problem 12
def lin_comb_vec_mat_mult(v, M):
    assert(v.D == M.D[0])
    pass



## Problem 13
def dot_product_mat_vec_mult(M, v):
    assert(M.D[1] == v.D)
    pass



## Problem 14
def dot_product_vec_mat_mult(v, M):
    assert(v.D == M.D[0])
    pass



## Problem 15
def Mv_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    pass



## Problem 16
def vM_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    pass



## Problem 17
def dot_prod_mat_mat_mult(A, B):
    assert A.D[1] == B.D[0]
    pass



## Problem 18
solving_systems_x1 = ...
solving_systems_x2 = ...
solving_systems_y1 = ...
solving_systems_y2 = ...
solving_systems_m = Mat(({0, 1}, {0, 1}), {...})
solving_systems_a = Mat(({0, 1}, {0, 1}), {...})
solving_systems_a_times_m = Mat(({0, 1}, {0, 1}), {...})
solving_systems_m_times_a = Mat(({0, 1}, {0, 1}), {...})



## Problem 19
# Please write your solutions as booleans (True or False)

are_inverses1 = ...
are_inverses2 = ...
are_inverses3 = ...
are_inverses4 = ...

