# How would you design a stack which, in addition to push and pop,
# has a function min which returns the minimum element?
# Push, pop, and min should take O(1) time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.min = None # keep track of the minimum of the stack, up to this point

class MinStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if not self.top:
            self.top = node
            node.min = data
        else:
            node.next = self.top
            self.top = node
            node.min = min([node.next.min, data])

    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            return data
        
        return None

    def min(self):
        if self.top:
            return self.top.min
        return None

ms = MinStack()
ms.push(2)
ms.push(99)
ms.push(3)
ms.push(4)
ms.push(1)

print(ms.min())
ms.pop()
print(ms.min())
ms.pop()
print(ms.min())
ms.pop()
print(ms.min())
ms.pop()
print(ms.min())
ms.pop()
print(ms.min())
