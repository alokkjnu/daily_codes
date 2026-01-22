"""
Write a Python program to find and return 
the first non-repeating character in a given string.
The program should:

Traverse the string character by character.

Check that the current character does not
appear in any previous or subsequent part of the string.

Return the first character that occurs only once.
inp1 = swiss
inp2 = statistics
inp3 = collector
"""

inp = "statistics"
def test(inp):
    for i in range(len(inp)):
        previous_char = inp[:i]
        new_char = inp[i+1:]
        if inp[i] not in new_char and inp[i] not in previous_char:
            return inp[i]

print(test(inp))
    

