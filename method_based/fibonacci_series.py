"""
Write a python program for
fibonacci Sequence.

"""

def fibonacci_series(inp):

    s,n = 0,1

    for _ in range(0,inp):
        print(s)
        nth = s+n
        s = n
        n = nth


fibonacci_series(10)