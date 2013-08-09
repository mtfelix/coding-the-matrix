# version code 829########                                     ######## 
# Hi there, curious student.                        #
#                                                   #
# This submission script runs some tests on your    #
# code and then uploads it to Coursera for grading. #
#                                                   #
# Changing anything in this script might cause your #
# submissions to fail.                              #
########                                     ########

import io, os, sys, doctest, traceback, importlib, urllib.request, urllib.parse, urllib.error, base64, hashlib, random, ast

URL                 = 'matrix-001'
part_friendly_names = ['Get Item', 'Set Item', 'Addition', 'Scalar Multiplication', 'Equality', 'Transposition', 'Vector-Matrix Multiplication', 'Matrix-Matrix Multiplication']
groups              = [[('D3Jz8BCduKJd3YFNoAuWJpQguXCvbilw', 'Get Item', ">>> from mat import Mat\n>>> M = Mat(({1,3,5}, {'a'}), {(1,'a'):3, (5,'a'): 9})\n>>> print(test_format([M[(x,y)] for x in sorted(M.D[0]) for y in sorted(M.D[1])]))\n>>> M = Mat((set(range(1,11)),{'a','b','c','d','e'}), {(2,'e'):20.1, (7,'e'):17, (4,'b'):-17, (10,'b'):2})\n>>> print(test_format([M[(x,y)] for x in sorted(M.D[0]) for y in sorted(M.D[1])]))\n>>> from GF2 import one\n>>> M = Mat((set(range(33,34)),{(1,2),(2,3),(1,3)}), {(33, (2,3)): one})\n>>> print(test_format([M[(x,y)] for x in sorted(M.D[0]) for y in sorted(M.D[1])]))\n")], [('D3Jz8BCduKJd3YFN0AYge3neP1L9r3Pd', 'Set Item', ">>> from mat import Mat\n>>> M = Mat(({'a','b','c'}, {5, 'a'}), {('a', 5):3, ('b', 5):7})\n>>> M['b',5] = 9\n>>> print(test_format(M))\n>>> M['c',5] = 13\n>>> print(test_format(M))\n>>> M['c',5] = 0\n>>> print(test_format(M))\n>>> from GF2 import one\n>>> M = Mat(({1,2},{2,3}),{(1,2):one})\n>>> M[(2,2)] = one\n>>> print(test_format(M))\n>>> M = Mat(({()},{((),)}),{})\n>>> M[(),((),)] = 17771\n>>> print(test_format(M))\n")], [('D3Jz8BCduKJd3YFNuNJQ0VFPg3GPI82k', 'Addition', ">>> from mat import Mat\n>>> M = Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (6,'y'):3})\n>>> N = Mat(({3, 6}, {'x','y'}), {(3,'y'):5})\n>>> print(test_format(M+N))\n>>> print(test_format(M))\n>>> print(test_format(N))\n>>> zero = Mat(({3,6}, {'x','y'}), {})\n>>> print(test_format(M + zero))\n>>> print(test_format(M))\n>>> print(test_format(zero))\n>>> M = Mat(({1,3}, {2,4}), {(1,2):2, (3,4):3})\n>>> N = Mat(({1,3}, {2,4}), {(1,4):1, (1,2):4})\n>>> print(test_format(M+N))\n>>> print(test_format(M))\n>>> print(test_format(N))\n>>> from GF2 import one\n>>> M = Mat(({1,2,3},{0,2,4}), {(1,0): one, (2,2):one})\n>>> N = Mat(({1,2,3},{0,2,4}), {(1,0): one, (2,2):one})\n>>> print(test_format(M + N))\n>>> print(test_format(M))\n>>> print(test_format(N))\n>>> M = Mat(({1,2,3},{0,2,4}), {(1,0): 0.5, (2,2):3})\n>>> N = Mat(({1,2,3},{0,2,4}), {(1,0): 2j, (2,2):1 + 4j})\n>>> print(test_format(M + N))\n>>> print(test_format(M))\n>>> print(test_format(N))\n")], [('D3Jz8BCduKJd3YFNEifga5IXkwhK9yX6', 'Scalar Multiplication', ">>> from mat import Mat\n>>> M = Mat(({1,3,5}, {2,4}), {(1,2):4, (5,4):2, (3,4):3})\n>>> print(test_format(0*M))\n>>> print(test_format(M))\n>>> print(test_format(1*M))\n>>> print(test_format(0.25*M))\n>>> print(test_format(19*M))\n>>> print(test_format(M))\n>>> print(test_format(2*M))\n>>> from GF2 import one\n>>> M = Mat(({'a','b'}, {not not 0, not not 1}), {('a',False):one, ('b',True):one})\n>>> print(test_format(one * M))\n>>> print(test_format(0 * M))\n>>> print(test_format(M))\n")], [('D3Jz8BCduKJd3YFNltxUghO7N4k5KDbp', 'Equality', ">>> from mat import Mat\n>>> a, b = 'a', 'b'\n>>> d = ({a, b}, {0, 1})\n>>> M1 = Mat(d, {})\n>>> M2 = Mat(d, {(a, 0): 0})\n>>> M3 = Mat(d, {(a, 1): 1})\n>>> M4 = Mat(d, {(a, 0): 1})\n>>> print(test_format([Ma == Mb for Ma in [M1, M2, M3, M4] for Mb in [M1, M2, M3, M4]]))\n>>> A = Mat(d, {(a,1):2, (b,0):1})\n>>> B = Mat(d, {(a,1):2, (b,0):1, (b,1):0})\n>>> C = Mat(d, {(a,1):2, (b,0):1, (b,1):5}) \n>>> print(test_format([Ma == Mb for Ma in [A, B, C] for Mb in [A, B, C]]))\n>>> from GF2 import one\n>>> d = (set(range(100)), set(range(25,125)))\n>>> M1 = Mat(d, {(71, 121): one, (11,66): one, (87,87): one, (1,99): 0})\n>>> M2 = Mat(d, {(71, 121): 0,   (11,66): one, (87,87): one, (1,99): 0})\n>>> M3 = Mat(d, {(71, 121): one, (11,66): one, (87,87): one, (1,99): 0, (2,99): 0})\n>>> M4 = Mat(d, {(71, 121): one, (11,66): one, (87,87): one, (1,99): 0, (2,99): one})\n>>> M5 = Mat(d, {(71, 121): one, (11,66): one, (87,87): one, (1,99): 0, (3,99): 0})\n>>> M6 = Mat(d, {(71, 121): 0,   (11,66): one, (87,87): one, (1,99): 0, (3,99): one})\n>>> L = [M1, M2, M3, M4, M5, M6]\n>>> print(test_format([Ma == Mb for Ma in L for Mb in L]))\n")], [('D3Jz8BCduKJd3YFNCqDxiQ5nwoJl3ICO', 'Transposition', ">>> from mat import Mat\n>>> d = ({0,1},{0,1})\n>>> M = Mat(d, {(0,1):9, (1,0):2, (1,1):4})\n>>> print(test_format(M.transpose()))\n>>> print(test_format(M))\n>>> x, y, z = 'x','y','z'\n>>> M = Mat(({x,y,z}, {2,4}), {(x,4):7, (x,2):2, (y,4):4, (z,4):5})\n>>> print(test_format(M.transpose()))\n>>> print(test_format(M.transpose().transpose()))\n>>> print(test_format(M.transpose().transpose().transpose()))\n>>> from GF2 import one\n>>> print(test_format(Mat(({0,one},{0,one}), {(0,0):one, (one,0):one}).transpose()))\n")], [('D3Jz8BCduKJd3YFNEOWC0oLi3nmYeFi3', 'Vector-Matrix Multiplication', ">>> from mat import Mat\n>>> from vec import Vec\n>>> from GF2 import one\n>>> v = Vec({1, 2, 3}, {1: 1, 2: 8})\n>>> M = Mat(({1, 2, 3}, {1, 2, 3}), {(1, 2): 7, (2, 1):-1, (3, 1): 1, (3, 3): 7})\n>>> print(test_format(v * M))\n>>> v = Vec({'a','b'}, {})\n>>> M = Mat(({'a','b'}, {0, 2, 4, 6, 7}), {})\n>>> print(test_format(v * M))\n>>> M = Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 3, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})\n>>> v = Vec({'a', 'b'}, {'a': 1, 'b': 2})\n>>> print(test_format(M * v))\n>>> M = Mat(({('a', 'b'), ('c', 'd')}, {1, 2, 3, 5, 8}), {})\n>>> v = Vec({1, 2, 3, 5, 8}, {})\n>>> print(test_format(M * v))\n>>> M = Mat(({0,2,'a'},{'b','c','d'}), {(0,'b'): one, (0, 'c'): one, (2, 'd'): one, ('a','c'):one})\n>>> v = Vec({'b','c','d'}, {'b':one,'d':one})\n>>> print(test_format(M * v))\n>>> d = set(range(100))\n>>> M = Mat((d,d), {(82, 86): 919, (22, 13): 832, (58, 58): 310, (77, 68): 65, (28, 67): 196, (4, 46): 316, (11, 88): 733, (17, 13): 116, (3, 69): 91, (13, 65): 681, (21, 53): 367, (18, 78): 25, (83, 27): 653, (95, 76): 944, (66, 0): 984, (2, 16): 646, (10, 56): 626, (80, 53): 377, (41, 49): 94, (76, 43): 214, (37, 59): 870, (83, 96): 246, (79, 58): 441, (90, 47): 725, (60, 36): 333, (66, 48): 647, (75, 40): 717, (25, 7): 614, (88, 31): 897, (84, 74): 714, (21, 4): 406, (99, 41): 231, (81, 25): 473, (6, 59): 656, (88, 22): 693, (78, 9): 295, (30, 82): 377, (33, 1): 764, (87, 20): 939, (91, 20): 780, (97, 44): 775, (48, 30): 385, (0, 19): 61, (47, 95): 323, (8, 31): 651, (23, 99): 729, (52, 72): 332, (52, 31): 523, (63, 10): 825, (99, 69): 798, (13, 66): 333, (83, 6): 414, (73, 47): 563, (41, 85): 869, (19, 26): 79, (27, 57): 789, (26, 21): 43, (79, 19): 334, (23, 84): 164, (0, 16): 104, (6, 24): 105, (13, 8): 599, (56, 21): 636, (27, 99): 74, (8, 14): 675, (10, 30): 119, (69, 16): 656, (76, 0): 644, (46, 57): 612, (34, 4): 559, (51, 88): 961, (7, 37): 348, (94, 63): 421, (1, 71): 566, (62, 4): 395, (74, 29): 982, (84, 91): 373, (40, 14): 206, (35, 98): 74, (68, 18): 2, (99, 74): 994, (74, 57): 864, (31, 17): 809, (30, 43): 862, (8, 30): 939, (30, 10): 788, (17, 89): 782, (77, 8): 489, (46, 14): 469, (32, 73): 667, (7, 93): 255, (92, 19): 634, (12, 26): 477, (44, 7): 954, (94, 66): 474, (92, 9): 35, (52, 10): 810, (77, 62): 832, (10, 64): 602, (50, 10): 315})\n>>> v = Vec(d, {0: 601, 1: 394, 3: 836, 5: 857, 6: 888, 7: 906, 8: 607, 12: 776, 14: 192, 15: 594, 16: 508, 17: 218, 18: 28, 19: 966, 20: 271, 21: 295, 23: 149, 24: 928, 25: 328, 26: 968, 27: 85, 28: 640, 30: 625, 31: 43, 32: 665, 36: 477, 39: 327, 41: 715, 42: 580, 43: 921, 46: 935, 48: 354, 49: 958, 50: 779, 51: 78, 53: 37, 54: 764, 56: 361, 58: 530, 60: 968, 61: 138, 66: 316, 67: 934, 71: 150, 72: 268, 73: 643, 74: 82, 76: 580, 77: 297, 78: 631, 79: 678, 80: 850, 82: 817, 83: 867, 84: 611, 85: 58, 87: 212, 90: 837, 91: 719, 92: 771, 94: 262, 96: 155, 97: 801, 99: 983})\n>>> print(test_format(M*v))\n")], [('D3Jz8BCduKJd3YFNvPf1gH3T5Qt5EtNm', 'Matrix-Matrix Multiplication', ">>> from mat import Mat\n>>> M = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):3, (1,0):5, (0,1):3, (0,2):2})\n>>> N = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})\n>>> print(test_format(M*N))\n>>> print(test_format(M))\n>>> print(test_format(N))\n>>> M = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2}) \n>>> N = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):2, ('b','x'):4, ('b','y'):-1})\n>>> print(test_format(M*N))\n>>> M = Mat(({0, 1}, {'a', 'c', 'b'}), {})\n>>> N = Mat(({'a', 'c', 'b'}, {(1, 1), (2, 2)}), {})\n>>> print(test_format(M*N))\n>>> from GF2 import one\n>>> M = Mat(({0,one},{0,one}), {(0,0):one, (0,one):0, (one,0):one})\n>>> N = Mat(({0,one},{0,one}), {(0,0):one, (0,one):one, (one,0):0})\n>>> print(test_format(M*N))\n>>> d = (set(range(100)), set(range(100)))\n>>> M = Mat(d, {(15, 27): 675, (90, 21): 331, (61, 82): 308, (10, 17): 418, (71, 67): 990, (82, 68): 928, (71, 18): 803, (66, 10): 134, (85, 30): 125, (96, 11): 445, (60, 52): 377, (0, 10): 604, (73, 31): 568, (85, 70): 594, (0, 94): 244, (81, 27): 72, (9, 1): 203, (50, 22): 849, (98, 51): 377, (25, 4): 95, (44, 45): 38, (32, 51): 693, (54, 48): 888, (49, 53): 933, (90, 5): 585, (61, 13): 46, (27, 94): 412, (49, 58): 806, (18, 75): 716, (25, 60): 268, (61, 35): 359, (79, 86): 620, (52, 12): 772, (71, 25): 23, (20, 93): 890, (69, 26): 261, (23, 90): 163, (51, 96): 308, (27, 9): 753, (76, 20): 174, (19, 15): 114, (56, 53): 779, (45, 59): 464, (89, 26): 589, (92, 2): 830, (67, 82): 778, (46, 15): 80, (55, 1): 153, (47, 14): 744, (55, 45): 514, (50, 10): 488, (0, 64): 679, (73, 65): 673, (89, 95): 94, (27, 37): 101, (64, 45): 201, (11, 64): 405, (15, 43): 499, (18, 41): 707, (87, 38): 678, (86, 42): 73, (38, 79): 988, (71, 35): 267, (36, 7): 845, (65, 35): 647, (20, 66): 629, (3, 20): 787, (43, 99): 507, (90, 31): 255, (80, 96): 551, (89, 33): 597, (75, 15): 64, (65, 43): 150, (86, 32): 929, (87, 37): 357, (50, 41): 565, (69, 6): 1, (87, 93): 293, (69, 50): 877, (25, 25): 955, (6, 32): 297, (62, 63): 799, (68, 66): 723, (62, 50): 590, (74, 3): 574, (38, 26): 734, (3, 22): 559, (9, 79): 937, (83, 36): 260, (61, 21): 538, (14, 45): 780, (10, 7): 58, (27, 74): 887, (25, 59): 958, (17, 12): 226, (41, 53): 768, (46, 21): 617, (88, 91): 777, (50, 65): 210})\n>>> N = Mat(d, {(7, 3): 841, (94, 1): 107, (23, 80): 252, (8, 66): 559, (16, 68): 867, (99, 65): 444, (28, 67): 308, (38, 55): 640, (58, 36): 328, (11, 14): 874, (14, 99): 908, (12, 1): 313, (32, 2): 313, (9, 44): 298, (95, 39): 842, (79, 76): 114, (73, 51): 967, (69, 69): 987, (82, 29): 127, (83, 12): 156, (41, 76): 252, (96, 36): 908, (74, 73): 451, (92, 95): 917, (43, 81): 433, (4, 82): 775, (38, 96): 0, (76, 82): 28, (53, 31): 602, (68, 12): 529, (0, 67): 233, (69, 23): 764, (13, 43): 904, (27, 7): 88, (72, 98): 500, (74, 7): 432, (88, 73): 370, (39, 71): 365, (80, 55): 105, (0, 6): 572, (1, 38): 940, (10, 9): 957, (98, 98): 578, (29, 66): 269, (17, 78): 499, (1, 52): 40, (6, 68): 282, (10, 68): 604, (62, 21): 692, (51, 93): 38, (83, 39): 428, (85, 23): 685, (35, 18): 101, (66, 86): 21, (86, 39): 894, (79, 14): 289, (49, 59): 887, (6, 47): 420, (87, 38): 152, (89, 10): 21, (21, 27): 731, (58, 99): 674, (10, 47): 772, (67, 18): 837, (13, 82): 385, (49, 61): 211, (90, 71): 722, (78, 41): 232, (48, 7): 868, (81, 47): 206, (35, 47): 111, (2, 93): 514, (92, 59): 237, (86, 54): 532, (87, 22): 48, (81, 23): 900, (25, 76): 19, (1, 19): 990, (58, 7): 348, (14, 73): 123, (75, 57): 103, (72, 90): 218, (83, 62): 112, (66, 26): 796, (27, 0): 776, (11, 74): 338, (0, 79): 639, (99, 6): 588, (77, 67): 637, (15, 64): 300, (73, 87): 706, (60, 34): 19, (74, 78): 956, (21, 24): 294, (32, 85): 535, (61, 35): 268, (82, 31): 0, (35, 71): 460, (91, 98): 466, (92, 6): 130})\n>>> import hashlib\n>>> print(test_format(hashlib.md5(test_format(M*N).encode()).hexdigest()))\n")]]
source_files        = ['mat.py'] * len(sum(groups,[]))

try:
    import mat as solution
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
        entries = tf({x:obj.f[x] for x in obj.f if obj.f[x] != 0})
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
    src = []
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

