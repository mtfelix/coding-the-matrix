# version code 941
# Please fill out this stencil and submit using the provided submission script.

from GF2 import one
from math import sqrt, pi
from matutil import coldict2mat
from solver import solve
from vec import Vec



## Problem 1
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.
#
# For example, [1, 3, 5] would mean 1*[2,0,4,0] + 3*[0,1,0,1] + 5*[0,0,-1,-1]

rep_1 = [...]
rep_2 = [...]
rep_3 = [...]



## Problem 2
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

lin_comb_coefficients_1 = [...]
lin_comb_coefficients_2 = [...]
lin_comb_coefficients_3 = [...]
lin_comb_coefficients_4 = [...]



## Problem 3
# Use one from the GF2 module, not the integer 1.
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

gf2_rep_1 = [...]
gf2_rep_2 = [...]
gf2_rep_3 = [...]



## Problem 4
# Use one from the GF2 module, not the integer 1.
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

gf2_lc_rep_1 = [...]
gf2_lc_rep_2 = [...]
gf2_lc_rep_3 = [...]
gf2_lc_rep_4 = [...]



## Problem 5
# For each part, please provide your solution as a list of the coefficients for
# the generators of V.

lin_dep_R_1 = [...]
lin_dep_R_2 = [...]
lin_dep_R_3 = [...]



## Problem 6
# Please record your solution as a list of coefficients

linear_dep_R_1 = [...]
linear_dep_R_2 = [...]
linear_dep_R_3 = [...]



## Problem 7
# Assign the COEFFICIENT of the vector to each variable.
# Assign sum_to to the vector that you are expressing as a linear combination
# of the other two.  Write the name of the vector as a STRING.  i.e. 'u' or 'w'

u = ...
v = ...
w = ...
sum_to = ...



## Problem 8
# Please use the Vec class to represent your vectors

indep_vec_1 = Vec({...}, {...})
indep_vec_2 = Vec({...}, {...})
indep_vec_3 = Vec({...}, {...})
indep_vec_4 = Vec({...}, {...})



## Problem 9
# Please give your solution as a list of coefficients of the linear combination

zero_comb_1 = [...]
zero_comb_2 = [...]
zero_comb_3 = [...]



## Problem 10
# Please give your solution as a list of coefficients of the vectors
# in the set in order (list the coefficient for v_i before v_j if i < j).

sum_to_zero_1 = [...]
sum_to_zero_2 = [...]
sum_to_zero_3 = [...]
sum_to_zero_4 = [...]



## Problem 11
## Please express your answer a list of ints, such as [1,0,0,0,0]

exchange_1 = [...]
exchange_2 = [...]
exchange_3 = [...]


## Problem 12
# Please give the name of the vector you want to replace as a string (e.g. 'v1')

replace_1 = ...
replace_2 = ...
replace_3 = ...



## Problem 13
def rep2vec(u, veclist):
    '''
    Input:
        - u: a vector as an instance of your Vec class with domain set(range(len(veclist)))
        - veclist: a list of n vectors (as Vec instances)
    Output:
        vector v (as Vec instance) whose coordinate representation is u
    Example:
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> rep2vec(Vec({0,1,2}, {0:2, 1:4, 2:6}), [a0,a1,a2]) == Vec({'a', 'c', 'b', 'd'},{'a': 2, 'c': 6, 'b': 4, 'd': 0})
        True
    '''
    pass



## Problem 14
def vec2rep(veclist, v):
    '''
    Input:
        - veclist: a list of vectors (as instances of your Vec class)
        - v: a vector (as Vec instance) with domain set(range(len(veclist)))
             with v in the span of set(veclist).
    Output:
        Vec instance u whose coordinate representation w.r.t. veclist is v
    Example:
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> vec2rep([a0,a1,a2], Vec({'a','b','c','d'}, {'a':3, 'c':-2})) == Vec({0, 1, 2},{0: 3.0, 1: 0.0, 2: -2.0})
        True
    '''
    pass



## Problem 15
def is_superfluous(L, i):
    '''
    Input:
        - L: list of vectors as instances of Vec class
        - i: integer in range(len(L))
    Output:
        True if the span of the vectors of L is the same
        as the span of the vectors of L, excluding L[i].

        False otherwise.
    Examples:
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
        >>> is_superfluous(L, 3)
        True
        >>> is_superfluous([a0,a1,a2,a3], 3)
        True
        >>> is_superfluous([a0,a1,a2,a3], 0)
        True
        >>> is_superfluous([a0,a1,a2,a3], 1)
        False
    '''
    pass



## Problem 16
def is_independent(L):
    '''
    input: a list L of vectors (using vec class)
    output: True if the vectors form a linearly independent list.
    >>> vlist = [Vec({0, 1, 2},{0: 1, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 0})]
    >>> is_independent(vlist)
    False
    >>> is_independent(vlist[:3])
    True
    >>> is_independent(vlist[:2])
    True
    >>> is_independent(vlist[1:4])
    True
    >>> is_independent(vlist[2:5])
    True
    >>> is_independent(vlist[2:6])
    False
    >>> is_independent(vlist[1:3])
    True
    >>> is_independent(vlist[5:])
    True
    '''
    pass



## Problem 17
def superset_basis(S, L):
    '''
    Input: 
        - S: linearly independent list of Vec instances
        - L: list of Vec instances such that every vector in S is in Span(L)
    Output:
        Linearly independent list T containing all vectors (as instances of Vec)
        such that the span of T is the span of L (i.e. T is a basis for the span
        of L).
    Example:
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
        >>> superset_basis([a0, a3], [a0, a1, a2]) == [Vec({'a', 'c', 'b', 'd'},{'a': 1}), Vec({'a', 'c', 'b', 'd'},{'b':1}),Vec({'a', 'c', 'b', 'd'},{'c': 1})]
        True
    '''
    pass



## Problem 18
def exchange(S, A, z):
    '''
    Input:
        - S: a list of vectors, as instances of your Vec class
        - A: a list of vectors, each of which are in S, with len(A) < len(S)
        - z: an instance of Vec such that A+[z] is linearly independent
    Output: a vector w in S but not in A such that Span S = Span ({z} U S - {w})
    Example:
        >>> S = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]]
        >>> A = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]]
        >>> z = list2vec([0,2,1,1])
        >>> exchange(S, A, z) == Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 1, 3: 0})
        True
    '''
    pass

