"""Write a Python program to merge them alternately — one element from s1, then one from s2.
If one string has extra elements, append them at the end separated by " " (a space).

input:

s1 = "a,b,c,d"
s2 = "e,f,g,h,i,j"

output:
a,e,b,f,c,g,d,h, ,i, ,j

['a', 'e', 'b', 'f', 'c', 'g', 'd', 'h', ' ', 'i', ' ', 'j']

"""


def merge_alternately(str1, str2):
    s1 = str1.split(',')
    s2 = str2.split(',')
    s_len = len(s1) - len(s2)
    if s_len > 0:
        s2.extend([" "] * s_len)
    elif s_len < 0:
        s1.extend([" "] * abs(s_len))
    res = []
    for i in range(len(s1)):
        res.append(s1[i])
        res.append(s2[i])
    return res # or use ','.join(res) to return as a string

s1 = "a,b,c,d"
s2 = "e,f,g,h,i,j"

print(merge_alternately(s1, s2))