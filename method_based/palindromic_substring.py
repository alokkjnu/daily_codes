"""
Write a pythonn program to find
all palindromic substring.

inp ="ababacbcbcbcdgdadgdg"
"""

def is_palindrome(inp):

    return inp == inp[::-1]

def find_substring(inp):

    n = len(inp)

    palindromes = set()
    for i in range(n):
        for j in range(i+1,n+1):
            substring = inp[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return sorted(palindromes)



print(find_substring("ababacbcbcbcdgdadgdg"))