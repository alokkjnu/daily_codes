"""
5
3,2
 Write a program to divide a number into two parts such that the first part is greater than the second part by 1.
 """

def test(s):
    mid = s//2
    first_value = mid
    second_value = mid+1
    return first_value,second_value

print(test(6))