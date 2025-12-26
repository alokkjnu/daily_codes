"""
Write a Python program to demonstrate,
 shallow copy and deep copy
 a = [[1, 2], [3, 4]]
 1. b = copy.copy(a) Shallow Copy
 2. c = copy.deepcopy(a) Deep Copy
"""

import copy

class ShallowDeepCopy:

    def __init__(self,inp1,inp2):

        self.inp1 = inp1
        self.inp2 = inp2

    def shallow_Copy(self):

        b = copy.copy(self.inp1)
        b[0][0] = self.inp2

        res = {
            "original":self.inp1,
            "copied" : b
        }

        return res

    def deep_copy(self):
        b = copy.deepcopy(self.inp1)
        b[0][1] = self.inp2

        res = {
            "original":self.inp1,
            "copied": b
        }

        return res


if __name__ == "__main__":

    inp1 =[[1, 2], [3, 4]]
    inp2 = 600

    cls_obj = ShallowDeepCopy(inp1,inp2)
    res = cls_obj.shallow_Copy()
    res2 = cls_obj.deep_copy()

    print("\n Shallow Copy\t",res)
    print("\n Deep Copy ]\t", res2)