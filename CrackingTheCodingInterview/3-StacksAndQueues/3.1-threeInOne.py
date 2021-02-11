# Describe how you could use a single array to implement three stacks

# partition the array into 3 parts of equal (fixed) size
# do not allow data to be pushed if the partition is at capacity
class MultiStack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.array = [None] * (stack_size * 3)
        self.tops = [0, 0, 0]

    def push(self, stack, data):
        if self.tops[stack] >= self.stack_size:
            print("Error: stack at capacity")
        else:
            self.array[(self.stack_size * stack) + self.tops[stack]] = data
            self.tops[stack] += 1

    def pop(self, stack):
        if self.tops[stack] <= 0:
            return None
        data = self.array[(self.stack_size * stack) + self.tops[stack] - 1]
        self.tops[stack] -= 1
        return data

    def peek(self, stack):
        if self.tops[stack] <= 0:
            return None
        return self.array[(self.stack_size * stack) + self.tops[stack] - 1]

    def is_empty(self, stack):
        return self.tops[stack] <= 0

s = MultiStack(3)
s.push(0, 1)
s.push(0, 2)
s.push(0, 3)
print(s.array)
s.push(1, 4)
s.push(1, 5)
s.push(1, 6)
s.push(1, 7)
s.push(1, 8)
s.push(1, 9)
print(s.array)
s.push(2, 10)
s.push(2, 11)
s.push(2, 12)
print(s.array)

print(s.pop(0))
print(s.pop(0))
print(s.pop(0))
print(s.pop(0))
print(s.pop(0))

print(s.pop(1))
print(s.pop(1))
print(s.pop(1))
print(s.pop(1))
print(s.pop(1))

print(s.pop(2))
print(s.pop(2))
print(s.pop(2))
print(s.pop(2))
print(s.pop(2))