# If a stack of plates gets too high, start a new stack. 
# Implement SetOfStacks, composed of several stacks, that creates a new stack when the previous one is at capacity.
# Push and pop should behave identically to a normal stack.

# Follow Up: perform a pop operation on a specific sub-stack.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, capacity):
        self.top = None
        self.capacity = capacity

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node
        self.capacity -= 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            self.capacity += 1
            return data
        return None

class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, data):
        if self.stacks and self.stacks[-1].capacity > 0:
            self.stacks[-1].push(data)
        else:
            s = Stack(self.capacity)
            s.push(data)
            self.stacks.append(s)

    def pop(self):
        if self.stacks:
            data = self.stacks[-1].pop()
            if self.stacks[-1].capacity == self.capacity:
                del self.stacks[-1]
            return data
        return None

    # This implementation allows for any stack to be non-empty to save time
    def pop_at(self, index):
        if index < len(self.stacks):
            return self.stacks[index].pop()
        return None

sos = SetOfStacks(3)
sos.push(1)
sos.push(2)
sos.push(3)
sos.push(4)
sos.push(5)
sos.push(6)
sos.push(7)

print(len(sos.stacks))
sos.pop()
print(len(sos.stacks))
print(sos.pop_at(1))
