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
# Write code to remove duplicates from a list

def delete_from(llist: LinkedList, start: Node, data):
    if not llist.head:
        return

    n = start
    while n.next:
        if n.next.data == data:
            n.next = n.next.next
        else:
            n = n.next

# time: O(n^2), space: O(1)
def removeDups1(llist: LinkedList):
    n = llist.head
    while n.next:
        delete_from(llist, n.next, n.next.data)
        n = n.next

# time: O(n), space: O(n)
def removeDups2(llist: LinkedList):
    seen = []
    n = llist.head
    prev = None
    while n:
        if n.data in seen:
            prev.next = n.next
        else:
            seen.append(n.data)
            prev = n
        n = n.next

# tests
llist = LinkedList()
llist.insert_many([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1, 1, 9])
llist.print()
removeDups2(llist)
llist.print()
