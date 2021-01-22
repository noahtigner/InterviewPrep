# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring

# (e.g., "waterbottle" is a rotation of "erbottlewat")

# time: O(mn), space: O(1)
def isSubstring(s1, s2):
    window = len(s1)

    for i in range(len(s2) - window + 1):
        for j in range(window):
            if s1[j] != s2[i+j]:
                break
        if j == window - 1:
            return True
    return False

# Simple
# time: O(mn), space: O(m^2)
def stringRotation1(s1, s2):
    if len(s1) != len(s2):
        return False

    rotations = ""
    for i in range(len(s1)):
        rotation = ""
        for j in range(len(s1)):
            rotation += s1[(i + j) % len(s1)]
        rotations += rotation
    return isSubstring(s2, rotations)

# Simplified (I was being dumb about space)
# time: O(mn), space: O(m)
def stringRotation2(s1, s2):
    if len(s1) != len(s2):
        return False

    rotations = s1 + s1
    return isSubstring(s2, rotations)

print(stringRotation2("waterbottle", "erbottlewat"))