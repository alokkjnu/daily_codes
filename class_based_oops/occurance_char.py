"""
Write a Python program to count the
 occurrences of each character in a string.

Input: "mississippi"
Output: {'m': 1, 'i': 4, 's': 4, 'p': 2}
"""

class CharOccurance:

    def __init__(self,inp):

        self.inp = inp
    
    def count_char(self):

        d = {}

        for i in self.inp:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        
        return d

if __name__ == "__main__":

    inp = "missisippi"
    cls_ob = CharOccurance(inp)
    res = cls_ob.count_char()

    print(res)