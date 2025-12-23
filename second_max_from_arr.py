"""
Write a Python program to get 
second max element from array.
input = [2,4,5,6,3,2,2,4,5,7,
            8,9,0,32,55,34,55,44]
"""

def get_second_max(inp):

    unique_ele = []

    for i in inp:
        if i not in unique_ele:
            unique_ele.append(i)
    sorted_ele = quck_sort(unique_ele)

    max_ele = get_max(sorted_ele)
    new_ele = sorted_ele.remove(max_ele)
    second_max = get_max(sorted_ele)

    return second_max


def get_max(inp):
    max_ele = 0
    for i in inp:
        if max_ele < i:
            max_ele = i
    return max_ele


def quck_sort(inp):

    if len(inp) <= 1:
        return inp

    pivote = inp[len(inp) // 2]
    left = [x for x in inp if x < pivote]
    mid = [x for x in inp if x == pivote]
    right = [x for x in inp if x > pivote]

    return quck_sort(left) + mid + quck_sort(right)


inp = [2,4,5,6,3,2,2,4,5,7,8,9,0,32,55,34,55,44]
print(get_second_max(inp))