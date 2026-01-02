""" 
write a decorator to remove duplicate and sort the array.
input: [1,2,3,4,5,4,2,2,1,5,4,65,6,7,8,9,0,0,8,8,7,6,5,5,4,4,43]
output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 43, 65]
"""

def remove_duplicate(func):
    def wrapper(arr):
        res = func(arr)
        unique = []

        for i in res:
            if i not in unique:
                unique.append(i)

        return unique

    return wrapper

#method to sort the array

def sort_arr(func):
    def wrapper(arr):
        res = func(arr)

        def quick_sort(res):
            if len(res) <=1:
                return res
            pivote = res[len(res) // 2]
            left = [x for x in res if x < pivote]
            mid = [x for x in res if x == pivote]
            right = [x for x in res if x > pivote]

            return quick_sort(left) + mid + quick_sort(right)

        return quick_sort(res)

    return wrapper

@remove_duplicate
@sort_arr
def main_method(inp):
    return inp


inp = [1,2,3,4,5,4,2,2,1,5,4,65,6,7,8,9,0,0,8,8,7,6,5,5,4,4,43]
print(main_method(inp))