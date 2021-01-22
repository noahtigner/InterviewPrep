class Queue:
    # FIFO
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
