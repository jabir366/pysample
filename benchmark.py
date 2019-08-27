#!/usr/bin/python3

def cube(x):
    return x*x*x

g = lambda x: x*x*x

#if __name__ == "__main__":
#    import timeit
#    setup = "from __main__ import cube"
#    print (timeit.timeit("cube(200)", setup=setup))
#    setup = "from __main__ import g"
#    print (timeit.timeit("g(200)", setup=setup))
import random
import time

class MyTimer():

    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        runtime = end - self.start
        msg = 'The function took {time} seconds to complete'
        print(msg.format(time=runtime))


def long_runner():
    for x in range(5):
        sleep_time = random.choice(range(1,5))
        time.sleep(sleep_time)

def test1():
    for i in range(1,100):
       _= cube(i)

def test2():
    for i in range(1,100):
       _= g(i)

if __name__ == '__main__':

    with MyTimer():
        print("helloo")

    with MyTimer():
        mydict ={'name':[i for i in range(100)]}

    with MyTimer():
        mydict ={'name':[i for i in range(1000)]}
    with MyTimer():
        test2()

