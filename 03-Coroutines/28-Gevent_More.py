from gevent import monkey
import gevent
import random
import time


def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())


if __name__ == '__main__':
    monkey.patch_all(ssl=False)
    gevent.joinall([
        gevent.spawn(coroutine_work, "Work1"),
        gevent.spawn(coroutine_work, "Work2")
])
