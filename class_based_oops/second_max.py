"""
Write a Python program to get 
second max element from array.
input = [2,4,5,6,3,2,2,4,5,7,
            8,9,0,32,55,34,55,44]
output = 44
"""
class SecondMax:

    def __init__(self,inp):

        self.inp = inp

    def get_second_max(self):

        unique_ele = []
        for i in self.inp:
            if i not in unique_ele:
                unique_ele.append(i)

        sorted_ele = self.quick_sort(unique_ele)
        max_ele = self.get_max(sorted_ele)
        new_ele = sorted_ele.remove(max_ele)
        second_max = self.get_max(sorted_ele)

        return second_max

    def get_max(self,sorted_ele):

        max_ele = 0

        for i in sorted_ele:
            if max_ele < i:
                max_ele = i
        return   max_ele

    
    def quick_sort(self,unique_ele):

        if len(unique_ele) <= 1:
            return unique_ele

        pivote = unique_ele[ len(unique_ele) //2]

        left = [x for x in unique_ele if x < pivote]
        mid = [ x for x in unique_ele if x == pivote]
        right = [ x for x in unique_ele if x > pivote]

        return self.quick_sort(left) + mid + self.quick_sort(right)


if __name__ == "__main__":
    inp =[2,4,5,6,3,2,2,4,5,7,
            8,9,0,32,55,34,55,44]

    cls_obj = SecondMax(inp)
    res = cls_obj.get_second_max()

    print(res)