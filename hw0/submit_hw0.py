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

URL                 = 'matrix-001'
part_friendly_names = ['Python Comprehensions: Filtering', 'Python Comprehensions: Lists of Lists', 'Python Comprehensions: Function Composition', 'Complex Addition Practice', 'GF(2) Arithmetic', 'Summing numbers in a list', 'Multiplying numbers in a list', 'Minimum of a list', 'Concatenation of a List', 'Union of Sets in a List']
groups              = [[('gv45JFu2O10IPxYA', 'Python Comprehensions: Filtering', '>>> l = [24, 60, 120, 130]\n>>> print(test_format(myFilter(l, 1)))\n>>> print(test_format(myFilter(l, 400)))\n>>> print(test_format(myFilter(l, 8)))\n')], [('Z9NGhxaoEQbmjYJH', 'Python Comprehensions: Lists of Lists', '>>> print(test_format(myLists([0, 0, 0])))\n>>> print(test_format(myLists([1, 2, 3])))\n>>> print(test_format(myLists([4, 2, 0])))\n')], [('Zwko9KLTikR7j7Ki', 'Python Comprehensions: Function Composition', ">>> f = {0:'a', 1:'b'}\n>>> g = {'a':'apple', 'b':'banana'}\n>>> print(test_format(myFunctionComposition(f, g)))\n>>> f = {1:'q', 3:'w', 0:'e', 2:'r'}\n>>> g = {'w':'ace', 'e':'vet', 'q':'pot', 'r':'bat'}\n>>> print(test_format(myFunctionComposition(f, g)))\n")], [('ZpBBYvZM0gzozTf9', 'Complex Addition Practice, Part 1', '>>> print(test_format(complex_addition_a))\n'), ('m3RyKG2J9LG5L52R', 'Complex Addition Practice, Part 2', '>>> print(test_format(complex_addition_b))\n'), ('GenQi4GcQM8hdFlY', 'Complex Addition Practice, Part 3', '>>> print(test_format(complex_addition_c))\n'), ('iKXsc49APL88NCSu', 'Complex Addition Practice, Part 4', '>>> print(test_format(complex_addition_d))\n')], [('bkzn4cWKrDF41tuV', 'GF(2) Arithmetic, Part 1', '>>> print(test_format(GF2_sum_1))\n'), ('7DSb4Mjn6Iaqjvmp', 'GF(2) Arithmetic, Part 2', '>>> print(test_format(GF2_sum_2))\n'), ('Q7kNzUgXt2YLrENt', 'GF(2) Arithmetic, Part 3', '>>> print(test_format(GF2_sum_3))\n')], [('nnNZ6rSVx1Lhu3q3', 'Summing numbers in a list', '>>> print(test_format(mySum([1,2,3,4,5])))\n>>> print(test_format(mySum([8164, 1964, 4619, 2432, 8105, 4519, 1645, 6169, 507, 2196, 9946, 2330, 2854, 9261, 7432, 2915, 8787, 7486, 7585, 861, 4171, 9860, 2870, 7983, 7736, 8966, 1879, 6451, 3958, 4089, 5528, 1399, 4230, 9332, 4931, 8135, 869, 7672, 9161, 6570, 4478, 6140, 3857, 9427, 8348, 6882, 4183, 3417, 8160, 2365])))\n>>> print(test_format(mySum([4500, 8117, 1907, 9899, 5719, 584, 2363, 547, 9576, 4465, 724, 5931, 7480, 3992, 5250, 8625, 5245, 8895, 7832, 5528, 2591, 3608, 4563, 2683, 5633, 4322, 2050, 7836, 9372, 1264, 1209, 8529, 6291, 3167, 7427, 1271, 6868, 5574, 5561, 8523, 5788, 3968, 2337, 9012, 5293, 8911, 5187, 5587, 7294, 7452])))\n')], [('PoZ7GYg1Ewv8cHaG', 'Multiplying numbers in a list', '>>> print(test_format(myProduct([1,2,3,4,5])))\n>>> print(test_format(myProduct([5310, 3433, 5531, 7696, 8319, 8765, 956, 9875, 1664, 6175, 7757, 1129, 1008, 4766, 6138, 8200, 6641, 3677, 2129, 9127, 3265, 6157, 5326, 3765, 4576, 5672, 7474, 6576, 2749, 4750, 218, 2908, 6595, 7732, 2923, 1328, 3440, 6544, 420, 8323, 3754, 7268, 6492, 921, 256, 6537, 6649, 9590, 1918, 9452])))\n>>> print(test_format(myProduct([6870, 3697, 9664, 6568, 6626, 6358, 4001, 9836, 7573, 103, 6069, 435, 3302, 5744, 6014, 5891, 7474, 6569, 5921, 4403, 5787, 5497, 1765, 6661, 3811, 3618, 9742, 4886, 3353, 9392, 9065, 1861, 2556, 2470, 8072, 1670, 2046, 2261, 6080, 7201, 7578, 35, 8178, 5455, 4439, 6005, 843, 2752, 3259, 8945])))\n')], [('2OXyh1iVD9D0gZOP', 'Minimum of a list', '>>> print(test_format(myMin([5,2,4,7,4])))\n>>> print(test_format(myMin([4390, 8557, 9868, 5303, 2153, 4409, 9245, 1431, 1865, 9451, 4448, 8864, 3051, 4930, 951, 1173, 4534, 6540, 3080, 4583, 14, 6039, 2296, 4361, 1796, 2359, 2750, 3357, 1401, 6568, 4570, 9643, 854, 1844, 8994, 3468, 7654, 3192, 2956, 3346, 95, 875, 1671, 1116, 1611, 7554, 8299, 7631, 6104, 2502])))\n>>> print(test_format(myMin([899, 8048, 429, 7731, 7465, 5454, 1923, 4509, 1441, 5916, 2155, 9467, 4499, 2303, 8331, 9658, 2650, 9222, 9593, 6473, 6611, 9157, 2219, 4596, 1669, 7200, 5329, 9282, 7523, 7457, 8643, 3078, 1189, 1818, 1151, 8058, 6410, 8307, 5229, 7533, 3836, 2357, 2014, 2658, 6964, 3294, 6519, 9242, 1240, 2632])))\n')], [('a5WTpgLaqwe4Isp6', 'Concatenation of a List', ">>> import hashlib\n>>> print(test_format(hashlib.md5(myConcat(['rolnmcaipe', 'bopsjvkhxz', 'alhtcriyub', 'lxmunfkpcz', 'vpsikhtflg', 'qrwnhtfuxg', 'wvofecpxbn', 'tkjawldvqm', 'blznrdkjcf', 'dpromgblct', 'gswrnxivda', 'gyjbaldcxu', 'ldercanzgi', 'mnflwaedop', 'tehilkboup', 'abspyehcoi', 'amqhtulexg', 'qczasxmuyf', 'qxvzjudgko', 'ylucajwrfk', 'tivlnksdob', 'nbqmcelfzw', 'zngmbkxwsi', 'xhurdszbwe', 'nwigkzphyu', 'loufhrsnav', 'vrexwiuhyf', 'yuanbxehrw', 'dovbhitsju', 'lgxukpfayw', 'lawnbyrcit', 'nsxloghdzi', 'wgbyajloiv', 'pargnymzfc', 'kuhspewzjb', 'mpvayrhels', 'klxudpihny', 'sneapfohwu', 'bwclzgvtmh', 'wuceqtlrio', 'xbgezaiwvk', 'fklyhzjotx', 'bwzalcvhof', 'eapyjoidgt', 'ruxvimzcyw', 'rkgezstlum', 'ubwkoznhgl', 'cpoijlmwes', 'eqfhkgmxrc', 'abcfrwmztx', 'npesjzhdia', 'opvhrzgten', 'uixemtayfc', 'nkvjqtbszd', 'hjerkaxmqd', 'qvmnscgjxa', 'jrhmafnyvk', 'routmqeyki', 'ubqkjmvocn', 'yaptwcenqj', 'mdegpuslyk', 'kqhezlpvsn', 'hbfcdepjxa', 'jsdwoxgcqe', 'vgzophscmn', 'kvhniafpjc', 'mobtvykenh', 'opsilmznex', 'sfwtvyxuml', 'yuminqrhgo', 'lcyfsrjduz', 'vjxnhkabcu', 'uwxkaejotd', 'bfcjopiulm', 'ekwrtphvon', 'jktfryduvc', 'nbqvldpofi', 'pbhjrivazs', 'gzfkxjqvlw', 'mzylopudsh', 'uhjdkovtme', 'ebxtlmjpck', 'yezmlarvps', 'clwbdmoagp', 'epnwzxhjgv', 'tfaveismjw', 'xmqusyfvbe', 'uiywrzqgep', 'lwutsaypiq', 'bzaxwumvjh', 'zqlgjshbir', 'wfistgdope', 'azwkvxympf', 'xteidsjgwn', 'jswauobpzd', 'fpstnmxugy', 'qsgnuydjxm', 'nlcosrpubz', 'erknqbjmud', 'ziduqlwabg']).encode()).hexdigest()))\n>>> print(test_format(myConcat(['he', 'll', 'ow','or','ld'])))\n>>> print(test_format(hashlib.md5(myConcat(['jyrwnfaekq', 'yqeljvspin', 'ysxrcpdvmz', 'mpgvfordix', 'fhzjxcbgvr', 'jleipntzvx', 'qyvlhxcotu', 'whaiptsfuc', 'sfoaybnqch', 'hxodqwuyec', 'ibnuyvrzqg', 'mrepshvtyc', 'gdeszmhoqa', 'qjmsnczduv', 'hyrwpdeluc', 'fhdoprilze', 'gvprbcejuy', 'upwzqlmsyh', 'orvgyfkcie', 'brxycavszh', 'rldhqazvfx', 'nrfsydpoht', 'gotmuhdkvp', 'qtfcjugrdv', 'qpfwuelbzx', 'lremuckqfw', 'oguwenbdav', 'gcsjnopyqr', 'pmtoeuigys', 'pesahbcwdy', 'cfiybgkpho', 'zaqwbkuyvj', 'dtcbwrmqji', 'mjygopznus', 'edbajtrwhs', 'kvywatjgir', 'mwcsrailtj', 'soxqcynvmr', 'ixavjybuge', 'ajlfsbcimw', 'wifnkyepgt', 'lkfnxqgmta', 'ojgcuxnylb', 'btejgdrplu', 'cnjfmbsxer', 'niaupcyevz', 'dyqhnbipaf', 'qvtycnwrop', 'xcdrmpefzl', 'mxqynravzf', 'rymuxbctow', 'owrlhzgmds', 'cxozkwhais', 'axnvwfgidc', 'obkgftselm', 'cbazgqewix', 'vsxqwkbump', 'rhmnyvkxua', 'kqtyjbaugp', 'jozgmlqbyk', 'yegqluozrx', 'nxleihzcyu', 'ldhyvntiwc', 'okrhpxdwgv', 'xusrzmildy', 'uxrhifplem', 'crpxhdyksz', 'frkdpqstvb', 'hxnjatyvgf', 'zgjabroyxd', 'dfthcrnugo', 'hrxindytgm', 'riwzgchytx', 'naysmkzvld', 'rfvsiaqxoz', 'tfrouxzhbv', 'zeqydinkrs', 'gcpblyiofk', 'jnsbqvogpi', 'idzvrweqnj', 'arpfgwzqyi', 'vasghowike', 'zxtighumkj', 'pokqudvnlj', 'gmqljakfrv', 'frqblatkzn', 'fxmewlgzcr', 'qjmsfixodn', 'sdwtjhkrao', 'crytljgfiu', 'hrvcoxyafb', 'nxbpitedsj', 'qrasxmlguw', 'gwfsqpvmtx', 'rowdsjemgf', 'hbcatpgzrv', 'srbcdiohfn', 'inqwcbulrg', 'eovdhwtlcb', 'aynmdreols']).encode()).hexdigest()))\n")], [('qIKxBeFR4U19krlA', 'Union of Sets in a List', '>>> print(test_format(myUnion([{1,2,3},{2,3,4}])))\n>>> print(test_format(myUnion([set(),{1,2}])))\n>>> print(test_format(myUnion([])))\n>>> print(test_format(myUnion([{31, 61, 27, 88, 98, 22, 16, 86, 99, 35}, {42, 85, 78, 4, 10, 26, 76, 91, 63, 2}, {76, 5, 5, 81, 69, 0, 27, 64, 74, 56}, {20, 12, 23, 39, 90, 68, 15, 55, 41, 57}, {64, 43, 15, 96, 12, 99, 37, 53, 75, 99}, {9, 75, 9, 91, 26, 7, 79, 28, 46, 50}, {21, 13, 1, 56, 92, 47, 9, 15, 77, 79}, {16, 68, 41, 99, 57, 90, 10, 68, 49, 91}, {85, 44, 54, 12, 97, 64, 63, 81, 37, 56}, {36, 5, 76, 13, 63, 36, 63, 67, 62, 27}])))\n')]]
source_files        = ['hw0.py'] * len(sum(groups,[]))

try:
    import hw0 as solution
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
    elif otype is float:
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

