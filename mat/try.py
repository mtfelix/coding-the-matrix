from mat import Mat
from vec import Vec
from GF2 import one

v1 = Vec({1, 2, 3}, {1: 1, 2: 8})
M1 = Mat(({1, 2, 3}, {1, 2, 3}), {(1, 2): 2, (2, 1):-1, (3, 1): 1, (3, 3): 7})
print(v1*M1 == Vec({1, 2, 3},{1: -8, 2: 2, 3: 0}))
#True
print(v1 == Vec({1, 2, 3}, {1: 1, 2: 8}))
#True
print(M1 == Mat(({1, 2, 3}, {1, 2, 3}), {(1, 2): 2, (2, 1):-1, (3, 1): 1, (3, 3): 7}))
#True
v2 = Vec({'a','b'}, {})
M2 = Mat(({'a','b'}, {0, 2, 4, 6, 7}), {})
print(v2*M2 == Vec({0, 2, 4, 6, 7},{}))
#True