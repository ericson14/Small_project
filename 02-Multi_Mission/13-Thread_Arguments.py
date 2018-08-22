from time import sleep
import threading


def sing(num):
    print(threading.current_thread())
    for i in range(num):
        print("唱歌ing", i+1)
        sleep(0.1)


def dance(name, age, address):
    print(threading.current_thread())
    print(name, age, address)


if __name__ == '__main__':
    print("活动线程列表")
    print(threading.enumerate())
    print("\n当前线程", threading.current_thread())
    print("活动线程", threading.active_count())
    t1 = threading.Thread(target=sing, name="Sing", args=(3,))
    t2 = threading.Thread(target=dance, name="Dance",
                          kwargs={"name": "张三", "age": "15", "address": "北京"})
    print(threading.enumerate())
    t1.start()
    t2.start()
    print(threading.enumerate())
    print("开启线程后的活动线程数量", threading.active_count())
    print("主程序执行完毕")
