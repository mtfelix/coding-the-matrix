# version code 988
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

SUBMIT_VERSION      = "988"
URL                 = 'matrix-001'
part_friendly_names = ['Recognizing Echelon Form', 'Is it echelon?', 'Solving with Echelon Form: No Zero Rows', 'Solving with Echelon Form', 'Echelon Solver', 'Solving General Matrices via Echelon', 'Nullspace A', 'Nullspace B', 'Closest Vector', 'Projection Orthogonal to and onto Vectors', 'Computing the Norm']
groups              = [[('NXdqtXZ99p92mBVs6k1MCv3CyaSnSFwq', 'Recognizing Echelon Form', '>>> print(test_format(echelon_form_1))\n>>> print(test_format(echelon_form_2))\n>>> print(test_format(echelon_form_3))\n>>> print(test_format(echelon_form_4))\n')], [('NXdqtXZ99p92mBVsgrdHRlN6pu9E9KhY', 'Is it echelon?', '>>> M1 = [[0,0,0],[0,0,0],[0,0,0]]\n>>> M2 = [[1,0,0],[0,1,0],[0,1,0]]\n>>> M3 = [[0]*4,[1]*4]\n>>> M4 = [[1,0,0,0,0,0,0,0],\n...       [0,1,1,1,1,1,1,1],\n...       [0,0,1,1,1,0,1,0],\n...       [0,0,0,0,0,1,1,0]]\n>>> M5 = [[1]]\n>>> M6 = [[0]]\n>>> print(test_format([is_echelon(M) for M in [M1, M2, M3, M4, M5, M6]]))\n>>> print(test_format(M1))\n>>> print(test_format(M4))\n')], [('NXdqtXZ99p92mBVsfhc17lbCCcdfuyrU', 'Solving with Echelon Form: No Zero Rows, Part 1', '>>> from vecutil import list2vec\n>>> Ma, ba = [[10,2,-3,53],[0,0,1,2013]], [1,3]\n>>> r = list2vec(ba) - listlist2mat(Ma) * list2vec(echelon_form_vec_a)\n>>> print(test_format(r*r))\n'), ('NXdqtXZ99p92mBVsVhpWWADBLpY4zFvP', 'Solving with Echelon Form: No Zero Rows, Part 2', '>>> from vecutil import list2vec\n>>> Mb, bb = [[2,0,1,3],[0,0,5,3],[0,0,0,1]], [1,-1,3]\n>>> r = list2vec(bb) - listlist2mat(Mb) * list2vec(echelon_form_vec_b)\n>>> print(test_format(r*r))\n'), ('NXdqtXZ99p92mBVsPdNrUVUk8UAJxHNZ', 'Solving with Echelon Form: No Zero Rows, Part 3', '>>> from vecutil import list2vec\n>>> Mc, bc = [[2,2,4,3,2],[0,0,-1,11,1],[0,0,0,0,5]], [2,0,10]\n>>> r = list2vec(bc) - listlist2mat(Mc) * list2vec(echelon_form_vec_c)\n>>> print(test_format(r*r))\n')], [('NXdqtXZ99p92mBVsTenGxBVAmmdvERHR', 'Solving with Echelon Form, Part 1', '>>> from vecutil import list2vec\n>>> from matutil import listlist2mat\n>>> M1 = listlist2mat([[1, 3, -2,  1, 0],[0, 0,  2, -3, 0],[0, 0,  0,  0, 0]])\n>>> b1 = list2vec([5,3,2])\n>>> swefa = solving_with_echelon_form_a or [0,0,0,0,0]\n>>> eq = b1 - M1 * list2vec(swefa)\n>>> print(test_format(solving_with_echelon_form_a is None or 10-eq*eq))\n'), ('NXdqtXZ99p92mBVszsa2YIJ8zzbA0S1w', 'Solving with Echelon Form, Part 2', '>>> from vecutil import list2vec\n>>> from matutil import listlist2mat\n>>> M2 = listlist2mat([[1,2,-8,-4,0],[0,0,2,12,0],[0]*5,[0]*5])\n>>> b2 = list2vec([5,4,0,0])\n>>> swefb = solving_with_echelon_form_b or [0,0,0,0,0]\n>>> eq = b2 - M2 * list2vec(swefb)\n>>> print(test_format(solving_with_echelon_form_b is None or 10-eq*eq))\n')], [('NXdqtXZ99p92mBVsHC1kITNNgcHgCGet', 'Echelon Solver', ">>> from solver import solve\n>>> solve.__calls__ = 0\n>>> from GF2 import one\n>>> cols = ['A', 'B', 'C', 'D', 'E']\n>>> D = set(cols)\n>>> U_rows = [Vec(D,{'E': one, 'D': one, 'A': 0, 'C': 0, 'B': one}), Vec(D,{'E': 0, 'D': one, 'A': 0, 'C': 0, 'B': 0}), Vec(D,{'E': 0, 'D': 0, 'A': one, 'C': one, 'B': 0}), Vec(D,{'E': 0, 'D': 0, 'A': 0, 'C': 0, 'B': 0})]\n>>> b_list = [0, 0, one, 0]\n>>> u = echelon_solve(U_rows, cols, b_list)\n>>> print(test_format(u))\n>>> print(test_format([u_row*u for u_row in U_rows]))\n>>> print(test_format(U_rows))\n>>> print(test_format(b_list))\n>>> U_rows=[Vec(D,{'E': one, 'D': one, 'A': one, 'C': one, 'B': one}), Vec(D,{'E': one, 'D': 0, 'A': 0, 'C': 0, 'B': one}), Vec(D,{'E': one, 'D': 0, 'A': 0, 'C': one, 'B': 0}), Vec(D,{'E': one, 'D': one, 'A': 0, 'C': 0, 'B': 0})]\n>>> b_list = [0, one, 0, one]\n>>> u=echelon_solve(U_rows, cols, b_list)\n>>> print(test_format(u))\n>>> print(test_format([u_row*u for u_row in U_rows]))\n>>> U_rows = [Vec(D, {'A':one, 'C':one}), Vec(D, {'C':one, 'E':one}), Vec(D,{'D':one})]\n>>> b_list = [one, one, one]\n>>> u = echelon_solve(U_rows, cols, b_list)\n>>> print(test_format(u))\n>>> print(test_format([u_row*u for u_row in U_rows]))\n>>> print(test_format(solve.__calls__))\n")], [('NXdqtXZ99p92mBVsP8ACbduEG391C969', 'Solving General Matrices via Echelon', '>>> print(test_format(rowlist))\n>>> print(test_format(label_list))\n>>> print(test_format(b))\n')], [('NXdqtXZ99p92mBVsu4oWwgLr28lQxT6D', 'Nullspace A', '>>> print(test_format(null_space_rows_a))\n')], [('NXdqtXZ99p92mBVsTDPsROTr3txYAUfM', 'Nullspace B', '>>> print(test_format(null_space_rows_b))\n')], [('NXdqtXZ99p92mBVs6CQvmkVQyOnU1WVO', 'Closest Vector', '>>> print(test_format(closest_vector_1))\n>>> print(test_format(closest_vector_2))\n>>> print(test_format(closest_vector_3))\n')], [('NXdqtXZ99p92mBVsTIcPOXdzVZ5HQnfb', 'Projection Orthogonal to and onto Vectors', '>>> print(test_format(projection_orthogonal_1))\n>>> print(test_format(project_onto_1))\n>>> print(test_format(projection_orthogonal_2))\n>>> print(test_format(project_onto_2))\n>>> print(test_format(projection_orthogonal_3))\n>>> print(test_format(project_onto_3))\n')], [('NXdqtXZ99p92mBVsGwr9TtaZR2tS6z1p', 'Computing the Norm', '>>> print(test_format(norm1))\n>>> print(test_format(norm2))\n>>> print(test_format(norm3))\n')]]
source_files        = ['hw6.py'] * len(sum(groups,[]))

try:
    import hw6 as solution
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
            res_itr = iter(results)
            for t in part_tests.split('\n'):
                print(t)
                if t[:3] == '>>>':
                   sys.stdout.write(next(res_itr)) 
            # print(part_tests)
            # print(results)
            # for t, r in zip(part_tests.split('\n>>>'), results):
            #     sys.stdout.write('>>> %s\n%s' % (t, r))
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

