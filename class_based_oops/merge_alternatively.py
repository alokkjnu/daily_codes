"""
Write a Python program to merge them alternately 
— one element from s1, then one from s2.
If one string has extra elements, append them a
t the end separated by " " (a space).

input:
s1 = "a,b,c,d"
s2 = "e,f,g,h,i,j"

output:
a,e,b,f,c,g,d,h, ,i, ,j
['a', 'e', 'b', 'f', 'c', 'g',
 'd', 'h', ' ', 'i', ' ', 'j']
"""

class MergeALternatly:

    def __init__(self,inp1,inp2):
        self.inp1 = inp1
        self.inp2 = inp2
    
    def get_merged(self):

        str1 = self.inp1.split(',')
        str2 = self.inp2.split(',')
        str_len = len(str1) - len(str2)

        if str_len > 0:

            str2.extend([" "] * str_len)
        elif str_len < 0:
            str1.extend([" "] * abs(str_len))

        res = []
        for i in range(len(str1)):
            res.append(str1[i])
            res.append(str2[i])

        return res

if __name__=="__main__":
    inp1 = "a,b,c,d"
    inp2 = "e,f,g,h,i,j"
    class_obj  = MergeALternatly(inp1,inp2)
    res = class_obj.get_merged()

    print(res)

