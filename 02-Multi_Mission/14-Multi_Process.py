import multiprocessing
from time import sleep
import os


def other_prod(num):
    for j in range(num):
        print("执行了{}次".format(j+1))
        print(os.getpid(), os.getppid())
        os.kill(os.getpid(), 9)


def run_prod(name, age, **kwargs):
    print(multiprocessing.current_process().pid)
    for i in range(10):
        print("子进程运行中，名字={}，年龄={}，进程ID={}。。。".format(name, age, os.getpid()))
        print(kwargs)
        sleep(0.1)


if __name__ == '__main__':
    print(multiprocessing.current_process())
    p1 = multiprocessing.Process(target=run_prod, args=("李四", 16), kwargs={"m": 20})
    p2 = multiprocessing.Process(target=other_prod, name="测试用", args=(3, ))
    p1.start()
    p2.start()
    print(multiprocessing.active_children())
    sleep(0.5)
    p1.terminate()
    p1.join()
