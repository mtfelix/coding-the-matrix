from itertools import *
from vec import Vec
from GF2 import one
from hw2 import *
D = {'a', 'b', 'c'}
L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
print(len(GF2_span(D, L)))
#    4
print( Vec(D, {}) in GF2_span(D, L))
#    True
Vec(D, {'b': one}) in GF2_span(D, L)
#    True
Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
#    True
print(Vec(D, {x:one for x in D}) in GF2_span(D, L))
#   True

print (GF2_span(D,[]))