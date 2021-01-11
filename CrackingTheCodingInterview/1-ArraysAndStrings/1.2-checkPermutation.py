# Given two strings, write a method to decide if one is a permutation of the other.

# Initial
# time: O(nlogn), space: O(n)
def checkPermutation1(a, b):
    if len(a) != len(b):
        return False

    a_srtd = "".join(sorted(a)) # O(nlogn)
    b_srtd = "".join(sorted(b)) # O(nlogn)
    for i in range(len(a)):     # O(n)
        if a_srtd[i] != b_srtd[i]:
            return False
    return True

# Optimization
# time: O(n), space: O(n)
def checkPermutation2(a, b):
    if len(a) != len(b):
        return False

    a_hash = {}
    b_hash = {}
    for i in range(len(a)):     # O(n)
        if a[i] in a_hash:
            a_hash[a[i]] += 1
        else:
            a_hash[a[i]] = 0

        if b[i] in b_hash:
            b_hash[b[i]] += 1
        else:
            b_hash[b[i]] = 0

    return a_hash == b_hash     # O(n)
