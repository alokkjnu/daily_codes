"""write a program to remove duplicate
from string without using set or inbuit method

input:"edfasjkbfkeaskfdnkbsafkjbdsf"
output: "edfasjkbn"
"""

input="edfasjkbfkeaskfdnkbsafkjbdsf"


def remove_duplicate_str(s):
    res = []

    for i in s:
        if i not in res:
            res.append(i)

    res = ''.join(res)
    return res

print(remove_duplicate_str(input))
