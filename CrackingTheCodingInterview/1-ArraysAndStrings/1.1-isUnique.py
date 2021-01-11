# Simple
# time: O(n), space: O(n)
def isUnique1(string):
    seen = []
    for c in string:
        if c in seen:
            return False
        seen.append(c)
    return True

# Alternative
# time: O(nlogn), space: O(n)
def isUnique2(string):              # O(nlogn + n) -> O(nlogn)
    srt = "".join(sorted(string))   # O(nlogn)
    prev = srt[0]
    for i in range(1, len(srt)):    # O(n)
        if srt[i] == prev:
            return False
        prev = srt[i]
    return True

# Optimized
# time: O(n), space: O(1)
def isUnique3(string):
    chars = [0] * 256   # bit array
    for c in string:
        val = ord(c)    # char -> int
        if chars[val]:
            return False
        chars[val] = 1
    return True

# No Extra Data Structures
# time: O(n^2), space: O(1)
def isUnique4(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True

print(isUnique2("abc"))