# version code 941
########                                     ######## 
# Hi there, curious student.                        #
#                                                   #
# This submission script runs some tests on your    #
# code and then uploads it to Coursera for grading. #
#                                                   #
# Changing anything in this script might cause your #
# submissions to fail.                              #
########                                     ########

import io, os, sys, doctest, traceback, importlib, urllib.request, urllib.parse, urllib.error, base64, hashlib, random, ast

SUBMIT_VERSION      = "941"
URL                 = 'matrix-001'
part_friendly_names = ['Span of Vectors over R, A', 'Span of Vectors over R, B', 'Span of Vectors over GF2 A', 'Span of Vectors over GF2 B', 'Linear Dependence over R A', 'Linear Dependence over R B', 'Superfluous vector', '4 linearly dependent vectors, every 3 are independent', 'Linear Dependence over GF(2) A', 'Linear Dependence over GF(2) B', 'Exchange Lemma for Vectors over $\\R$', 'Exchange Lemma for Vectors over GF(2)', 'rep2vec', 'vec2rep', 'Superfluous Vector in Python', 'is_independent in Python', 'Superset Basis Lemma in Python', 'Exchange Lemma in Python']
groups              = [[('38CzLjeEQsHBI7ul30blZEB0dWTqeOde', 'Span of Vectors over R, A', '>>> print(test_format(rep_1))\n>>> print(test_format(rep_2))\n>>> print(test_format(rep_3))\n')], [('38CzLjeEQsHBI7ulP2TdWw4Zy0bNkAfs', 'Span of Vectors over R, B', '>>> print(test_format(lin_comb_coefficients_1))\n>>> print(test_format(lin_comb_coefficients_2))\n>>> print(test_format(lin_comb_coefficients_3))\n>>> print(test_format(lin_comb_coefficients_4))\n')], [('38CzLjeEQsHBI7ulyG3jIPmBZ6BXOVIg', 'Span of Vectors over GF2 A', '>>> print(test_format(gf2_rep_1))\n>>> print(test_format(gf2_rep_2))\n>>> print(test_format(gf2_rep_3))\n')], [('38CzLjeEQsHBI7ulEwMeTlewPMQfhwFI', 'Span of Vectors over GF2 B', '>>> v1 = Vec(set(range(8)), {0:one, 1:one})\n>>> v2 = Vec(set(range(8)), {1:one, 2:one})\n>>> v3 = Vec(set(range(8)), {0:one, 3:one})\n>>> v4 = Vec(set(range(8)), {1:one, 4:one})\n>>> v5 = Vec(set(range(8)), {2:one, 4:one})\n>>> v6 = Vec(set(range(8)), {3:one, 4:one})\n>>> v7 = Vec(set(range(8)), {5:one, 7:one})\n>>> v8 = Vec(set(range(8)), {6:one, 7:one})\n>>> veclist = [v1, v2, v3, v4, v5, v6, v7, v8]\n>>> print(test_format(sum([x*y for x,y in zip(gf2_lc_rep_1, veclist)])))\n>>> print(test_format(sum([x*y for x,y in zip(gf2_lc_rep_2, veclist)])))\n>>> print(test_format(sum([x*y for x,y in zip(gf2_lc_rep_3, veclist)])))\n>>> print(test_format(sum([x*y for x,y in zip(gf2_lc_rep_4, veclist)])))\n')], [('38CzLjeEQsHBI7ul7IEtQTHBp6fp3fSA', 'Linear Dependence over R A, Part 1', '>>> p11 = Vec({0, 1, 2},{0: 1, 1: 2, 2: 0})\n>>> p12 = Vec({0, 1, 2},{0: 2, 1: 4, 2: 1})\n>>> p13 = Vec({0, 1, 2},{0: 0, 1: 0, 2: -1})\n>>> b = lin_dep_R_1[0]*p11 + lin_dep_R_1[1]*p12 + lin_dep_R_1[2]*p13\n>>> print(test_format(b*b < 1E-15))\n'), ('38CzLjeEQsHBI7ulkdczjHT5aM3RMfM2', 'Linear Dependence over R A, Part 2', '>>> p21 = Vec({0, 1, 2},{0: 2, 1: 4, 2: 0})\n>>> p22 = Vec({0, 1, 2},{0: 8, 1: 16, 2: 4})\n>>> p23 = Vec({0, 1, 2},{0: 0, 1: 0, 2: 7})\n>>> b = lin_dep_R_2[0]*p21 + lin_dep_R_2[1]*p22 + lin_dep_R_2[2]*p23\n>>> print(test_format(b*b < 1E-15))\n'), ('38CzLjeEQsHBI7uldnk8EwmB85vl1f98', 'Linear Dependence over R A, Part 3', '>>> p31 = Vec({0, 1, 2},{0: 0, 1: 0, 2: 5})\n>>> p32 = Vec({0, 1, 2},{0: 1, 1: 34, 2: 2})\n>>> p33 = Vec({0, 1, 2},{0: 123, 1: 456, 2: 789})\n>>> p34 = Vec({0, 1, 2},{0: -3, 1: -6, 2: 0})\n>>> p35 = Vec({0, 1, 2},{0: 1, 1: 2, 2: 0.5})\n>>> b = lin_dep_R_3[0]*p31 + lin_dep_R_3[1]*p32 + lin_dep_R_3[2]*p33 + lin_dep_R_3[3]*p34 + lin_dep_R_3[4]*p35\n>>> print(test_format(b*b < 1E-15))\n')], [('38CzLjeEQsHBI7uloDoR4lt0F9TH5F7Y', 'Linear Dependence over R B, Part 1', '>>> v11 = Vec({0, 1, 2},{0: 1, 1: 2, 2: 3})\n>>> v12 = Vec({0, 1, 2},{0: 4, 1: 5, 2: 6})\n>>> v13 = Vec({0, 1, 2},{0: 1, 1: 1, 2: 1})\n>>> b = linear_dep_R_1[0]*v11 + linear_dep_R_1[1]*v12 + linear_dep_R_1[2]*v13 \n>>> print(test_format(b*b < 1E-15))\n'), ('38CzLjeEQsHBI7ulSyd20igj60x7cjb4', 'Linear Dependence over R B, Part 2', '>>> v21 = Vec({0, 1, 2, 3},{0: 0, 1: -1, 2: 0, 3: -1})\n>>> v22 = Vec({0, 1, 2, 3},{0: 3.141592653589793, 1: 3.141592653589793, 2: 3.141592653589793, 3: 3.141592653589793})\n>>> v23 = Vec({0, 1, 2, 3},{0: -1.4142135623730951, 1: 1.4142135623730951, 2: -1.4142135623730951, 3: 1.4142135623730951})\n>>> b = linear_dep_R_2[0]*v21 + linear_dep_R_2[1]*v22 + linear_dep_R_2[2]*v23\n>>> print(test_format(b*b < 1E-15))\n'), ('38CzLjeEQsHBI7ulXNJXazQsSo9z7Vz0', 'Linear Dependence over R B, Part 3', '>>> v31 = Vec({0, 1, 2, 3, 4},{0: 1, 1: -1, 2: 0, 3: 0, 4: 0})\n>>> v32 = Vec({0, 1, 2, 3, 4},{0: 0, 1: 1, 2: -1, 3: 0, 4: 0})\n>>> v33 = Vec({0, 1, 2, 3, 4},{0: 0, 1: 0, 2: 1, 3: -1, 4: 0})\n>>> v34 = Vec({0, 1, 2, 3, 4},{0: 0, 1: 0, 2: 0, 3: 1, 4: -1})\n>>> v35 = Vec({0, 1, 2, 3, 4},{0: -1, 1: 0, 2: 0, 3: 0, 4: 1})\n>>> b = sum(x*y for x,y in zip(linear_dep_R_3,[v31,v32,v33,v34,v35]))\n>>> print(test_format(b*b < 1E-15))\n')], [('38CzLjeEQsHBI7ulq3a19UB6397Tnc0d', 'Superfluous vector', '>>> def sup_vec_check(u, v, w, sum_to):\n...     if sum_to == \'u\':\n...         return v*v_vec + w*w_vec == u_vec\n...     elif sum_to == \'v\':\n...         return u*u_vec + w*w_vec == v_vec\n...     elif sum_to == \'w\':\n...         return u*u_vec + v*v_vec == w_vec\n...     else:\n...         return "SUM_TO IS NOT \'u\', \'v\', or \'w\'"\n>>> u_vec = Vec({0,1,2,3,4},{0:3, 1:9, 2:6, 3:5, 4:5})\n>>> v_vec = Vec({0,1,2,3,4},{0:4, 1:10, 2:6, 3:6, 4:8})\n>>> w_vec = Vec({0,1,2,3,4},{0:1, 1:1, 2:0, 3:1, 4:3})\n>>> print(test_format(sup_vec_check(u, v, w, sum_to)))\n')], [('38CzLjeEQsHBI7ulIc8rRpFit8r8RFq2', '4 linearly dependent vectors, every 3 are independent', '>>> import solver\n>>> import matutil\n>>> import GF2\n>>> def _which_field(v):\n...     for x in v.f.values():\n...         if x != 0:\n...             if isinstance(x, GF2.One):\n...                 return 1\n...             return 2\n...     return 0\n>>> def _check(wf, r):\n...     #check if zero vector\n...     if wf == 1:\n...         return r*r == 0\n...     return r*r < 1e-20\n>>> def _test1(wf, L):\n...     if len(L) != 4: return False\n...     wf = _which_field(L[0])\n...     if wf == 0: return False\n...     A = matutil.coldict2mat(L[1:])\n...     u = solver.solve(A, L[0])\n...     return _check(wf, A*u-L[0])\n>>> def _test2(wf, L):\n...     for i in range(4):\n...         L1 = L[:i]+L[i+1:]\n...         for j in range(3):\n...             v = L1[j]\n...             A = matutil.coldict2mat(L1[:j]+L1[j+1:])\n...             u = solver.solve(A, v)\n...             if _check(wf, A*u-v): return False\n...     return True\n>>> def _deptest(L):\n...     if len(L) != 4: return False\n...     wf = _which_field(L[0])\n...     return _test1(wf, L) and _test2(wf, L)\n>>> print(test_format(_deptest([indep_vec_1, indep_vec_2, indep_vec_3, indep_vec_4])))\n')], [('38CzLjeEQsHBI7ulmEfHHVCa6npnXg2c', 'Linear Dependence over GF(2) A', '>>> from vec import *\n>>> from GF2 import one\n>>> L1 = [Vec({0, 1, 2, 3},{0: one, 1: one, 2: one, 3: one}), Vec({0, 1, 2, 3},{0: one, 1: 0, 2: one, 3: 0}), Vec({0, 1, 2, 3},{0: 0, 1: one, 2: one, 3: 0}), Vec({0, 1, 2, 3},{0: 0, 1: one, 2: 0, 3: one})]\n>>> print(test_format(sum([zero_comb_1[i]*L1[i] for i in range(len(L1))])))\n>>> L2 = [Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 0, 3: one}), Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: one, 3: 0}), Vec({0, 1, 2, 3},{0: one, 1: one, 2: 0, 3: one}), Vec({0, 1, 2, 3},{0: one, 1: one, 2: one, 3: one})]\n>>> print(test_format(sum([zero_comb_2[i]*L2[i] for i in range(len(L2))])))\n>>> L3 =[Vec({0, 1, 2, 3, 4},{0: one, 1: one, 2: 0, 3: one, 4: one}), Vec({0, 1, 2, 3, 4},{0: 0, 1: 0, 2: one, 3: 0, 4: 0}), Vec({0, 1, 2, 3, 4},{0: 0, 1: 0, 2: one, 3: one, 4: one}), Vec({0, 1, 2, 3, 4},{0: one, 1: 0, 2: one, 3: one, 4: one}), Vec({0,1,2,3,4},{0: one, 1: one, 2: one, 3: one, 4: one})]\n>>> print(test_format(sum([zero_comb_3[i]*L3[i] for i in range(len(L3))])))\n')], [('38CzLjeEQsHBI7ulo70J6go2Qjozlvxh', 'Linear Dependence over GF(2) B', '>>> v1 = Vec(set(range(8)), {0:one, 1:one})\n>>> v2 = Vec(set(range(8)), {1:one, 2:one})\n>>> v3 = Vec(set(range(8)), {0:one, 3:one})\n>>> v4 = Vec(set(range(8)), {1:one, 4:one})\n>>> v5 = Vec(set(range(8)), {2:one, 4:one})\n>>> v6 = Vec(set(range(8)), {3:one, 4:one})\n>>> v7 = Vec(set(range(8)), {5:one, 7:one})\n>>> v8 = Vec(set(range(8)), {6:one, 7:one})\n>>> print(test_format(any(sum_to_zero_1)))\n>>> l1 = [v1,v2,v3,v4,v5]\n>>> print(test_format(sum([x*y for x,y in zip(sum_to_zero_1, l1)])))\n>>> print(test_format(any(sum_to_zero_2)))\n>>> l2 = [v1,v2,v3,v4,v5,v7,v8]\n>>> print(test_format(sum([x*y for x,y in zip(sum_to_zero_2, l2)])))\n>>> print(test_format(any(sum_to_zero_3)))\n>>> l3 = [v1, v2, v3, v4, v6]\n>>> print(test_format(sum([x*y for x,y in zip(sum_to_zero_3, l3)])))\n>>> print(test_format(any(sum_to_zero_4)))\n>>> l4 = [v1, v2, v3, v5, v6, v7, v8]\n>>> print(test_format(sum([x*y for x,y in zip(sum_to_zero_4, l4)])))\n')], [('38CzLjeEQsHBI7ulDXKk6RdQmxMop7cS', 'Exchange Lemma for Vectors over $\\R$', '>>> print(test_format(exchange_1 in [[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]))\n>>> print(test_format(exchange_2 in [[0,0,1,0,0],[0,0,0,0,1]]))\n>>> print(test_format(exchange_3 in [[0,0,1,0,0],[0,0,0,0,1]]))\n')], [('38CzLjeEQsHBI7uluPlRZG2nzVZ1wL4i', 'Exchange Lemma for Vectors over GF(2)', '>>> print(test_format(replace_1))\n>>> print(test_format(replace_2))\n>>> print(test_format(replace_3))\n')], [('38CzLjeEQsHBI7ullHkKg2Cl7ob6Ah3q', 'rep2vec', ">>> from vec import Vec\n>>> from vecutil import list2vec\n>>> a0 = Vec({'a','b','c','d'}, {'a':1})\n>>> a1 = Vec({'a','b','c','d'}, {'b':1})\n>>> a2 = Vec({'a','b','c','d'}, {'c':1})\n>>> print(test_format(rep2vec(Vec({0,1,2}, {0:2, 1:4, 2:6}), [a0,a1,a2])))\n>>> a0 = list2vec([3,1,2])\n>>> a1 = list2vec([2,1,3])\n>>> a2 = list2vec([1,3,2])\n>>> b = list2vec([1,1,1])\n>>> print(test_format(rep2vec(b, [a0,a1,a2])))\n")], [('38CzLjeEQsHBI7ulhV7UpqFZVDgvaGAS', 'vec2rep', ">>> from vec import Vec\n>>> from vecutil import list2vec\n>>> a0 = Vec({'a','b','c','d'}, {'a':1})\n>>> a1 = Vec({'a','b','c','d'}, {'b':1})\n>>> a2 = Vec({'a','b','c','d'}, {'c':1})\n>>> print(test_format(vec2rep([a0,a1,a2], Vec({'a','b','c','d'}, {'a':3, 'c':-2}))))\n>>> a0 = list2vec([4,6,2])\n>>> a1 = list2vec([7,3,5])\n>>> a2 = list2vec([12,75,2])\n>>> b = list2vec([4,6,8])\n>>> print(test_format(vec2rep([a0,a1,a2], b)))\n")], [('38CzLjeEQsHBI7ulfChR31W2PemQyhog', 'Superfluous Vector in Python', ">>> from vec import Vec\n>>> a0 = Vec({'a','b','c','d'}, {'a':1})\n>>> a1 = Vec({'a','b','c','d'}, {'b':1})\n>>> a2 = Vec({'a','b','c','d'}, {'c':1})\n>>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})\n>>> print(test_format(is_superfluous([a0,a1,a2,a3], 3)))\n>>> print(test_format(is_superfluous([a0,a1,a2,a3], 0)))\n>>> print(test_format(is_superfluous([a0,a1,a2,a3], 1)))\n")], [('38CzLjeEQsHBI7ulAnZS7bWmGdLcOs4c', 'is_independent in Python', ">>> from vec import Vec\n>>> a0 = Vec({'a','b','c','d'}, {'a':1})\n>>> a1 = Vec({'a','b','c','d'}, {'b':1})\n>>> a2 = Vec({'a','b','c','d'}, {'c':1})\n>>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})\n>>> print(test_format(is_independent([a0, a1, a2])))\n>>> print(test_format(is_independent([a0, a2, a3])))\n>>> print(test_format(is_independent([a0, a1, a3])))\n>>> print(test_format(is_independent([a0, a1, a2, a3])))\n")], [('38CzLjeEQsHBI7uly2YRCrNS8OShv9S3', 'Superset Basis Lemma in Python', ">>> from vec import Vec\n>>> from vecutil import list2vec\n>>> a0 = Vec({'a','b','c','d'}, {'a':1})\n>>> a1 = Vec({'a','b','c','d'}, {'b':1})\n>>> a2 = Vec({'a','b','c','d'}, {'c':1})\n>>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})\n>>> print(test_format(superset_basis([a0, a3], [a0, a1, a2])))\n>>> S = [list2vec(v) for v in [[0, 1, 1, 0], [1, 0, 0, 1]]]\n>>> L = [list2vec(v) for v in [[1, 1, 1, 1], [1, 0, 0, 0], [0, 0, 0, 1]]]\n>>> print(test_format(superset_basis(S, L)))\n>>> S = [list2vec(v) for v in [[0, 5, 3], [0, 2, 2]]] \n>>> L = [list2vec(v) for v in [[1, 1, 1], [0, 1, 1], [0, 0, 1]]]\n>>> print(test_format(superset_basis(S, L)))\n>>> S = [list2vec(v) for v in [[0, 5, 3], [0, 2, 2], [1, 5, 7]]] \n>>> L = [list2vec(v) for v in [[1, 1, 1], [0, 1, 1], [0, 0, 1]]]\n>>> print(test_format(superset_basis(S, L)))\n")], [('38CzLjeEQsHBI7ulxxZ47EOMOqincfiC', 'Exchange Lemma in Python', '>>> from vecutil import list2vec\n>>> S=[list2vec(v) for v in [[0,0,5,3] , [2,0,1,3],[0,0,1,0],[1,2,3,4]]]\n>>> A=[list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]]\n>>> z=list2vec([0,2,1,1])\n>>> print(test_format((exchange(S, A, z) == list2vec([0,0,1,0])) or (exchange(S, A, z) == list2vec([1,2,3,4]))))\n>>> S = [list2vec(v) for v in [[0,0,4,9],[7,0,5,3],[0,3,4,5],[0,1,2,0]]]\n>>> A = [list2vec(v) for v in [[0,0,4,9],[0,3,4,5],]]\n>>> z = list2vec([1,0,0,0])\n>>> print(test_format((exchange(S, A, z) == list2vec([7,0,5,3])) or (exchange(S, A, z) == list2vec([0,1,2,0]))))\n>>> S = [list2vec(v) for v in [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]]\n>>> A = [list2vec(v) for v in [[1,0,0,0],[0,0,0,1]]]\n>>> z = list2vec([0,0,2,0])\n>>> print(test_format(exchange(S, A, z)))\n>>> S = [list2vec(v) for v in [[3,67,8,4],[0,6,3,4],[5,9,5,2],[67,342,567,5],[9,5,9,0],[7,4,5,3],[34,7,65,3]]]\n>>> A = [list2vec(v) for v in [[3,67,8,4],[0,6,3,4]]]\n>>> z = list2vec([0,0,0,1])\n>>> print(test_format((exchange(S, A, z) == list2vec([9,5,9,0])) or (exchange(S, A, z) == list2vec([7,4,5,3])) or (exchange(S, A, z) == list2vec([34, 7, 65, 3]))))\n>>> print(test_format((exchange(S, A, z) == list2vec([5,9,5,2])) or (exchange(S, A, z) == list2vec([67,342,567,5]))))\n')]]
source_files        = ['hw4.py'] * len(sum(groups,[]))

try:
    import hw4 as solution
    test_vars = vars(solution).copy()
except Exception as exc:
    print(exc)
    print("!! It seems like you have an error in your stencil file. Please fix before submitting.")
    sys.exit(1)

def find_lines(varname):
    return list(filter(lambda l: varname in l, list(open("python_lab.py"))))

def find_line(varname):
    ls = find_lines(varname)
    return ls[0] if len(ls) else None


def use_comprehension(varname):
    lines = find_lines(varname)
    for line in lines:
        try:
            if "comprehension" in ast.dump(ast.parse(line)):
                return True
        except: pass
    return False

def double_comprehension(varname):
    line = find_line(varname)
    return ast.dump(ast.parse(line)).count("comprehension") == 2

def line_contains_substr(varname, word):
    lines = find_line(varname)
    for line in lines:
        if word in line:
            return True
    return False

def test_format(obj, precision=6):
    tf = lambda o: test_format(o, precision)
    delimit = lambda o: ', '.join(o)
    otype = type(obj)
    if otype is str:
        return "'%s'" % obj
    elif otype is float or otype is int:
        if otype is int:
            obj = float(obj)
        if -0.000001 < obj < 0.000001:
            obj = 0.0
        fstr = '%%.%df' % precision
        return fstr % obj
    elif otype is set:
        if len(obj) == 0:
            return 'set()'
        return '{%s}' % delimit(sorted(map(tf, obj)))
    elif otype is dict:
        return '{%s}' % delimit(sorted(tf(k)+': '+tf(v) for k,v in obj.items()))
    elif otype is list:
        return '[%s]' % delimit(map(tf, obj))
    elif otype is tuple:
        return '(%s%s)' % (delimit(map(tf, obj)), ',' if len(obj) is 1 else '')
    elif otype.__name__ in ['Vec','Mat']:
        entries = tf({x:obj.f[x] for x in obj.f if tf(obj.f[x]) != tf(0)})
        return '%s(%s, %s)' % (otype.__name__, test_format(obj.D), entries)
    else:
        return str(obj)



def output(tests):
    dtst = doctest.DocTestParser().get_doctest(tests, test_vars, 0, '<string>', 0)
    runner = ModifiedDocTestRunner()
    runner.run(dtst)
    return runner.results

test_vars['test_format'] = test_vars['tf'] = test_format
test_vars['find_lines'] = find_lines
test_vars['find_line'] = find_line
test_vars['use_comprehension'] = use_comprehension
test_vars['double_comprehension'] = double_comprehension
test_vars['line_contains_substr'] = line_contains_substr

base_url = '://class.coursera.org/%s/assignment/' % URL
protocol = 'https'
colorize = False
verbose  = False

class ModifiedDocTestRunner(doctest.DocTestRunner):
    def __init__(self, *args, **kwargs):
        self.results = []
        return super(ModifiedDocTestRunner, self).__init__(*args, checker=OutputAccepter(), **kwargs)
    
    def report_success(self, out, test, example, got):
        self.results.append(got)
    
    def report_unexpected_exception(self, out, test, example, exc_info):
        exf = traceback.format_exception_only(exc_info[0], exc_info[1])[-1]
        self.results.append(exf)

class OutputAccepter(doctest.OutputChecker):
    def check_output(self, want, got, optionflags):
        return True

def submit(parts_string, login, password):   
    print('= Coding the Matrix Homework and Lab Submission')
    
    if not login:
        login = login_prompt()
    if not password:
        password = password_prompt()
    if not parts_string: 
        parts_string = parts_prompt()

    parts = parse_parts(parts_string)

    if not all([parts, login, password]):
        return

    for sid, name, part_tests in parts:
        sys.stdout.write('== Submitting "%s"' % name)

        if 'DEV' in os.environ: sid += '-dev'

        (login, ch, state, ch_aux) = get_challenge(login, sid)

        if not all([login, ch, state]):
            print('  !! Error: %s\n' % login)
            return

        # to stop Coursera's strip() from doing anything, we surround in parens
        results  = output(part_tests)
        prog_out = '(%s)' % ''.join(map(str.rstrip, results))
        token    = challenge_response(login, password, ch)
        src      = source(sid)

        feedback = submit_solution(login, token, sid, prog_out, src, state, ch_aux)

        if len(feedback.strip()) > 0:
            if colorize:
                good = 'incorrect' not in feedback.lower()
                print(': \033[1;3%dm%s\033[0m' % (2 if good else 1, feedback.strip()))
            else:
                print(': %s' % feedback.strip())
        
        if verbose:
            for t, r in zip(part_tests.split('\n'), results):
                sys.stdout.write('%s\n%s' % (t, r))
            sys.stdout.write('\n\n')


def login_prompt():
    return input('Login email address: ')


def password_prompt():
    return input("One-time password from the assignment page (NOT your own account's password): ")


def parts_prompt():
    print('These are the assignment parts that you can submit:')

    for i, name in enumerate(part_friendly_names):
        print('  %d) %s' % (i+1, name))

    return input('\nWhich parts do you want to submit? (Ex: 1, 4-7): ')

def parse_parts(string):
    def extract_range(s):
        s = s.split('-')
        if len(s) == 1: return [int(s[0])]
        else: return list(range(int(s[0]), 1+int(s[1])))
    parts = map(extract_range, string.split(','))
    flat_parts = sum(parts, [])
    return sum(list(map(lambda p: groups[p-1], flat_parts)),[])

def get_challenge(email, sid):
    """Gets the challenge salt from the server. Returns (email,ch,state,ch_aux)."""
    params = {'email_address': email, 'assignment_part_sid': sid, 'response_encoding': 'delim'}

    challenge_url = '%s%schallenge' % (protocol, base_url)
    data = urllib.parse.urlencode(params).encode('utf-8')
    req  = urllib.request.Request(challenge_url, data)
    resp = urllib.request.urlopen(req)
    text = resp.readall().decode('utf-8').strip().split('|')

    if len(text) != 9:
        print('  !! %s' % '|'.join(text))
        sys.exit(1)
  
    return tuple(text[x] for x in [2,4,6,8])


def challenge_response(email, passwd, challenge):
    return hashlib.sha1((challenge+passwd).encode('utf-8')).hexdigest()


def submit_solution(email_address, ch_resp, sid, output, source, state, ch_aux):
    b64ize = lambda s: str(base64.encodebytes(s.encode('utf-8')), 'ascii')

    values = { 'assignment_part_sid' : sid
             , 'email_address'       : email_address
             , 'submission'          : b64ize(output) 
             , 'submission_aux'      : b64ize(source)
             , 'challenge_response'  : ch_resp
             , 'state'               : state
             }

    submit_url = '%s%ssubmit' % (protocol, base_url)
    data     = urllib.parse.urlencode(values).encode('utf-8')
    req      = urllib.request.Request(submit_url, data)
    response = urllib.request.urlopen(req)

    return response.readall().decode('utf-8').strip()


def source(sid):
    src = ['# submit version: %s' % SUBMIT_VERSION]
    for fn in set(source_files):
        with open(fn) as source_f:
            src.append(source_f.read())
    return '\n\n'.join(src)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    env = os.environ
    helps = [ 'numbers or ranges of tasks to submit'
            , 'the email address on your Coursera account'
            , 'your ONE-TIME password'
            , 'use ANSI color escape sequences'
            , 'show the test\'s interaction with your code'
            , 'use an encrypted connection to Coursera'
            , 'use an unencrypted connection to Coursera'
            ]
    parser.add_argument('tasks',      default=env.get('COURSERA_TASKS'), nargs='*', help=helps[0])
    parser.add_argument('--email',    default=env.get('COURSERA_EMAIL'),            help=helps[1])
    parser.add_argument('--password', default=env.get('COURSERA_PASS'),             help=helps[2])
    parser.add_argument('--colorize', default=False, action='store_true',           help=helps[3])
    parser.add_argument('--verbose',  default=False, action='store_true',           help=helps[4])
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--https', dest="protocol", const="https", action="store_const", help=helps[-2])
    group.add_argument('--http',  dest="protocol", const="http",  action="store_const", help=helps[-1])
    args = parser.parse_args()
    if args.protocol: protocol = args.protocol
    colorize = args.colorize
    verbose = args.verbose
    submit(','.join(args.tasks), args.email, args.password)

