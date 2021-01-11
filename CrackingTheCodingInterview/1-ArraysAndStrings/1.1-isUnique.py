# Simple
def isUnique1(string):
    seen = []
    for c in string:
        if c in seen:
            return False
        seen.append(c)
    return True

# time: O(n), space: O(1)
def isUnique2(string):
    chars = [0] * 256   # bit array
    for c in string:
        val = ord(c)
        if chars[val]:
            return False
        chars[val] = 1
    return True

# No Extra Data Structures : O(n^2)
def isUnique3(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True