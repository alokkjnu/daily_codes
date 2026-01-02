"""
Given the word:  "HelloWorld"
Divide it into two equal halves:
Hello
World
Then mix both halves in such a way that the final output becomes:
output : odlllreoHW
"""

class DivideMix:

    def __init__(self,inp):

        self.inp = inp
        self.len_inp = len(inp)

    def divide_mix(self):

        mid = self.len_inp //2

        first_str = self.inp[:mid]
        last_str = self.inp[mid:]

        first_str = self.reverse_str(first_str)
        last_str = self.reverse_str(last_str)

        res = ""

        for i in range(len(first_str)):

            res = res + first_str[i]
            res = res +last_str[i]

        return res
    
    def reverse_str(self,inp):
        res = ""

        for i in inp:
            res = i +res
        
        return res

if __name__ == "__main__":

    inp = "HelloWorld"

    cls_obj = DivideMix(inp)

    res= cls_obj.divide_mix()

    print(res)