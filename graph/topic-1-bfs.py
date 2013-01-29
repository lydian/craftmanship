#http://www.careercup.com/question?id=14800913
#Longest posibble path in a tree, you had to return the end leaf nodes.

# input:
# 5 - 3 - 1
#   \ 9 - 6
#       \10

from collections import deque
class Node:
    def __init__(self,name):
        self.name = name
        self.children = {}
    def addChild(self, child):
        self.children[child.name] = child


nodes = dict([(i, Node(i)) for i in [1,3,5,6,9,10,11]])
nodes[5].addChild(nodes[3])
nodes[5].addChild(nodes[9])
nodes[3].addChild(nodes[1])
nodes[9].addChild(nodes[6])
nodes[9].addChild(nodes[10])
nodes[10].addChild(nodes[11])

queue = deque([])
node = nodes[5]
node.depth = 0
while True:
    for child_name in node.children:
        nodes[child_name].depth = node.depth +1
        queue.append((nodes[child_name]))
    if len(queue) == 0:
        break
    node = queue.popleft()

print "depth:", node.depth
for i in nodes:
    if nodes[i].depth == node.depth:
        print i

