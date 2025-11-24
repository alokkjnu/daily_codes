import threading
import time


def square(n):
    print(n*n)


def cube(n):
    print(n*n*n)



t1 = threading.Thread(target = square,args=(5,))
t2 = threading.Thread(target = cube,args=(4,))
t1.start()
t2.start()

time.sleep(10)

t1.join()
t2.join()

