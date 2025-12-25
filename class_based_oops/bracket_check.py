"""
Write a Python program to check if the 
brackets in a given string are balanced.
Input : "{([])}{}{()"
output : True/False 
"""

class BracketCheck:

    def __init__(self,inp):

        self.inp = inp

    def bracket_check(self):

        while True:

            inp = self.inp.replace("()","").replace("{}","").replace("[]","")

            if self.inp == inp:
                break

            self.inp = inp

        return (self.inp=="")

if __name__ == "__main__":

    inp = "{([])}{}{()"
    cls_obj = BracketCheck(inp)
    res = cls_obj.bracket_check()

    print(res)