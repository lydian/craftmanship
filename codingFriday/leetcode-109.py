import unittest

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def output_as_list(self):
        current_node = self
        output_list = []
        while current_node != None:
            output_list.append(current_node.val)
            current_node = current_node.next
        return output_list
    def get_length(self):
        n = 0
        current_node = self
        while current_node != None:
            n += 1
            current_node = current_node.next
        return n

    def convert_to_BST(self):
        length = self.get_length()
        return LinkedListNode.to_BST(self, 0, length -1)

    @staticmethod
    def to_BST(linkded_list, start, end):
        #print start, end 
        if start > end: return 
        
        mid = int(start + (end - start) / 2)
        left_child = LinkedListNode.to_BST(linkded_list, start, mid -1)
        if left_child != None:
            print  "left:", left_child.output_as_list()
        else:
            print "left: None"
        parent = TreeNode(linkded_list.val)
        parent.left = left_child
        
        parent.right = LinkedListNode.to_BST(linkded_list.next, mid+ 1 , end)
        if parent.right != None:
            print  "right:", parent.right.output_as_list()
        else:
            print "right: None"
        print parent.output_as_list()
        return parent

    @staticmethod
    def create_from_list(list):
        prev_node = None
        root_node = None
        for value in list:
            node = LinkedListNode(value)
            if prev_node == None:
                root_node = node
            else:
                prev_node.next = node
            prev_node = node
        return root_node

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get_max_level(self):
        if self.left == None and self.right == None: 
            return 1
        elif self.left != None and self.right == None:
            return  1  + self.left.get_max_level()
        elif self.left == None and self.right != None:
            return 1 + self.right.get_max_level()
        else:
            return 1 + max(self.left.get_max_level(), self.right.get_max_level()) 

    def output_as_list(self):
        output_list = []
        traverse_list = [self]
        current_position = 0 
        while len(traverse_list) > current_position:
            current_node = traverse_list[current_position]
            if current_node != None: 
                output_list.append(current_node.val)
                traverse_list.append(current_node.left)
                traverse_list.append(current_node.right)
            else:
                output_list.append("#")

            current_position += 1
       
        level = self.get_max_level()
        max_length = reduce(lambda a,b: a+b, map(lambda i: 2**i, range(0,level)))
        return output_list[:max_length]
    
    @staticmethod
    def create_from_list(list):
        root_node = None
        traverse_list = []
        last_position = 0
        for val in list:
            node = TreeNode(val)
            if root_node == None:
                root_node = node
                traverse_list.append(node)
            else:
                traverse_list.append(node)
                last_node = traverse_list[last_position]
                if last_node.left == None:
                    last_node.left = node
                elif last_node.right == None:
                    last_node.right = node
                    last_position += 1
        return root_node

class TestConversion(unittest.TestCase):
    def testTransformLinkedList(self):
        root_node = LinkedListNode.create_from_list([1, 2, 3, 4, 5])
        self.assertEqual(root_node.output_as_list(), [1,2,3,4,5])
    def testTransformTree(self):
        root_node = TreeNode.create_from_list([1, 2, 3, 4, 5])
        self.assertEqual(root_node.output_as_list(), [1,2,3,4,5,'#','#'])

    def testCoversion(self):
        root_node = LinkedListNode.create_from_list([-10,-3,0])
        print root_node.output_as_list()
        root_node = root_node.convert_to_BST()
        self.assertEqual(root_node.output_as_list(), [-3,-10,0])

if __name__ == '__main__':
    unittest.main()
