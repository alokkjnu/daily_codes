"""
Python Program to find longest
substring in given string.
"""

def longest_substring(inp):

    longest = ""
    current = ""
    for char in inp:
        if char not in current:
            current += char
        else:
            current = current[current.index
                              (char)+1:]+char
        if len(current) > len(longest):
            longest = current

    return longest 


print(longest_substring("fgasgdfjklahdflkhed"))