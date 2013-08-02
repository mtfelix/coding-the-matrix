voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    voting_dic = {}
    for s in voting_data:
        s = s.strip()
        items = s.split(' ')
        voting_dic[items[0]] = [int(v) for v in items[3:]]
    return voting_dic
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    assert len(voting_dict[sen_a]) == len(voting_dict[sen_b])
    return sum([voting_dict[sen_a][k]*voting_dict[sen_b][k] for k in range(0,len(voting_dict[sen_a]))])
    


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    score_map = {policy_compare(sen,another_guy,voting_dict):another_guy for another_guy in voting_dict.keys() if another_guy != sen}
    return score_map[max(score_map.keys())]

    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    score_map = {policy_compare(sen,another_guy,voting_dict):another_guy for another_guy in voting_dict.keys() if another_guy != sen}
    return score_map[min(score_map.keys())]
    return ""
    
    

## Task 5

most_like_chafee    = most_similar('Chafee',create_voting_dict())
least_like_santorum = least_similar('Santorum',create_voting_dict()) 



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    score_list = [policy_compare(sen,another_guy,voting_dict) for another_guy in sen_set]
    if 0 < len(score_list):
        return sum(score_list) / len(score_list)
    else:
        return 0

set_of_Democrat = set()
set_of_all_sen = set()
for s in voting_data:
    s = s.strip()
    items = s.split(' ')
    set_of_all_sen.add(items[0])
    if items[1] == 'D':
        set_of_Democrat.add(items[0])

score_sen_map = {find_average_similarity(sen,set_of_Democrat, create_voting_dict()):sen for sen in set_of_all_sen}
#-->Biden
most_average_Democrat = score_sen_map[max(score_sen_map.keys())] # give the last name (or code that computes the last name)

# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    assert len(sen_set) > 0
    rlt_vec = list()
    for sen in sen_set:
        rlt_vec = [0]*len(voting_dict[sen])
        break
    for sen in sen_set:
        for i in range(0, len(voting_dict[sen])):
            rlt_vec[i] += voting_dict[sen][i]/len(sen_set)
    return rlt_vec

average_Democrat_record = find_average_record(set_of_Democrat, create_voting_dict()) # (give the vector)

new_vd = create_voting_dict()
new_vd['ALLDemocrat'] = average_Democrat_record
most_average_Democrat2 = most_similar('ALLDemocrat', new_vd)
# yea, Biden again
#print(most_average_Democrat2) 

    

# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    score_person_pair_dic = {policy_compare(p1,p2,voting_dict):(p1,p2) for p1 in voting_dict.keys() for p2 in voting_dict.keys()}
    return score_person_pair_dic[min(score_person_pair_dic.keys())]

