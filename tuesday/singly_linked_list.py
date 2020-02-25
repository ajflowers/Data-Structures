## How do you find and return the middle node of a singly linked list in one pass? You do not have access to the length of the list. If the list is even, you should return the first of the two “middle” nodes. You may not store the nodes in another data structure.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def add(self, value):
        self.next = Node(value)

# create singly linked list class w/ self.head pointing to beginning of list
#initialize two pointers at head
#increment first pointer by 1, second pointer by 2
#if second pointer is at node w/ next = none, it's at the end and length is odd
#if 2nd has reached none value, it has overshot end and length is even


class SinglyLinkedList:
    def __init__(self, node=None):
        self.head = node

    def find_middle(self):
        fast_node = self.head
        slow_node = self.head

        while True:
            fast_node = fast_node.next.next
            if fast_node is None:
                return slow_node.value
            elif fast_node.next is None:
                return slow_node.next.value
            else:
                slow_node = slow_node.next

    #How do you reverse a singly linked list without recursion? You may not store the list, or it’s values, in another data structure.

    def add_to_head(node):
        node.next = self.head

    def reverse(self):
        pointer = self.head
        


node1 = Node(1)

sll = SinglyLinkedList(node1)
node1.add(2)
node1.next.add(3)
node1.next.next.add(4)
node1.next.next.next.add(5)
# node1.next.next.next.next.add(6)

print(sll.find_middle())

