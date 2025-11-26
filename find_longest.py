""" Find longest word and index """
s = ['Happy', 'birthday', 'to', 'you']


def find_longest(s):
    res = ""
    longest_len = 0
    for i in range(len(s)):
        if len(res) < len(s[i]):
            res = s[i]
            longest_len = i
    
    return res,longest_len

print(find_longest(s))