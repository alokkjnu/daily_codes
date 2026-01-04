"""write a program to remove duplicate from 
list without using set or inbuit method

input:[1,2,3,4,5,4,2,2,1,5,4,65,6,7,8,9,
0,0,8,8,7,6,5,5,4,4,43,4,5,6,7,8,8,1,8,9]
output: [1, 2, 3, 4, 5, 65, 6, 7, 8, 9, 0, 43]
"""
num  = [1,2,3,4,5,4,2,2,1,5,4,65,6,7,8,9,0,0,
        8,8,7,6,5,5,4,4,43,4,5,6,7,8,8,1,8,9]

def remove_duplicate_num(num):
    res = []

    for i in num:
        if i not in res:
            res.append(i)
    return res


print(remove_duplicate_num(num))