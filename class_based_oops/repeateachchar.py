"""
Given a string where each letter is
followed by a number (example: "a2b3c4"), 
write a Python program to repeat 
each letter according to its number.

Input:  a2b3c4
Output: aabbbcccc
"""

class RepeatEachChar:

    def __init__(self,inp):

        self.inp = inp

    def repeat_char(self):

        if len(self.inp) <= 1:
            return self.inp

        res = ""
        ele = ""

        for i in self.inp:
            if i.isnumeric():
                ele = str(ele)*int(i)
                res = res+ele
                ele = ""
            else:
                ele = i

        return res

if __name__ == "__main__":
    inp = "a2b3c4"
    cls_obj = RepeatEachChar(inp)
    res = cls_obj.repeat_char()
    print(res)