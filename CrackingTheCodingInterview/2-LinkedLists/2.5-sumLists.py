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

# time: O(n), space: O(1)
def sumList(llist: LinkedList, reverse: bool = True):
    s = 0
    node = llist.head

    if reverse:
        multiplier = 1
        while node:
            s += (node.data * multiplier)
            multiplier *= 10
            node = node.next
    else:
        multiplier = 10
        while node:
            s = (s * multiplier) + node.data
            node = node.next
    return s

# time: O(n + m), space: O(n + m)
def sumLists(l1: LinkedList, l2: LinkedList, reverse: bool = True):
    s = sumList(l1, reverse) + sumList(l2, reverse)
    print(s)
    sum_list = LinkedList()

    if reverse:
        tail = Node(s % 10)
        sum_list.head = tail
  
        while (s >= 10):
            s //= 10
            tail.next = Node(s % 10)
            tail = tail.next
    else:
        while (s > 0):
            sum_list.insert(s % 10)
            s //= 10

    return sum_list

# tests
l1 = LinkedList()
l2 = LinkedList()
l1.insert_many([6, 1, 7])
l2.insert_many([2, 9, 5])
sum_list = sumLists(l1, l2, reverse=True)
sum_list.print()
