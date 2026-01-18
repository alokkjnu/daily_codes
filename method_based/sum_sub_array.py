"""
Write a Python program to
find sum of all sub array.

inp = [1,2,3,4,5,6,7,8]
"""

def find_sum(inp):
    total_sum = 0
    n = len(inp)
    for i in range(n):
        subarr_sum = 0
        for j in range(i,n):
            subarr_sum+=inp[j]
            total_sum +=subarr_sum
    return total_sum

inp = [1,2,3,4,5,6,7,8]
print(find_sum(inp))