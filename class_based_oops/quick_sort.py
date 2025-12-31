"""
Write a program to sort the list
 element using quick sort algorithm.
input= [5,4,3,2,6,7,8,9,1]
"""

class QuickSort:

    def quick_sort(self,inp):

        if len(inp) <=1:
            return inp

        pivote = inp[len(inp)//2]
        left = [x for x in inp if x < pivote]
        mid = [x for x in inp if x == pivote]
        right = [x for x in inp if x > pivote]

        return self.quick_sort(left) + mid + self.quick_sort(right)


if __name__ == "__main__":

    input= [5,4,3,2,6,7,8,9,1]
    cls_ob = QuickSort()
    res = cls_ob.quick_sort(input)
    print(res)