"""
Write a Python program to
find sum of all sub array.

inp = [1,2,3,4,5,6,7,8]
"""

class FindSubArrSum:

    def __init__(self,inp):

        self.inp = inp
        self.inp_len = len(inp)

    def find_sum(self):

        total_sum = 0

        for i in range(self.inp_len):
            sub_arr_sum = 0
            for j in range(i,self.inp_len):
                sub_arr_sum += self.inp[j]
                total_sum += sub_arr_sum
        return total_sum
    
if __name__ == "__main__":

    inp = [1,2,3,4,5,6,7,8]
    cls_ob = FindSubArrSum(inp)
    res = cls_ob.find_sum()
    print(res)