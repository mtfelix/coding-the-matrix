from mat import Mat
from vec import Vec
from GF2 import one

#No operations should mutate the input matrices, except setitem.
Mat(({'a','b'}, {0,1}), {('a',1):0}) == Mat(({'a','b'}, {0,1}), {('b',1):0})
#True
A = Mat(({'a','b'}, {0,1}), {('a',1):2, ('b',0):1})
B = Mat(({'a','b'}, {0,1}), {('a',1):2, ('b',0):1, ('b',1):0})
C = Mat(({'a','b'}, {0,1}), {('a',1):2, ('b',0):1, ('b',1):5}) 
print(A == C)
#True
#>>> A == C
#False
#>>> A == Mat(({'a','b'}, {0,1}), {('a',1):2, ('b',0):1})
#True