from vec import *
from hw2 import *
D = {'a','b','c'}
v1 = Vec(D, {'a': 1})
v2 = Vec(D, {'a': 0, 'b': 1})
v3 = Vec(D, {        'b': 2})
v4 = Vec(D, {'a': 10, 'b': 10})
vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 1})
#True
print(vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 12}))
