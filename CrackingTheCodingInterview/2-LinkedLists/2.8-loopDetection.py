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
def loopDetection(llist: LinkedList):
    slow = llist.head
    fast = llist.head

    # detect loop, stop at meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    # no loop found
    if not fast or not fast.next:
        return False

    # restart slow, keep fast at meeting point
    # each are k steps from loop start
    # if they move at the same pace, they must meet at loop start
    slow = llist.head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast

llist = LinkedList()
llist.insert_many(['E', 'D', 'C', 'B', 'A'])
llist.head.next.next.next.next.next = llist.head.next.next
print(loopDetection(llist).data)
