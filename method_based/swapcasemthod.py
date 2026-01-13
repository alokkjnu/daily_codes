"""
Python program for swapcase using decorator.
"""


def swapcase_deco(inp):
    def wrapper(inp):

        return inp.swapcase()
    
    return wrapper


@swapcase_deco
def swapcase_str(inp):
    return inp

print(swapcase_str("Hello World"))