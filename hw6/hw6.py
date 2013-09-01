# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one



## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[   ...   ],
                  [   ...   ],
                  [   ...   ],
                  [   ...   ],
                  [   ...   ]]

echelon_form_2 = [[   ...   ],
                  [   ...   ],
                  [   ...   ],
                  [   ...   ]]

echelon_form_3 = [[   ...   ],
                  [   ...   ],
                  [   ...   ]]

echelon_form_4 = [[   ...   ],
                  [   ...   ],
                  [   ...   ],
                  [   ...   ]]



## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
    '''
    pass



## Problem 3
# Give each answer as a list

echelon_form_vec_a = ...
echelon_form_vec_b = ...
echelon_form_vec_c = ...



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = ...
solving_with_echelon_form_b = ...



## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
    >>> b_list = [one,0,one]>>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    pass



## Problem 6
rowlist = [ ... ]    # Provide as a list of Vec instances
label_list = [ ... ] # Provide as a list
b = [ ... ]          # Provide as a list



## Problem 7
null_space_rows_a = {...} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {...}



## Problem 9
# Write each vector as a list
closest_vector_1 = [...]
closest_vector_2 = [...]
closest_vector_3 = [...]



## Problem 10
# Write each vector as a list

project_onto_1 = [...]
projection_orthogonal_1 = [...]

project_onto_2 = [...]
projection_orthogonal_2 = [...]

project_onto_3 = [...]
projection_orthogonal_3 = [...]



## Problem 11
norm1 = ...
norm2 = ...
norm3 = ...

