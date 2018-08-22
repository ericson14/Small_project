from threading import Lock, Thread, enumerate
from time import sleep

g_num = 0


def tes1(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("----Test1----g_num={}".format(g_num))


def tes2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("----Test2----g_num={}".format(g_num))


mutex = Lock()
p1 = Thread(target=tes1, args=(1000000,))
p1.start()
p2 = Thread(target=tes2, args=(1000000,))
p2.start()

while len(enumerate()) != 1:
    sleep(1)

print("2个线程对同一个变量计算的结果是：{}".format(g_num))
