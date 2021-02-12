# Implement a MyQueue class which implements a queue using two stacks.

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

    def is_empty(self):
        return not self.top

class MyQueue:
    def __init__(self):
        self.stacks = [Stack(), Stack()]    # keep left empty for pushing, keep right full for popping

    def enqueue(self, data):
        while not self.stacks[1].is_empty():
            self.stacks[0].push(self.stacks[1].pop())
        self.stacks[0].push(data)
        while not self.stacks[0].is_empty():
            self.stacks[1].push(self.stacks[0].pop())

    def dequeue(self):
        if self.stacks[1]:
            return self.stacks[1].pop()
        return None

    def is_empty(self):
        return not self.stacks[1]

q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())