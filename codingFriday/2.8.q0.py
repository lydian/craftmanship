
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def traverse(head):
    current = head
    array = []
    while current!= None:
        array.append(current.val)
        current = current.next
    return array

def create(array):
    if len(array) == 0: return None
    head = Node(array[0])
    current = head
    for item in array[1:]:
        node = Node(item)
        current.next = node
        current = node
    return head

def remove(head):
    prev = head
    if prev == None: return head
    current = prev.next
    last = prev.val
    while current != None:
        if last == current.val:
            prev.next = current.next
        else:
            prev = current
            last = current.val
        current = current.next
    return head

def test(A):
    head = create(A)
    print traverse( remove(head))


A = [1,2,3,3,3,4, 4, 5]
test(A)
A = []
test(A)
A = [-1, 2,2,2,3,3,3,4,4,4,4,4,4,5,7, 8]
test(A)
