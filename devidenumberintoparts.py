"""
Write a program to divide a number into two parts such that,
the first part is greater than the second part by 1.
input: 5
output: 3,2
"""


class DivideTwo:

    def __init__(self,inp):

        self.inp = inp

    def divide_into_two(self):

        mid = self.inp //2
        left = mid
        right = mid + 1

        return left,right


if __name__ == "__main__":

    class_obj = DivideTwo(9)
    res = class_obj.divide_into_two()

    print(res)