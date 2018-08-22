from time import sleep


def work1():
    for i in range(5):
        print("work")
        yield
        sleep(0.2)


def work2():
    for j in range(5):
        print("work2")
        yield
        sleep(0.2)


if __name__ == '__main__':
    w1 = work1()
    w2 = work2()
    for k in range(5):
        next(w1)
        next(w2)
