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
# Implement an algorithm to return the Kth to last element of a singly linked list.

# time: O(n), O(1)
def kthToLast1(llist: LinkedList, k: int):
    length = 0
    n = llist.head
    while n:
        n = n.next
        length += 1

    if length - k < 0:
        return None
    
    n = llist.head
    for _ in range(length - k):
        n = n.next
    return n.data

# small optimization (sliding window)
# time: O(n), space: O(1)
def kthToLast2(llist: LinkedList, k: int):
    n = llist.head
    n_minus_k = llist.head
    while n:
        n = n.next
        if k == 0:
            n_minus_k = n_minus_k.next
        else:
            k -= 1
    return n_minus_k.data if k == 0 else None

# tests
llist = LinkedList()
llist.insert_many([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1, 1, 9])
llist.print()
print(kthToLast2(llist, 3))
