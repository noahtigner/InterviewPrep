# Given a string, write a function to check if its a permutation of a palindrome.
# A palindrom is a word or phrase that is the same forwards as backwards.
# A permutation is a rearrangement of letters.
# The palindrom does not need to be limited to just dictionary words.
# You can ignore casing and non-letter characters

# We know:
# - must have even number of all characters,
# - except for (possibly) one
# - ignore whitespace & special characters

# Simple
# time: O(n), space: O(n)
def palindromPermutations1(string):
    counts = {}
    for c in string:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    odds = 0
    for key in counts:
        if key != ' ' and counts[key] % 2 == 1:
            odds += 1
    return odds <= 1

# Space Optimization
# time: O(n), space: O(1)
def palindromPermutation2(string):
    counts = [0 for c in range(26)]
    print(counts)
    for c in string:
        lower = ord(c.lower()) - 97
        if lower >= 0 and lower <= 25:
            counts[lower] += 1

    odds = 0
    for c in range(26):
        if counts[c] % 2 == 1:
            odds += 1

    return odds <= 1
