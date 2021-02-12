# Write a program to sort a stack such that the smallest items are on top.
# You can use an additional temporary stack, but you may not copy the elements in any other data strucuture.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            return data
        return None

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return not self.top

# time: O(n^2), space: O(n)
def sortStack(s1: Stack):
    s2 = Stack()
    while not s1.is_empty():
        tmp = s1.pop()
        while not s2.is_empty() and s2.peek() > tmp:
            s1.push(s2.pop())
        s2.push(tmp)
    while not s2.is_empty():
        s1.push(s2.pop())



s = Stack()
s.push(4)
s.push(1)
s.push(2)
s.push(3)
s.push(5)

sortStack(s)

n = s.top
for _ in range(5):
    print(n.data)
    n = n.next
