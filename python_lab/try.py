
D = {1,2,3,4,5,6,7,8,9,0}
list = [[x1,x2,x3,x4,x5,x6] for x1 in D for x2 in D for x3 in D for x4 in D for x5 in D for x6 in D if len({x1,x2,x3,x4,x5,x6}) == 6 and len({x*y for x in {x1,x2,x3} for y in {x4,x5,x6}})==5 ] 
print(list)