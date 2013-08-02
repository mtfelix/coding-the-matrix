# version code 761########                                     ######## 
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
part_friendly_names = ['Vector Comprehension and Sum', 'Vector Dictionary', 'Constructing a Span over GF(2)', 'Identifying Vector Spaces A', 'Identifying Vector Spaces B', 'Identifying Vector Spaces C']
groups              = [[('DaewSQBNUKRoMWOTh0a4cX6g', 'Vector Comprehension and Sum, Part 1', ">>> from vec import *\n>>> def veclist_equal(list1, list2): return len(list1) == len(list2) & sum([equal(list1[i], list2[i]) for i in range(len(list1))]) == len(list1)\n>>> veclist = [Vec({'a', 'b', 'c', 'd'}, {'a': 2, 'b': 3, 'c':1}), Vec({'a', 'b', 'c', 'd'}, {'a': 3, 'c': 1}), Vec({'a', 'b', 'c', 'd'}, {'c': 5})]\n>>> selected1 = vec_select(veclist, 'c')\n>>> expected_selected1 = []\n>>> print(test_format(veclist_equal(selected1, expected_selected1)))\n>>> selected2 = vec_select(veclist, 'b')\n>>> expected_selected2 = [Vec({'a', 'b', 'c', 'd'}, {'a': 3, 'c': 1}), Vec({'a', 'b', 'c', 'd'}, {'c': 5})]\n>>> print(test_format(veclist_equal(selected2, expected_selected2)))\n>>> selected3 = vec_select(veclist, 'd')\n>>> print(test_format(veclist_equal(selected3, veclist)))\n"), ('DaewSQBNACRNxF8JlslkmqLh', 'Vector Comprehension and Sum, Part 2', ">>> veclist = [Vec({'a', 'b', 'c', 'd'}, {'a': 2, 'b': 3, 'c':1}), Vec({'a', 'b', 'c', 'd'}, {'a': 3, 'c': 1}), Vec({'a', 'b', 'c', 'd'}, {'c': 5})]\n>>> selected1 = vec_select(veclist, 'c')\n>>> selected2 = vec_select(veclist, 'b')\n>>> selected3 = vec_select(veclist, 'd')\n>>> D = {'a', 'b', 'c', 'd'}\n>>> print(test_format(vec_sum(selected1, D)))\n>>> print(test_format(vec_sum(selected2, D)))\n>>> print(test_format(vec_sum(selected3, D)))\n"), ('DaewSQBNEitE5FTWEDt1vDCk', 'Vector Comprehension and Sum, Part 3', ">>> veclist = [Vec({'a', 'b', 'c', 'd'}, {'a': 2, 'b': 3, 'c':1}), Vec({'a', 'b', 'c', 'd'}, {'a': 3, 'c': 1}), Vec({'a', 'b', 'c', 'd'}, {'c': 5})]\n>>> selected1 = vec_select(veclist, 'c')\n>>> selected2 = vec_select(veclist, 'b')\n>>> selected3 = vec_select(veclist, 'd')\n>>> D = {'a', 'b', 'c', 'd'}\n>>> print(test_format(vec_select_sum(veclist, 'c', D)))\n>>> print(test_format(vec_select_sum(veclist, 'b', D)))\n>>> print(test_format(vec_select_sum(veclist, 'd', D)))\n")], [('DaewSQBNoEcEaR2fzDkFDleR', 'Vector Dictionary', ">>> from hashlib import md5\n>>> vd = {9: Vec({'a', 'c', 'b'},{'a': 1, 'c': 2}), 6: Vec({'a', 'c', 'b'},{'c': 4, 'b': 2}), 1: Vec({'a', 'c', 'b'},{'a': 2, 'c': 3})}\n>>> print(test_format(set(map(test_format, scale_vecs(vd)))))\n>>> vedi = {83: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 864, 1: 917, 2: 709, 3: 717, 4: 540, 5: 582, 6: 460, 7: 367, 8: 373, 9: 868}), 3: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 274, 1: 425, 2: 435, 3: 125, 4: 892, 5: 327, 6: 70, 7: 213, 8: 764, 9: 808}), 4: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 658, 1: 500, 2: 419, 3: 387, 4: 101, 5: 337, 6: 930, 7: 33, 8: 928, 9: 872}), 39: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 63, 1: 358, 2: 527, 3: 22, 4: 198, 5: 670, 6: 281, 7: 420, 8: 197, 9: 608}), 40: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 78, 1: 137, 2: 676, 3: 60, 4: 902, 5: 100, 6: 770, 7: 110, 8: 477, 9: 468}), 43: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 411, 1: 66, 2: 400, 3: 174, 4: 286, 5: 309, 6: 862, 7: 760, 8: 753, 9: 408}), 34: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 67, 1: 594, 2: 211, 3: 608, 4: 735, 5: 147, 6: 855, 7: 736, 8: 256, 9: 122}), 78: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 675, 1: 729, 2: 690, 3: 732, 4: 78, 5: 429, 6: 450, 7: 3, 8: 322, 9: 828}), 15: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 724, 1: 961, 2: 0, 3: 47, 4: 236, 5: 227, 6: 113, 7: 53, 8: 251, 9: 443}), 81: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 932, 1: 697, 2: 223, 3: 751, 4: 359, 5: 112, 6: 278, 7: 915, 8: 289, 9: 366}), 50: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 168, 1: 504, 2: 107, 3: 270, 4: 112, 5: 700, 6: 867, 7: 189, 8: 966, 9: 858}), 35: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 945, 1: 463, 2: 367, 3: 186, 4: 616, 5: 408, 6: 563, 7: 666, 8: 644, 9: 731}), 14: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 339, 1: 969, 2: 868, 3: 258, 4: 293, 5: 770, 6: 487, 7: 496, 8: 98, 9: 632}), 25: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 37, 1: 303, 2: 211, 3: 577, 4: 558, 5: 342, 6: 238, 7: 634, 8: 884, 9: 166}), 27: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 664, 1: 293, 2: 75, 3: 983, 4: 581, 5: 323, 6: 726, 7: 847, 8: 863, 9: 865}), 60: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 512, 1: 115, 2: 491, 3: 127, 4: 914, 5: 872, 6: 20, 7: 825, 8: 253, 9: 536}), 61: Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 637, 1: 649, 2: 402, 3: 547, 4: 325, 5: 695, 6: 684, 7: 152, 8: 357, 9: 925})}\n>>> print(test_format(md5(test_format(set(map(test_format, scale_vecs(vedi)))).encode()).hexdigest()))\n")], [('DaewSQBNjoL1FqmPd5U6jPMF', 'Constructing a Span over GF(2)', '>>> from GF2 import one\n>>> from vecutil import list2vec\n>>> l = [list2vec(v) for v in [[one,0,one],[0,one,one]]]\n>>> print(test_format(set(map(test_format, GF2_span({0,1,2}, l)))))\n>>> l = [list2vec(v) for v in [[0,0,one,0],[one,one,0,one]]]\n>>> print(test_format(set(map(test_format, GF2_span({0,1,2,3}, l)))))\n')], [('DaewSQBNWBa5FWTEpRt4xO2v', 'Identifying Vector Spaces A', '>>> print(test_format(is_it_a_vector_space_1))\n>>> print(test_format(is_it_a_vector_space_2))\n')], [('DaewSQBNlAA3iJwnVlCkEcHf', 'Identifying Vector Spaces B', '>>> print(test_format(is_it_a_vector_space_3))\n>>> print(test_format(is_it_a_vector_space_4))\n')], [('DaewSQBNOCb1aiHLPwS4FAcg', 'Identifying Vector Spaces C', '>>> print(test_format(is_it_a_vector_space_5))\n>>> print(test_format(is_it_a_vector_space_6))\n')]]
source_files        = ['hw2.py'] * len(sum(groups,[]))

try:
    import hw2 as solution
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
        entries = delimit(map(tf, sorted(filter(lambda o: o[1] != 0, obj.f.items()))))
        return '<%s %s {%s}>' % (otype.__name__, test_format(obj.D), entries)
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

