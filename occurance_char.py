"""Write a Python program to count the occurrences of each character in a string.

Input: "mississippi"
Output: {'m': 1, 'i': 4, 's': 4, 'p': 2}
"""

def occurance_count(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

s = "mississippi"
print(occurance_count(s))