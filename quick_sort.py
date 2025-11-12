
def quick_sort(n):
    if len(n)<=1:
        return n

    pivote = n[len(n)//2]
    left = [i for i in n if i < pivote]
    mid = [i for i in n if i == pivote]
    right = [i for i in n if i > pivote]

    return quick_sort(left)+mid+quick_sort(right)


print(quick_sort([5,4,3,2,6,7,8,9,1]))