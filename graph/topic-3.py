# 247
#
import sys
#          |----->Aron
# Ben -> Alex -> Dolly <-> Benedict
#  ^---------------|
def run(path, visited, data, circles):
    start = path[-1]
    if visited[start]:
        if start != path[0]: return
        mini = min([circles[i] for i in path])
        for n in path:
            for n2 in data:
                if circles[n2] == circles[n]:
                    circles[n2] = mini
            circles[n] = mini
        return

    visited[start] = True
    for neighbor in data[start]:
        path.append(neighbor)
        run(path, visited, data, circles)
        path.pop()
    visited[start] = False

def find(data):
    visited = dict([(n,False) for n in data])
    circles = dict([ (p, i) for i, p in enumerate(data.keys())])
    for p in data:
        if visited[p] == True: continue
        path = run([p], visited, data, circles)
        visited[p] = False

    groups = {}
    for p in circles:
        if circles[p] not in groups:
            groups[circles[p]] = []
        groups[circles[p]].append(p)

    return  [groups[g] for g in groups if len(groups[g])>0]


n, m =  [int(n) for n in sys.stdin.readline().strip().split(" ")]
count = 1
while True:
    if n==0 and m==0:
        break
    data = {}
    for i in range(m):
        A, B = sys.stdin.readline().strip().split(" ")
        if A not in data:
            data[A] = []
        if B not in data:
            data[B] = []
        data[A].append(B)
    groups = find(data)
    
    print "Calling circles for data set %d:" % count
    for g in groups:
        print ", ".join(g)
    print
    n, m =  [int(n) for n in sys.stdin.readline().strip().split(" ")]
    count += 1


