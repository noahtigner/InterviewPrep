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

    def append(self, data):
        # O(n)

        if not self.head:
            self.head = Node(data)
        else:
            end = Node(data)
            n = self.head
            while n.next:
                n = n.next
            n.next = end

    def delete(self, data):
        # O(n)

        if not self.head:
            return

        n = self.head
        if n.data == data:
            self.head = n.next  # moved head
            return

        while n.next:
            if n.next.data == data:
                n.next = n.next.next
                return
            n = n.next

    def reverse(self):
        prev = None
        curr = self.head
        nxt = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def print(self):
        n = self.head
        while n:
            print(n.data, end=" -> ")
            n = n.next
        print("None")
