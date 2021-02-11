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

# Given two singly linked lists, determine if the two lists intersect. 
# Return the intersecting node. Note that the intersection is based on reference, not value. 
# That is, if the kth node of the first singly linked list is the exact same node (by reference) 
# as the jth node of the second linked list, they are intersecting.

# time: O(n + m), space: O(1)
def intersection(l1: LinkedList, l2: LinkedList):
    ptr1 = l1.head
    while ptr1:
        ptr2 = l2.head
        while ptr2:
            if ptr1 == ptr2:
                return ptr1
            ptr2 = ptr2.next
        ptr1 = ptr1.next
    return False

l1 = LinkedList()
l2 = LinkedList()
l1.insert_many([1, 2, 3, 4, 5, 6])
l2.insert_many([7, 8, 9, 10])
l2.head.next.next.next.next = l1.head.next.next
l2.print()
print(intersection(l1, l2).data)