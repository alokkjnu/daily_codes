"""
Python program to find missing number in list.
input = [1,2,4,5,6]
output = 3
"""


def missing_number(lst,n):

    return n *(n+1) // 2 -sum(lst)

input = [1,2,4,5,6]
print(abs(missing_number(input,5)))