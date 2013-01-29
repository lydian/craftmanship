#http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=272

import sys, re
def run(now, ttl, nodes, visited):
    if ttl==-1:
        return
    for n in nodes[now]:
        if visited[n]: continue
        visited[n] = True
        run(n, ttl-1, nodes, visited)

def findPair(nodes, start, ttl):
    visited = dict([ (n,False) for n in nodes])
    visited[start] = True
    run(start, ttl-1, nodes, visited)
    all = [i for i in visited if visited[i] == False]
    return len(all)

line = sys.stdin.readline()
count = 0
while True:
    nodes = {}
    num_pairs = int(line)
    if num_pairs == 0 : break 
    while num_pairs > 0:
        line = sys.stdin.readline().strip()
        group = []
        for n in re.split(" +", line):
            group.append(n)
            if len(group) == 2:
                #find a pair
                if group[0] not in nodes:
                    nodes[group[0]] = []
                if group[1] not in nodes:
                    nodes[group[1]] = []
                nodes[group[0]].append(group[1])
                nodes[group[1]].append(group[0])
                num_pairs -= 1
                group = []
    
    cases = sys.stdin.readline().strip()
    group = []
    for n in re.split(" +", cases):
        group.append(int(n))
        if len(group) == 2:
            count += 1
            if group[0] == 0 and group[1] ==0: break
            result = findPair(nodes, str(group[0]), int(group[1]))
            print """Case %d: %d nodes not reachable from node %s with TTL = %d.""" % (count, result, group[0], int(group[1]))
            group=[]

    while True:
        line = sys.stdin.readline()
        if line.strip() != '': break

