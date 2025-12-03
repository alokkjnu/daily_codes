""" 
Write a python program to find longest word along with index in a list.

"""


def find_longest(s):

    res = ""
    longest_len = 0

    for i in range(len(s)):

        if len(res) < len(s[i]):
            res = s[i]
            longest_len = i
    
    return res,longest_len

s = ['Happy', 'birthday', 'to', 'you']

print(find_longest(s))