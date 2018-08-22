from time import sleep
from threading import Thread


class MyThread(Thread):
    def __init__(self, num):
        super(MyThread, self).__init__()
        self.num = num

    def my_thread(self):
        for i in range(self.num):
            sleep(1)
            msg = "I'm " + self.name + " @ " + str(i)
            print("\n", msg)

    def run(self):
        self.my_thread()


if __name__ == '__main__':
    for j in range(5):
        t = MyThread(3)
        t.start()
    print("主程序执行完毕")
