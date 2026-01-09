"""
Write a python program to
sort element by length.

inp = [[3,1,2,6], [6], [9,3,7], [2,1,6,9,7], [9,2], [0]]
"""

class SortElementByLen:

    def __init__(self,inp):

        self.inp = inp

    def sort_element(self):

        s_len = []

        for i in range(len(self.inp)):
            s_len.append(len(self.inp[i]))

        sorted_ele = self.quick_sort(s_len)
        unique_ele = []
        for x in sorted_ele:
            if x not in unique_ele:
                unique_ele.append(x)

        res = []
        for l in unique_ele:
            for j in self.inp:
                if len(j) == l:
                    res.append(j)

        return res


    def quick_sort(self,inp):
        if len(inp) <= 1:
            return inp

        pivote = inp[len(inp) // 2]

        left = [x for x in inp if x < pivote]
        mid = [x for x in inp if x == pivote]
        right = [ x for x in inp if x > pivote]

        return self.quick_sort(left) + mid + self.quick_sort(right)


if __name__ == "__main__":
    inp = [[3,1,2,6], [6], [9,3,7], [2,1,6,9,7], [9,2], [0]]
    cls_obj = SortElementByLen(inp)
    res = cls_obj.sort_element()
    print(res) 