class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Singly Linked
    def __init__(self):
        self.head = None

    def insert(self, data):
        # O(1)

        if not self.head:
            self.head = Node(data)
        else:
            n = self.head
            self.head = Node(data)
            self.head.next = n

    def insert_many(self, data):
        for d in data:
            self.insert(d)

    def print(self):
        n = self.head
        while n:
            print(n.data, end=" -> ")
            n = n.next
        print("None")

################################################################
# Implement an algorithm to delete a node in the middle (not first or last) of a singly linked list,
# given only access to that node

# In: node c from a->b->c->d->e
# Effects: a->b->d->e

# time: O(1), space: O(1)
def deleteMiddleNode(node: Node):
    if node and node.next:
        next_node = node.next
        node.data = node.next.data
        node.next = node.next.next
        del next_node # optional in python

    

# tests
llist = LinkedList()
llist.insert_many(['e', 'd', 'c', 'b', 'a'])
llist.print()
deleteMiddleNode(llist.head.next.next)
llist.print()
