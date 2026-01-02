"""
Write a multiprocessing sample program using Python.
"""

import multiprocessing
import time

def square(n):

    print(n**2)

def cube(n):

    print(n**3)

m1 = multiprocessing.Process(target=square, args=(5,))

m2 = multiprocessing.Process(target=cube, args=(4,))

m1.start()
time.sleep(2)
m2.start()



m1.join()
m2.join()