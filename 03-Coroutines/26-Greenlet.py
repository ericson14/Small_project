from greenlet import greenlet
import time


def foo1():
    for i in range(5):
        print("---A---")
        gr2.switch()
        time.sleep(0.5)


def foo2():
    for i in range(5):
        print("---B---")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(foo1)
gr2 = greenlet(foo2)
gr1.switch()
