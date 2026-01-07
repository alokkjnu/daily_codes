"""
Python program for swapcase using decorator.
"""

class SwapCase:

    def __init__(self,inp):

        self.inp = inp 

    
    def swap_deco(func):

        def wrapper(self):

            return func(self).swapcase()

        return wrapper

    @swap_deco
    def swapcase_str(self):

        return self.inp


if __name__ == "__main__":

    inp = "Hello World"
    cls_obj = SwapCase(inp)
    res = cls_obj.swapcase_str()

    print(res)