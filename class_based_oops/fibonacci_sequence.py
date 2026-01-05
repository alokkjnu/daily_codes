"""
Write a python program for
fibonacci Sequence.
"""

class FibonacciSequenc:

    def __init__(self,inp):

        self.inp = inp

    def fibonacci_sequence(self):

        s,n = 0,1

        for _ in range(0,self.inp):
            print(s)
            nth = s+n
            s = n
            n = nth


if __name__ == "__main__":
    inp  = 10

    cls_obj = FibonacciSequenc(inp)
    res = cls_obj.fibonacci_sequence()

    print(res)