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

URL               = 'matrix-001'
partFriendlyNames = ['Movie Review', 'Dictionary Utilities', 'List Range to Dictionary', 'Make Inverse Index', 'Or Search', 'And Search']
groups            = [[('jW1JmPJ7MxozuKUU', 'Movie Review', '>>> print(test_format(len({movie_review(str(randint(1,300))) for _ in range(300)})))\n')], [('u6z9uemgY2XO5i8b', 'Dictionary Utilities', '>>> import dictutil\n>>> print(test_format(dictutil.dict2list({1:2},[1])))\n>>> print(test_format(dictutil.list2dict([2],[1])))\n')], [('1W5vN6D5KTioevrb', 'List Range to Dictionary', ">>> print(test_format([listrange2dict(l) for l in [[0,1,2],['a','b'], range(100)]]))\n")], [('i06zNsrbnOmf4ASS', 'Make Inverse Index', '>>> stories = list(open("stories_small.txt"))\n>>> idx = makeInverseIndex(stories)\n>>> print(test_format([idx[w] for w in [\'leaving\', \'Florida\', \'After\', \'debate\', \'workers\', \'For\', \'use\']]))\n')], [('LEmkQURt338uFT3y', 'Or Search', '>>> stories = list(open("stories_small.txt"))\n>>> idx = makeInverseIndex(stories)\n>>> print(test_format(orSearch(idx, [\'travelers\', \'use\', \'Baltimore\', \'major-league\', \'whether\'])))\n')], [('7D2cgEQeGuInopfV', 'And Search', '>>> stories = list(open("stories_small.txt"))\n>>> idx = makeInverseIndex(stories)\n>>> print(test_format(andSearch(idx, [\'made\', \'are\'])))\n>>> print(test_format(andSearch(idx, [\'the\', \'in\', \'use\', \'times\'])))\n')]]
sourceFiles       = ['inverse_index_lab.py'] * len(sum(groups,[]))

try:
    import inverse_index_lab as solution
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
        fstr = '%%.%dg' % precision
        return fstr % obj
    elif otype is set:
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
    return ''.join(map(str.rstrip, runner.results))

test_vars['test_format'] = test_vars['tf'] = test_format
test_vars['find_lines'] = find_lines
test_vars['find_line'] = find_line
test_vars['use_comprehension'] = use_comprehension
test_vars['double_comprehension'] = double_comprehension
test_vars['line_contains_substr'] = line_contains_substr


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

challenge_url = 'https://class.coursera.org/%s/assignment/challenge' % URL
submit_url    = 'https://class.coursera.org/%s/assignment/submit'    % URL

def submit():   
    print('==\n== Submitting Solutions \n==\n')
    
    (login, password) = loginPrompt()
    if not login:
        print('!! Submission Cancelled')
        return
    
    print('\n== Connecting to Coursera ... \n')

    parts = partPrompt()
    if parts is None: return

    while len(parts) == 0:
        print('\n!! Cannot submit ungraded parts')
        parts = partPrompt()

    for (sid, name, part_tests) in parts:
        print('\n== Submitting "%s" \n' % name)

        if 'DEV' in os.environ: sid += '-dev'

        (login, ch, state, ch_aux) = getChallenge(login, sid)

        if (not login) or (not ch) or (not state):
            print('\n!! Error: %s\n' % login)
            return

        # to stop Coursera's strip() from doing anything, we surround in parens
        prog_out = '(%s)' % output(part_tests) 
        token    = challengeResponse(login, password, ch)
        src      = source(sid)

        if 'DEBUG' in os.environ: print('==== Output: %s' % prog_out.replace('\n','\\n'))
        
        feedback = submitSolution(login, token, sid, prog_out, src, state, ch_aux)

        if len(feedback.strip()) > 0:
            print('==== Feedback: %s\n' % feedback.strip())


def loginPrompt():
    """Prompt the user for login credentials. Returns a tuple (login, password)."""
    if 'COURSERA_EMAIL' in os.environ:
        login = os.environ['COURSERA_EMAIL']
    else:
        login = input('Login email address: ')

    if 'COURSERA_PASS' in os.environ:
        password = os.environ['COURSERA_PASS']
    else:
        password = input("One-time password from the assignment page (NOT your own account\'s password): ")
    return login, password

def partPrompt():
    print('These are the assignment parts that you can submit:\n')

    for i, name in enumerate(partFriendlyNames):
        print('  %d) %s' % (i+1, name))

    def extract_range(s):
        s = s.split('-')
        if len(s) == 1: return [int(s[0])]
        else: return list(range(int(s[0]), 1+int(s[1])))

    their_input = input('\nWhich parts do you want to submit? (Ex: 1, 4-7): ')
    parts = map(extract_range, their_input.split(','))
    flat_parts = sum(parts, [])
    return sum(list(map(lambda p: groups[p-1], flat_parts)),[])

def getChallenge(email, sid):
    """Gets the challenge salt from the server. Returns (email,ch,state,ch_aux)."""
    values = {'email_address' : email,
              'assignment_part_sid' : sid,
              'response_encoding' : 'delim'
             }
  
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(challenge_url, data)
    response = urllib.request.urlopen(req)
    text = response.readall().decode('utf-8').strip()
  
    # text is of the form email|ch|signature
    splits = text.split('|')
    if len(splits) != 9:
        print('Badly formatted challenge response: %s' % text)
        sys.exit(1)
    return (splits[2], splits[4], splits[6], splits[8])

def challengeResponse(email, passwd, challenge):
    sha1 = hashlib.sha1()
    sha1.update(('%s%s' % (challenge, passwd)).encode('utf-8'))
    return ''.join(sha1.hexdigest())


def submitSolution(email_address, ch_resp, sid, output, source, state, ch_aux):
    """Submits a solution to the server. Returns (result, string)."""

    source_64 = str(base64.encodebytes(source.encode('utf-8')), 'ascii')
    output_64 = str(base64.encodebytes(output.encode('utf-8')), 'ascii')

    values = { 'assignment_part_sid' : sid,
               'email_address'       : email_address,
               'submission'          : output_64,
               'submission_aux'      : source_64,
               'challenge_response'  : ch_resp,
               'state'               : state
             }

    data     = urllib.parse.urlencode(values).encode('utf-8')
    req      = urllib.request.Request(submit_url, data)
    response = urllib.request.urlopen(req)
    string   = response.readall().decode('utf-8').strip()

    return string

def source(sid):
    """ This collects the source code, for logging purposes. """
    f = open(sourceFiles[0])
    src = f.read() 
    f.close()
    return src

if __name__ == '__main__':
    submit()
