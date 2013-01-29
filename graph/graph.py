from collections import deque
class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def getGraph(self, file):
        f = open(file)
        for line in f:
            nodes = [Node(n) for n in line.strip().split(" ")]
            for n in nodes: self.nodes[n.name] = n
            self.edges.append(Edge(nodes[0], nodes[1]))

    def addEdge(self, a, b):
        if a in self.nodes:
            nodeA = self.nodes[a]
        else:
            nodeA = Node(a)
            self.nodes[a] = nodeA
        if b in self.nodes:
            nodeB = self.nodes[b]
        else:
            nodeB = Node(b)
            self.nodes[b] = nodeB
        
        self.edges.append(Edge(nodeA, nodeB))

    def __repr__(self):
        s = []
        for e in self.edges:
            s.append(str(e))
        return "\n".join(s)

    def sample(self):
        self.nodes = {}
        self.edges = []
        self.addEdge(1, 2)
        self.addEdge(1, 3)
        self.addEdge(2, 3)
        self.addEdge(2, 5)
        self.addEdge(3, 4)
        self.addEdge(5, 7)
        self.addEdge(6, 8)
        print '''
1 - 2 - 5 - 7 
 \  |
  \ 3 - 4
6 - 8
'''
    def dfs2(self):
        stack = []
        traverse = []
        visited = dict([(n, False) for n in self.nodes])
        for n in self.nodes:
            if visited[n]: continue
            start = self.nodes[n]
            visited[n] = True
            traverse.append(start)
            while(1):
                for neighbor in start.neighbors:
                    if visited[neighbor.name]: continue
                    traverse.append(neighbor)
                    visited[neighbor.name] = True
                    stack.append(neighbor)
                if len(stack) == 0:
                    break
                start = stack.pop()
        print traverse

    def dfs(self, path, visited):
        start = path[-1]
        not_visited = [ i for i in start.neighbors if visited[i.name] == False]
        if len(not_visited) == 0:
            print path
            return
 
        for node in start.neighbors:
            if visited[node.name] == True: continue
            visited[node.name] = True
            path.append(node)
            self.dfs(path, visited )
            path.pop()
    
    def bfs(self):
        queue = deque([])
        traverse = []
        visited = dict([(n, False) for n in self.nodes])
        for n in self.nodes:
            if visited[n]: continue
            start = self.nodes[n]
            traverse.append(start)
            visited[n] = True
            while(1):
                for neighbor in start.neighbors:
                    if visited[neighbor.name]: continue
                    visited[neighbor.name] = True
                    traverse.append(neighbor)
                    queue.append(neighbor)
                if len(queue) == 0:
                    break
                start = queue.popleft()
        print traverse


class Edge:
    def __init__(self, a, b):
        self.nodeA = a
        self.nodeB = b
        a.addNeighbor(b)
        b.addNeighbor(a)

    def __repr__(self):
        return str(self.nodeA) + "---" + str(self.nodeB)

class Node: 
    def __init__(self,name):
        self.name = name
        self.neighbors = []
    def addNeighbor(self,neighbor):
        self.neighbors.append(neighbor)

    def getNeighbors(self):
        return self.neighbors

    def __repr__(self):
        return "Node[" + str(self.name) + "]"

def testDFS(g):
    visited = dict([(a, False) for a in g.nodes])
    visited[g.nodes[1].name] = True
    g.dfs([g.nodes[1]], visited)

def testDFS_loop(g):
    g.dfs2()

def testBFS(g):
    start = g.nodes[1]
    path = [start]
    g.bfs()

if __name__ == "__main__":
    g = Graph()
    g.sample()
    print "DFS - find path:"
    testDFS(g)
    print "DFS traversal- loop:"
    testDFS_loop(g)
    
    print "BFS traversal:"
    testBFS(g)
