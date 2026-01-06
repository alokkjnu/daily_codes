""" 
Write a program to reverse 
string char by char
"""

class RerverseStringByChar:

    def __init__(self,inp):

        self.inp = inp 

    def reverse_str(self):

        s = ""

        for i in self.inp:

            s = i+s
        
        return s

if __name__ == "__main__":

    inp = "HelloWorld"
    cls_obj = RerverseStringByChar(inp)
    res = cls_obj.reverse_str()
    print(res)