"""
Write a pythonn program to find
all palindromic substring.

inp ="ababacbcbcbcdgdadgdg"
"""

class PalindromicSubstring:

    def __init__(self,inp):

        self.inp = inp

    def is_palindrome(self,inp):

        return inp == inp[::-1]
    
    def palindromic_substr(self):

        n = len(self.inp)
        palindromes = set()
        for i in range(n):
            for j in range(i+1,n+1):
                substring = self.inp[i:j]
                if self.is_palindrome(substring):
                    palindromes.add(substring)

        return palindromes
    

if __name__ =="__main__":

    inp = "ababacbcbcbcdgdadgdg"

    cls_obj = PalindromicSubstring(inp)
    res = cls_obj.palindromic_substr()
    print(res)