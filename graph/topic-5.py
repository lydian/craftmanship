#http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=480
import sys

def run(start, now, length, visited, nodes):
    for next in nodes[now]:
        if visited[next] == True:
            return 
        
        else:
            visited[next] = True
            length[start] +=1
            r = run(start, next, length, visited, nodes)
            visited[next] = False
            return r

def find(nodes):
    lengths = dict([(node, 0) for node in nodes])
    max = 0
    for n in nodes:
        visited = dict([(node, False) for node in nodes])
        run(n, n,  lengths, visited, nodes)
    print lengths

while True:
    m,n = [int(i) for i in sys.stdin.readline().strip().split(" ")]
    if m == 0 and n == 0: break
    cities = {}
    edges = {} 
    for i in range(n):
        a,b = [int(i) for i in sys.stdin.readline().strip().split(" ")]
        e_id = len(edges)
        edges[ e_id ] = (a, b)
        if a not in cities: cities[a] = []
        cities[a].append( [b, e_id])
        if b not in cities: cities[b] = []
        cities[b].append( [a, e_id])
    nodes = {}
    for e_id in edges: 
        nodes[e_id] = []
        nodes[e_id].extend([edge  for city,edge in cities[edges[e_id][0]] if edge!=e_id])
        nodes[e_id].extend([edge  for city,edge in cities[edges[e_id][1]] if edge != e_id])
        nodes[e_id] = list(set(nodes[e_id]))

    print find(nodes)

