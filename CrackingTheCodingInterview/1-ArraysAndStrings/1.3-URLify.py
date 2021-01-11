# Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficientspace at the end to hold the additional characters,
# and that you are given the "true" length.

# Input: "Mr John Smith   ", 13
# Output: "Mr%20John%20Smith"

# Simple
# time: O(n), space: O(n)
def URLify1(string, length):
    out = ""
    for c in string:
        if c == ' ' and length:
            out += '%20'
            length -= 1
        elif(length):
            out += c
            length -= 1
    return out
