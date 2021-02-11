# FIFIO
# enque, dequeue, peek, is_empty

# Array(list) - based implementation
class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def head(self):
        return self.data[0] if not self.is_empty() else None

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if not self.is_empty():
            item = self.data[0]
            del self.data[0]
            return item
        return None

# LinkedList - based implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        node = Node(data)
        if not self.first:
            self.first = node
        if self.last:
            self.last.next = node
        self.last = node

    def dequeue(self):
        if self.first:
            node = self.first
            self.first = self.first.next
            return node.data
        return None

    def peek(self):
        if self.first:
            return self.first.data
        else:
            return None
