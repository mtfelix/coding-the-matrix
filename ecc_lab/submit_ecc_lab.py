# version code 828+########                                     ######## 
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
part_friendly_names = ['Matrix G', 'Encode 1001', 'Matrix R', 'Matrix H', 'Find Error', 'Decode 1011011', 'Find Error Matrix', 'Matrix P', 'Matrix E', 'Number of Bits Encoded']
groups              = [[('aKngN8Qrgk3Krynswj0Njyxy93G2WSG9', 'Matrix G', '>>> print(test_format(G.D))\n>>> print(test_format(G.f))\n')], [('aKngN8Qrgk3KrynsZcSwrzNCUDIXUN3o', 'Encode 1001', '>>> print(test_format(encoding_1001))\n')], [('aKngN8Qrgk3KrynsRZeIXCMBidKOEbOW', 'Matrix R', '>>> print(test_format(R.D))\n>>> print(test_format(R*G))\n')], [('aKngN8Qrgk3KrynshvUCB9PJDcvTdvHP', 'Matrix H', '>>> print(test_format(H.D))\n>>> print(test_format(H.f))\n')], [('aKngN8Qrgk3KrynsUoFC5liGjiWJ8mwV', 'Find Error', '>>> from vec import Vec\n>>> x = [Vec({0, 1, 2},{0: 0, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 0, 2: one}), Vec({0, 1, 2},{0: 0, 1: one, 2: 0}), Vec({0, 1, 2},{0: 0, 1: one, 2: one}), Vec({0, 1, 2},{0: one, 1: 0, 2: 0}), Vec({0, 1, 2},{0: one, 1: 0, 2: one}), Vec({0, 1, 2},{0: one, 1: one, 2: 0}), Vec({0, 1, 2},{0: one, 1: one, 2: one})]\n>>> print(test_format([find_error(y).D for y in x]))\n>>> print(test_format([find_error(y).f for y in x]))\n')], [('aKngN8Qrgk3KrynsNP7mgVOTcTTC7Mj3', 'Decode 1011011', '>>> print(test_format(error_vector))\n>>> print(test_format(code_word))\n>>> print(test_format(original))\n')], [('aKngN8Qrgk3KrynsH6FQSvgfzJK7BTeQ', 'Find Error Matrix', '>>> from mat import Mat\n>>> print(test_format(find_error_matrix(Mat(({0, 1, 2}, {0, 1}), {(0, 1): 0, (2, 0): one, (0, 0): one, (1, 0): one, (1, 1): 0, (2, 1): one}))))\n>>> print(test_format(find_error_matrix(Mat(({0, 1, 2}, {0, 1, 2, 3, 4}), {(0, 1): 0, (1, 2): 0, (0, 0): one, (0, 2): one, (0, 4): one, (2, 1): one, (1, 1): 0, (2, 0): one, (1, 3): one, (2, 3): 0, (1, 4): one, (2, 2): 0, (2, 4): one, (1, 0): 0, (0, 3): 0}))))\n')], [('aKngN8Qrgk3Krynsw48M0OQeN4hIqR26', 'Matrix P', '>>> from hashlib import *\n>>> print(test_format(md5(test_format(P).encode()).hexdigest()))\n')], [('aKngN8Qrgk3Kryns2LTGZYLRzmNa3Loc', 'Matrix E', '>>> from hashlib import *\n>>> print(test_format(md5(test_format(C).encode()).hexdigest()))\n>>> print(test_format(bits_before))\n>>> print(test_format(bits_after))\n')], [('aKngN8Qrgk3KrynsW3mV56QUDnFQiAqS', 'Number of Bits Encoded', '>>> from hashlib import *\n>>> from mat import Mat\n>>> noisy = Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223}), {(2, 198): one, (4, 166): one, (0, 20): one, (2, 72): one, (0, 132): one, (2, 84): one, (5, 79): one, (5, 26): one, (4, 84): one, (4, 90): one, (0, 92): one, (3, 185): one, (1, 217): one, (3, 214): one, (5, 43): one, (3, 145): one, (6, 157): one, (2, 11): one, (3, 159): one, (4, 108): one, (2, 44): one, (6, 13): one, (5, 27): one})\n>>> CTILDE = C + noisy\n>>> print(test_format(md5(test_format(correct(CTILDE)).encode()).hexdigest()))\n')]]
source_files        = ['ecc_lab.py'] * len(sum(groups,[]))

try:
    import ecc_lab as solution
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
    print('**** VERSION 2.0 ****')
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

