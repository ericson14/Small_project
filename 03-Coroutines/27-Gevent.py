import gevent


def foo(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(.1)


g1 = gevent.spawn(foo, 5)
g2 = gevent.spawn(foo, 5)
g3 = gevent.spawn(foo, 5)
g1.join()
g2.join()
g3.join()
