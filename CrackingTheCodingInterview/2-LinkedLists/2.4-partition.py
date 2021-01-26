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
# Write code to partition a linked list around a value x such that all nodes less than x come before all nodes greater than or equal to x

# in: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1, partition=5
# out: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


# time: O(n), space: O(1)
def partition(llist: LinkedList, x: int):
    head = tail = node = llist.head
    while node:
        next_node = node.next
        if node.data < x:   # prepend node
            node.next = head
            head = node
        else:               # append node
            tail.next = node
            tail = node
        node = next_node

    tail.next = None
    llist.head = head

# tests
llist = LinkedList()
llist.insert_many([1, 2, 10, 5, 8, 5, 3])
llist.print()
partition(llist, 5)
llist.print()
