## Task 1
minutes_in_week = 10080

## Task 2
remainder_without_mod =  2304811 - (2304811//47)*47

## Task 3
divisible_by_3 =  0 == ((673 + 909) % 3)

## Task 4
x = -9
y = 1/2
statement_val = 2**(y+1/2) if x+10<0 else 2**(y-1/2)

## Task 5
first_five_squares = { x**2 for x in {1,2,3,4,5} }

## Task 6
first_five_pows_two = { 2**x for x in {0,1,2,3,4} }

## Task 7: enter in the two new sets
X1 = { 1, 3, 5 }
Y1 = { 4, 5, 6 }

## Task 8: enter in the two new sets
X2 = { 0, 2, 3 }
Y2 = { 4, 6, 9 }
### I (Hongfei Jiang) got the results for task 8 using following codes:
#D = {1,2,3,4,5,6,7,8,9,0}
#list = [[x1,x2,x3,x4,x5,x6] for x1 in D for x2 in D for x3 in D for x4 in D for x5 in D for x6 in D if len({x1,x2,x3,x4,x5,x6}) == 6 and len({x*y for x in {x1,x2,x3} for y in {x4,x5,x6}})==5 ] 
#print(list)

## Task 9
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = {x+y*(base**1)+z*(base**2) for x in digits for y in digits for z in digits}

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = { x for x in S if x in T  }

## Task 11
L_average = sum([20, 10, 15, 75])/len([20, 10, 15, 75]) # average of: [20, 10, 15, 75]

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = sum([sum(x) for x in LofL]) # use form: sum([sum(...) ... ])

## Task 13
#cartesian_product = ... # use form: [ ... {'A','B','C'} ... {1,2,3} ... ]
cartesian_product = [ [x,y] for x in {'A','B','C'} for y in {1,2,3}]  # use form: [ ... {'A','B','C'} ... {1,2,3} ... ]


## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [(i,j,k) for i in S for j in S for k in S if sum([i,j,k]) == 0]

## Task 15
exclude_zero_list = [(i,j,k) for i in S for j in S for k in S if (sum([i,j,k]) == 0 and {i,j,k}!={0,0,0})]

## Task 16
first_of_tuples_list = [(i,j,k) for i in S for j in S for k in S if (sum([i,j,k]) == 0 and {i,j,k}!={0,0,0})][0]

## Task 17
L1 = [0,1,0] # <-- want len(L1) != len(list(set(L1)))
L2 = [3,'a',1] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))

## Task 18
odd_num_list_range = {x for x in range(1,100,2)}

## Task 19
L = ['A','B','C','D','E']
range_and_zip = list(zip(range(5),L))

## Task 20
list_sum_zip = [x+y for (x, y) in zip([10,25,40],[1,15,20])]

## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [...]

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [...] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [...] # <-- as you do here

## Task 23
square_dict = {...}

## Task 24
D = {'red','white','blue'}
identity_dict = {...}

## Task 25
base = 10
digits = set(range(10))
representation_dict = {...}

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = { ... }

## Task 27
def nextInts(L): return [ ... ]

## Task 28
def cubes(L): return [ ... ] 

## Task 29
def dict2list(dct, keylist): return [ ... ]

## Task 30 
def list2dict(L, keylist): return { ... } 

