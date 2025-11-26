import multiprocessing
import time

def square(n):
    print(n*n)

def cube(n):
    print(n*n*n)

m1 = multiprocessing.Process(target=square, args=(5,))
m2 = multiprocessing.Process(target=cube, args=(4,))

m1.start()
m2.start()

time.sleep(10)

m1.join()
m2.join()