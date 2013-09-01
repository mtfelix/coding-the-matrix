def myFilter(L, num): return [x for x in L if 0 == x%num]
def myLists(L): return [[y+1 for y in range(x)] for x in L]
def myConcat(L): 
    current = ""
    for x in L:
        current = current + str(x)
    return current
print(myConcat([1,2,5]))