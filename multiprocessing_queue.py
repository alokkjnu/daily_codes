
"""
Write a python program for multiprocessing,
aong with multiprocessing queue,
"""

import multiprocessing
import time

def square(n,q):

    return q.put(n**2)

def cube(n,q):

    return q.put(n**3)
q = multiprocessing.Queue()
m1 = multiprocessing.Process(target=square, args=(5,q))

m2 = multiprocessing.Process(target=cube, args=(4,q))

m1.start()
time.sleep(2)
m2.start()
print(q.get())
print(q.get())



m1.join()
m2.join()