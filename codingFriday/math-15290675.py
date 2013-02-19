
def find(num, possible):
    sum = 0
    if len(possible)>1: sum = reduce(lambda x, y: x+y, possible)
    if sum >= num:
        if sum == num: print possible
        return
    
    for i in range(1, num):
        possible.append(i)
        find(num, possible)
        possible.pop()

for i in range(1,6):
    print i
    find(i,[])
