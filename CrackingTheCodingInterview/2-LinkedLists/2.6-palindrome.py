import copy

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

# Implement a function to check if a linked list is a palindrome.

# time: O(n), space: O(1)
def reverse(llist: LinkedList) -> LinkedList:
    prev = None
    curr = llist.head
    nxt = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    llist.head = prev
    return llist

# time: O(n), space: O(n)
def palindrome1(llist: LinkedList) -> bool:
    rev = reverse(copy.deepcopy(llist))
    
    length = 0
    node = llist.head
    while node:
        length += 1
        node = node.next

    curr = llist.head
    rev_curr = rev.head
    while length // 2 > 0:
        if curr.data != rev_curr.data:
            return False
        curr = curr.next
        rev_curr = rev_curr.next
        length -= 1
    return True



class Stack:
    # LIFO
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)

    def peek(self):
        return self.data[-1] if not self.is_empty() else None

    def pop(self):
        if not self.is_empty():
            item = self.data[-1]
            del self.data[-1]
            return item
        return None

# time: O(n), space: O(n)
def palindrome2(llist: LinkedList) -> bool:
    slow = fast = llist.head
    stack = Stack()
    
    while fast and fast.next:
        stack.push(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast:    # if odd # elements, skip to middle
        slow = slow.next

    while slow:
        if slow.data != stack.pop():
            return False
        slow = slow.next
    
    return True

# tests
llist = LinkedList()
llist.insert_many([1, 2, 10, 5, 10, 2, 1])
print(palindrome2(llist))