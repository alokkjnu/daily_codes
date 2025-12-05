""" 
write a decorator to remove duplicate and sort the array.
input: [1,2,3,4,5,4,2,2,1,5,4,65,6,7,8,9,0,0,8,8,7,6,5,5,4,4,43]

output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 43, 65]
"""

inp = [1,2,3,4,5,4,2,2,1,5,4,65,6,7,8,9,0,0,8,8,7,6,5,5,4,4,43]

def remove_duplicate(func):
    def wrapper(arr):
        res = func(arr)
        uniq = []
        for i in res:
            if i not in uniq:
                uniq.append(i)
        return uniq
    return wrapper

def sort_num(func):
    def wrapper(arr):
        res = func(arr)
        def quicksort(lst):
            if len(lst) <= 1:
                return lst
            pivot = lst[len(lst)//2]
            left = [x for x in lst if x < pivot]
            mid = [x for x in lst if x == pivot]
            right = [x for x in lst if x > pivot]
            return quicksort(left) + mid + quicksort(right)

        return quicksort(res)
    return wrapper

@remove_duplicate
@sort_num
def main(num):
    return num

print(main(inp))
