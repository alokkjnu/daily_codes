""" 
Write a program to reverse 
string Word by Word without inbuilt.
"""

class ReverseStrByWord:

    def __init__(self,inp):

        self.inp = inp

    def reverse_str(self):

        res = ""
        st = ""

        for i in self.inp:
            if i == " ":
                res = st + " " + res
                st = ""
            else:
                st +=i

        res = st + " " + res

        return res

if __name__ == "__main__":
    inp = "Alok Kumar Maurya"
    cls_obj = ReverseStrByWord(inp)
    res = cls_obj.reverse_str()
    print(res)