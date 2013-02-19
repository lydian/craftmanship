class node:
    def __init__(self, num):
        self.num = num
        self.children = []

    def add(self, child):
        if len(self.children) >= 2 : 
            print "error"
            return 
        else:
            self.children.append(child)

nodes = [node(i) for i in range(10)]
for n, node in enumerate(nodes):
    if n < len(nodes) -1:
        print nodes[n].num, "--", nodes[n].num
        node.add(nodes[n+1])
    if n < len(nodes) -1:
    node.add(node[n+2])

#def dfs(now, sum):

