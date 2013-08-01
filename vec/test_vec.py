"""
    
>>> from vec import Vec
    
For getitem(v,d):

Return the value of entry d in v.
Be sure getitem(v,d) returns 0 if d is not represented in v.f.
    
>>> v = Vec({'a','b','c', 'd'},{'a':2,'c':1,'d':3})
>>> v['d']
3
>>> v['b']
0

For setitem(v,d,val):

Set the element of v with label d to be val.
setitem(v,d,val) should set the value for key d even if d
  is not previously represented in v.f. 

>>> v = Vec({'a', 'b', 'c'}, {'b':0})
>>> v['b'] = 5
>>> v['b']
5
>>> v['a'] = 1
>>> v['a']
1

For equal(u,v):
    
Return true iff u is equal to v.
Because of sparse representation, it is not enough to compare dictionaries

>>> Vec({'a', 'b', 'c'}, {'a':0}) == Vec({'a', 'b', 'c'}, {'b':0})
True

Be sure that equal(u, v) check equalities for all keys from u.f and v.f even if some keys in u.f do not exist in v.f (or vice versa)

>>> Vec({'x','y','z'},{'y':1,'x':2}) == Vec({'x','y','z'},{'y':1,'z':0})
False
>>> Vec({'a','b','c'}, {'a':0,'c':1}) == Vec({'a','b','c'}, {'a':0,'c':1,'b':4})
False
    
For add(u, v):

Returns the addition of the two vectors. 
Be sure to add together values for all keys from u.f and v.f even if some keys in u.f do not exist in v.f (or vice versa)
    
>>> a = Vec({'a','e','i','o','u'}, {'a':0,'e':1,'i':2})
>>> b = Vec({'a','e','i','o','u'}, {'o':4,'u':7})
>>> c = Vec({'a','e','i','o','u'}, {'a':0,'e':1,'i':2,'o':4,'u':7}) 
>>> a + b == c
True
>>> d = Vec({'x','y','z'}, {'x':2,'y':1})
>>> e = Vec({'x','y','z'}, {'z':4,'y':-1})
>>> f = Vec({'x','y','z'}, {'x':2,'y':0,'z':4})
>>> d + e == f
True
>>> b + Vec({'a','e','i','o','u'}, {}) == b
True
    
For dot(u, v):
    
Returns the dot product of the two vectors.

>>> u1 = Vec({'a','b'}, {'a':1, 'b':2})
>>> u2 = Vec({'a','b'}, {'b':2, 'a':1})
>>> u1*u2
5
>>> v1 = Vec({'p','q','r','s'}, {'p':2,'s':3,'q':-1,'r':0})
>>> v2 = Vec({'p','q','r','s'}, {'p':-2,'r':5})
>>> v1*v2
-4
>>> w1 = Vec({'a','b','c'}, {'a':2,'b':3,'c':4})
>>> w2 = Vec({'a','b','c'}, {'a':12,'b':8,'c':6})
>>> w1*w2
72

For scalar_mul(v, alpha):
    
Returns the scalar-vector product alpha times v.

>>> zero = Vec({'x','y','z','w'}, {})
>>> u = Vec({'x','y','z','w'},{'x':1,'y':2,'z':3,'w':4})
>>> 0*u == zero
True
>>> 1*u == u
True
>>> 0.5*u == Vec({'x','y','z','w'},{'x':0.5,'y':1,'z':1.5,'w':2})
True
    
For neg(v):

Returns the negation of vector v. Be sure that all values in v.f are negated
>>> zero = Vec({'x','y','z'}, {})
>>> -zero == zero
True
>>> v = Vec({0,1,2,3,4,'a'}, {0:1,1:-1,2:-1,3:1})
>>> -v == Vec({0,1,2,3,4,'a'}, {0:-1,1:1,2:1,3:-1}) 
True
>>> -(-v) == v
True
>>> v == -v
False

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
