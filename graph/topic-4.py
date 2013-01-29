# 924
import sys
from collections import deque

def findMin(source, friends):
    visited = dict([(i, False) for i in friends])
    traverse = deque([])
    visited[source] = True
    levels = {source: 0}
    max = 0
    while True:
        if len(friends[source]) == 0:
            break
        
        if len(friends[source]) > max:
            max = len(friends[source])

        print source, friends[source]
        print visited
        for f in friends[source]:
            if visited[f]: continue
            visited[f] = True
            levels[f] = levels[source]+1
            traverse.append(f)
        
        if len(traverse) == 0: break
        source = traverse.popleft()


    if len([i for i in visited if visited[i] == False]) != 0:
        print 0
    else:
        print max, levels[source]


friends = {}
num_people = int(sys.stdin.readline().strip())
for i in range(num_people):
    friends[i] = [int(f) for f in sys.stdin.readline().strip().split(" ")[1:]]
 
num_cases = int(sys.stdin.readline().strip())
for i in range(num_cases):
    source = int(sys.stdin.readline().strip())
    findMin(source, friends) 
