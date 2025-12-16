""" 
Write a python program to find longest word along with index id in a list.
input = ['Happy', 'birthday', 'to', 'you']
"""

class FindLongestWord:

    def __init__(self,inp):
        self.inp = inp
        self.longest_len = 0

    def find_longest(self):

        res = ""
        for i in range(len(self.inp)):
            if len(res) < len(self.inp[i]):
                res = self.inp[i]
                self.longest_len = i
        
        return res,self.longest_len


if __name__ == "__main__":
    inp = ['Happy', 'birthday', 'to', 'you']
    cls_obj = FindLongestWord(inp)
    rexs = cls_obj.find_longest()

    print(rexs)