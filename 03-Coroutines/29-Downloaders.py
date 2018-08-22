from gevent import monkey, spawn, joinall
from urllib.request import urlopen

monkey.patch_all()


def my_download(url):
    print("Get:{}".format(url))
    resp = urlopen(url)
    data = resp.read()
    print("{} bytes received from {}".format(len(data), url))


if __name__ == '__main__':
    joinall([
        spawn(my_download, "http://www.baidu.com"),
        spawn(my_download, "http://www.itcast.cn"),
        spawn(my_download, "http://www.itheima.com")
    ])
