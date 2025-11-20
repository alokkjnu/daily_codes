#Sort by element length
d = [[3,1,2,6], [6], [9,3,7], [2,1,6,9,7], [9,2], [0]]


def test(d):
    len_d = []

    for i in range(len(d)):
        len_d.append(len(d[i]))
    sorted_len_d = quick_sort(len_d)
    unique = []
    for x in sorted_len_d:
        if x not in unique:
            unique.append(x)
    res = []
    for l in unique:
        for j in d:
            if len(j) == l:
                res.append(j)

    return res
        

def quick_sort(n):
    if len(n)<=1:
        return n

    pivote = n[len(n)//2]
    left = [i for i in n if i < pivote]
    mid = [i for i in n if i == pivote]
    right = [i for i in n if i > pivote]

    return quick_sort(left)+mid+quick_sort(right)

print(test(d))
# def sort_ele(d):
#     res = []
#     mid = len(d) // 2
#     left_side = []
#     right_side = []
#     for i in range(len(d)):
#         print((d[mid]))
#         if len(d[i]) < len(d[mid]):
#             left_side.append(d[i])
#         else:
#             right_side.append(d[i])
#     return sort_ele(left_side + d[mid] +right_side)
#     # print(left_side + d[mid] +right_side)

# print(sort_ele(d))