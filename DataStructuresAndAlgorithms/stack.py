# LIFO
# push, pop, peek, is_empty

# Array(list) - based implementation
class Stack:
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

# LinkedList - based implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        if self.top:
            node = self.top
            self.top = self.top.next
            return  node.data
        return None

    def peek(self):
        if self.top:
            print(self.top.data)

    def is_empty(self):
        return not self.top
