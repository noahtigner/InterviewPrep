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
