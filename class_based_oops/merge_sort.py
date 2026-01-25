"""
Write a program to sort the list
 element using Merge sort algorithm.
input= [5,4,3,2,6,7,8,9,1]
"""

class MergeSort:

    def merge_sort(self,inp):
        
        if len(inp) <=1:
            return inp
        
        mid = len(inp) //2
        left = inp[:mid]
        right = inp[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge(left,right)
    
    @staticmethod
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

if __name__ == "__main__":

    inp = [5,4,3,2,6,7,8,9,1]
    cls_obj = MergeSort()
    res = cls_obj.merge_sort(inp)

    print(res)