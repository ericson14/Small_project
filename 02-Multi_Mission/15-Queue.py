from multiprocessing import Process, Queue
from time import sleep
from random import random


def write(qu):
    for value in ["A", "B", "C"]:
        print("将{}放入队列".format(value))
        qu.put(value)
        sleep(random())


def read(qu):
    while True:
        if not qu.empty():
            value = qu.get(True)
            print("从队列中获得了{}".format(value))
            sleep(random())
        else:
            break


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    print("")
    print("所有数据都已经读写完毕")
