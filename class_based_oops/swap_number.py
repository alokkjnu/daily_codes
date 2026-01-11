"""
Write a Python porgram to swap numbers
without using third variabl.
inp : a=5,b=4

output: a=4, b=5
"""

class SwapNumbers:

    def __init__(self,a,b):

        self.a = a
        self.b = b

    def swap_numbers(self):

        a = self.a + self.b 

        b = a - self.b
        a = a - b

        return a,b
    

if __name__ == "__main__":

    a = 5
    b = 4
    cls_obj = SwapNumbers(a,b)
    res = cls_obj.swap_numbers()
    print(res)