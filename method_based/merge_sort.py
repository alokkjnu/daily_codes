"""
Write a program to sort the list
 element using Merge sort algorithm.
input= [5,4,3,2,6,7,8,9,1]
"""

def  merge_sort(inp):
    if len(inp) <= 1:
        return inp
    
    mid = len(inp) // 2
    left_h  = inp[:mid]
    right_h = inp[mid:]
    left_h = merge_sort(left_h)
    right_h = merge_sort(right_h)

    return merge(left_h,right_h)

def merge(left,right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1
    while i < len(left):
        sorted_list.append(left[i])
        i+=1
    while j < len(right):
        sorted_list.append(right[j])
        j +=1

    return sorted_list


input= [5,4,3,2,6,7,8,9,1]
print(merge_sort(input))