"""
write a program to remove duplicates
from string without using set or inbuit method

input:"edfasjkbfkeaskfdnkbsafkjbdsf"
output: ""
"""

class RemoveDuplicateChar:

    def __init__(self,inp):

        self.inp = inp

    def remove_duplicate(self):

        res = []

        for i in self.inp:
            if i not in res:
                res.append(i)

        return ''.join(res)


if __name__=="__main__":

    inp = "edfasjkbfkeaskfdnkbsafkjbdsf"

    cls_obj = RemoveDuplicateChar(inp)
    res = cls_obj.remove_duplicate()
    print(res)