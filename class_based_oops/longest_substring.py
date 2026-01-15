"""
Python Program to find longest
substring in given string.
"""

class FindLongestSubstring:

    def __init__(self,inp):

        self.inp = inp

    def longest_substring(self):

        longest = ""
        current = ""

        for char in self.inp:
            if char not in current:
                current +=char
            else:
                current = current[current.index(char)+1:]+char

            if len(current) > len(longest):
                longest = current
        return longest
    
if __name__ == "__main__":

    inp = "dsfakeflhekolwharflkear"
    clas_obj = FindLongestSubstring(inp)
    res = clas_obj.longest_substring()
    print(res)