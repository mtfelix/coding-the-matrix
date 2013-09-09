# version code 1049
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

SUBMIT_VERSION      = "1049"
URL                 = 'matrix-001'
part_friendly_names = ['Signum', 'Evaluate', 'Error', 'Find Grad', 'Gradient Descent Step']
groups              = [[('59qJbbUXhEMmAqc6myiKKi8MahYSqo1R', 'Signum', ">>> a = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},{0: 267, 1: 277, 2: -398, 3: 446, 4: 844, 5: -613, 6: -157, 7: 28, 8: 25, 9: 416})\n>>> print(test_format(signum(a)))\n>>> b = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29},{0: -456, 1: -120, 2: 937, 3: -123, 4: 387, 5: 54, 6: -131, 7: 275, 8: 611, 9: 472, 10: 255, 11: -14, 12: 827, 13: -586, 14: 864, 15: -679, 16: -851, 17: -431, 18: 17, 19: 986, 20: 716, 21: 117, 22: 645, 23: 880, 24: -695, 25: 692, 26: 861, 27: -441, 28: -8, 29: 49})\n>>> print(test_format(signum(b)))\n>>> c = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49},{0: -470, 1: -30, 2: 513, 3: 799, 4: -721, 5: 754, 6: 359, 7: -337, 8: -687, 9: -588, 10: 505, 11: -582, 12: -351, 13: -176, 14: -667, 15: -851, 16: 435, 17: -238, 18: 544, 19: 383, 20: -985, 21: -830, 22: 856, 23: 333, 24: -631, 25: -271, 26: -309, 27: -461, 28: -995, 29: -245, 30: -21, 31: -534, 32: 379, 33: 976, 34: -337, 35: -800, 36: 37, 37: 811, 38: -598, 39: -439, 40: 653, 41: 317, 42: -468, 43: 705, 44: -649, 45: 363, 46: -698, 47: -837, 48: 477, 49: 520})\n>>> print(test_format(signum(c)))\n>>> d = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69},{0: 837, 1: -801, 2: -376, 3: 388, 4: 482, 5: 313, 6: 812, 7: 118, 8: 796, 9: -273, 10: 763, 11: -534, 12: 584, 13: 74, 14: 214, 15: 564, 16: -923, 17: 977, 18: -859, 19: 288, 20: 99, 21: 676, 22: -223, 23: -103, 24: 893, 25: 4, 26: -734, 27: 120, 28: 549, 29: 433, 30: -295, 31: 822, 32: 655, 33: 870, 34: 205, 35: -241, 36: -632, 37: 159, 38: 476, 39: 189, 40: -210, 41: 158, 42: -945, 43: -270, 44: 9, 45: 510, 46: 254, 47: 5, 48: 755, 49: 473, 50: 347, 51: 259, 52: -305, 53: -303, 54: -299, 55: 371, 56: 47, 57: 143, 58: -97, 59: -690, 60: 788, 61: 80, 62: -3, 63: 332, 64: -88, 65: -746, 66: 775, 67: -416, 68: 688, 69: -93})\n>>> print(test_format(signum(d)))\n>>> e = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89},{0: -984, 1: -230, 2: 334, 3: -757, 4: 496, 5: 522, 6: -592, 7: -278, 8: -245, 9: 168, 10: -175, 11: -835, 12: 803, 13: 862, 14: 932, 15: 717, 16: -693, 17: 520, 18: -761, 19: 814, 20: 571, 21: -891, 22: 316, 23: 396, 24: 146, 25: 202, 26: 956, 27: -62, 28: 616, 29: 594, 30: -482, 31: -485, 32: 183, 33: 830, 34: 857, 35: 512, 36: -459, 37: 589, 38: 705, 39: -629, 40: -240, 41: 207, 42: -514, 43: 122, 44: -999, 45: -463, 46: -38, 47: 22, 48: -535, 49: -82, 50: 514, 51: -303, 52: 410, 53: -658, 54: 18, 55: 66, 56: 823, 57: -237, 58: -256, 59: -956, 60: 667, 61: 915, 62: 588, 63: -716, 64: 885, 65: 791, 66: -557, 67: -613, 68: -113, 69: -364, 70: 334, 71: -872, 72: 135, 73: -270, 74: 265, 75: -998, 76: 376, 77: 184, 78: 845, 79: -656, 80: 703, 81: -541, 82: -152, 83: 330, 84: -67, 85: -598, 86: 921, 87: -113, 88: -643, 89: 893})\n>>> print(test_format(signum(e)))\n>>> print(test_format(signum(Vec({'a','c','$'}, {'c':-0.5}))))\n")], [('59qJbbUXhEMmAqc6Q7T0ivY1zW8PXGIE', 'Evaluate', '>>> from mat import Mat\n>>> from vec import Vec\n>>> from vecutil import list2vec\n>>> from matutil import listlist2mat\n>>> A1 = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6], [10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])\n>>> b1 = list2vec([1, 1, -1, -1, 1])\n>>> A2 = Mat((set(range(97,123)),set(range(65,91))),{(x,y): 301-(7*((x-97)+26*(y-65))%761) for x in range(97,123) for y in range(65,91)})\n>>> b2 = Vec(A2.D[0], {x:(-1)**i for i, x in enumerate(sorted(A2.D[0]))})\n>>> print(test_format(fraction_wrong(A1, b1, Vec(A1.D[1], {}))))\n>>> print(test_format(fraction_wrong(A1, b1, Vec(A1.D[1], {x:-2 for x in A1.D[1]}))))\n>>> print(test_format(fraction_wrong(A1, b1, Vec(A1.D[1], {x: (-1)**i for i, x in enumerate(sorted(A1.D[1]))}))))\n>>> print(test_format(fraction_wrong(A2, b2, Vec(A2.D[1], {}))))\n>>> print(test_format(fraction_wrong(A2, b2, Vec(A2.D[1], {x:-2 for x in A2.D[1]}))))\n>>> print(test_format(fraction_wrong(A2, b2, Vec(A2.D[1], {x: (-1)**i for i, x in enumerate(sorted(A2.D[1]))}))))\n')], [('59qJbbUXhEMmAqc6KN7zKn8z4FN8Qmhm', 'Error', '>>> from mat import Mat\n>>> from vec import Vec\n>>> from vecutil import list2vec\n>>> from matutil import listlist2mat\n>>> A1 = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6], [10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])\n>>> b1 = list2vec([1, 1, -1, -1, 1])\n>>> A2 = Mat((set(range(97,123)),set(range(65,91))),{(x,y): 301-(7*((x-97)+26*(y-65))%761) for x in range(97,123) for y in range(65,91)})\n>>> b2 = Vec(A2.D[0], {x:(-1)**i for i,x in enumerate(sorted(A2.D[0]))})\n>>> print(test_format(loss(A1, b1, Vec(A1.D[1], {}))))\n>>> print(test_format(loss(A1, b1, Vec(A1.D[1], {x:-2 for x in A1.D[1]}))))\n>>> print(test_format(loss(A1, b1, Vec(A1.D[1], {x: (-1)**i for i, x in enumerate(sorted(A1.D[1]))}))))\n>>> print(test_format(loss(A2, b2, Vec(A2.D[1], {}))))\n>>> print(test_format(loss(A2, b2, Vec(A2.D[1], {x:-2 for x in A2.D[1]}))))\n>>> print(test_format(loss(A2, b2, Vec(A2.D[1], {x: (-1)**i for i, x in enumerate(sorted(A2.D[1]))}))))\n')], [('59qJbbUXhEMmAqc6oyzwzQwAGN8JpU91', 'Find Grad', '>>> from vec import Vec\n>>> from mat import Mat\n>>> from vecutil import list2vec\n>>> from matutil import listlist2mat\n>>> A1 = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6], [10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])\n>>> b1 = list2vec([1, 1, -1, -1, 1])\n>>> A2 = Mat((set(range(97,123)),set(range(65,91))),{(x,y): 301-(7*((x-97)+26*(y-65))%761) for x in range(97,123) for y in range(65,91)})\n>>> b2 = Vec(A2.D[0], {x:1 for x in A2.D[0]})\n>>> print(test_format(find_grad(A1, b1, Vec(A1.D[1], {}))))\n>>> print(test_format(find_grad(A1, b1, Vec(A1.D[1], {x:-2 for x in A1.D[1]}))))\n>>> print(test_format(find_grad(A1, b1, Vec(A1.D[1], {x: (-1)**i for i, x in enumerate(sorted(A1.D[1]))}))))\n>>> print(test_format(find_grad(A2, b2, Vec(A2.D[1], {}))))\n>>> print(test_format(find_grad(A2, b2, Vec(A2.D[1], {x:-2 for x in A2.D[1]}))))\n>>> print(test_format(find_grad(A2, b2, Vec(A2.D[1], {x: (-1)**i for i, x in enumerate(sorted(A2.D[1]))}))))\n')], [('59qJbbUXhEMmAqc6ZznFxzJm5xqIbE3U', 'Gradient Descent Step', '>>> from vec import Vec\n>>> from mat import Mat\n>>> from vecutil import list2vec\n>>> from matutil import listlist2mat\n>>> A1 = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6], [10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])\n>>> b1 = list2vec([1, 1, -1, -1, 1])\n>>> A2 = Mat((set(range(97,123)),set(range(65,91))),{(x,y): 301-(7*((x-97)+26*(y-65))%761) for x in range(97,123) for y in range(65,91)})\n>>> b2 = Vec(A2.D[0], {x:1 for x in A2.D[0]})\n>>> print(test_format(gradient_descent_step(A1, b1, Vec(A1.D[1], {}), 2)))\n>>> print(test_format(gradient_descent_step(A1, b1, Vec(A1.D[1], {x:-2 for x in A1.D[1]}), 2)))\n>>> print(test_format(gradient_descent_step(A1, b1, Vec(A1.D[1], {x: (-1)**i for i, x in enumerate(sorted(A1.D[1]))}), 2)))\n>>> print(test_format(gradient_descent_step(A2, b2, Vec(A2.D[1], {}), 3)))\n>>> print(test_format(gradient_descent_step(A2, b2, Vec(A2.D[1], {x:-2 for x in A2.D[1]}), 3)))\n>>> print(test_format(gradient_descent_step(A2, b2, Vec(A2.D[1], {x: (-1)**i for i, x in enumerate(sorted(A2.D[1]))}), 3)))\n')]]
source_files        = ['machine_learning_lab.py'] * len(sum(groups,[]))

try:
    import machine_learning_lab as solution
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

