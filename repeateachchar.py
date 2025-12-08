# Given a string where each letter is followed by a number (example: "a2b3c4"), write a Python program to repeat each letter according to its number.
# Input:  a2b3c4

# Output: aabbbcccc

def repeate_letter(inp):
    res = ""
    ele = ""

    for i in inp:

        if i.isnumeric():
            ele = str(ele)*int(i)
            res = res+ele
            ele = ""
            
        else:
            ele = i
    return res

print(repeate_letter("a2b3c4"))