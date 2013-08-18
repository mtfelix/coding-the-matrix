
from GF2 import one
from math import sqrt, pi
from matutil import coldict2mat
from solver import solve
from vec import Vec

from hw4 import *

vec1 = Vec({0,1,2,3},{1:one,3:one})
vec2 = Vec({0,1,2,3},{2:one})
vec3 = Vec({0,1,2,3},{0:one,3:one})
vec4 = Vec({0,1,2,3},{0:one,1:one,2:one,3:one})

veclist = [vec1,vec2,vec3,vec4]

avec = Vec({0,1,2,3},{0:one,1:one})
bvec = Vec({0,1,2,3},{0:one,2:one})
cvec = Vec({0,1,2,3},{0:one})

zerovec = Vec({0,1,2,3},{})

for i1 in range(0,2):
    for i2 in range(0,2):
        for i3 in range(0,2):
            for i4 in range(0,2):
                if i1*vec1+i2*vec2+i3*vec3+i4*vec4 == avec:
                    print ("avec:")
                    print (i1,i2,i3,i4)
                if i1*vec1+i2*vec2+i3*vec3+i4*vec4 == bvec:
                    print ("bvec:")
                    print (i1,i2,i3,i4)
                if i1*vec1+i2*vec2+i3*vec3+i4*vec4 == cvec:
                    print ("cvec:")
                    print (i1,i2,i3,i4)


#problem 9
vec_a1 = Vec({0,1,2,3},{0:one,1:one,2:one,3:one})
vec_a2 = Vec({0,1,2,3},{0:one,2:one})
vec_a3 = Vec({0,1,2,3},{1:one,2:one})
vec_a4 = Vec({0,1,2,3},{1:one,3:one})

vec_b1 = Vec({0,1,2,3},{3:one})
vec_b2 = Vec({0,1,2,3},{2:one})
vec_b3 = Vec({0,1,2,3},{0:one,1:one,3:one})
vec_b4 = Vec({0,1,2,3},{0:one,1:one,2:one,3:one})

vec_c1 = Vec({0,1,2,3,4},{0:one,1:one,3:one,4:one})
vec_c2 = Vec({0,1,2,3,4},{2:one})
vec_c3 = Vec({0,1,2,3,4},{2:one,3:one,4:one})
vec_c4 = Vec({0,1,2,3,4},{0:one,2:one,3:one,4:one})
vec_c5 = Vec({0,1,2,3,4},{0:one,1:one,2:one,3:one,4:one})

veclist_a = [vec_a1,vec_a2,vec_a3,vec_a4]
veclist_b = [vec_b1,vec_b2,vec_b3,vec_b4]
veclist_c = [vec_c1,vec_c2,vec_c3,vec_c4,vec_c5]

from itertools import *
A = [0,1]
zerovec = Vec({0,1,2,3},{})
zerovec_c = Vec({0,1,2,3,4},{})
    
for Alpha in product(A,repeat=len(veclist_c)):
    if sum(Alpha) > 0:
        if sum([Alpha[i]*veclist_c[i] for i in range(len(veclist_c))]) == zerovec_c:
            #print(Alpha)
            #exit()
            pass

# problem 16
a0 = Vec({'a','b','c','d'}, {'a':1})
a1 = Vec({'a','b','c','d'}, {'b':1})
a2 = Vec({'a','b','c','d'}, {'c':1})
a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
L = [a0,a1,a2,a3]
print(is_superfluous(L, 3))
#True
print(is_superfluous([a0,a1,a2,a3], 3))
#True
print(is_superfluous([a0,a1,a2,a3], 0))
#True
print(is_superfluous([a0], 0))
#False
