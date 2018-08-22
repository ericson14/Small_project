import multiprocessing
import time


def movie():
    print("电影下载完毕。。。", multiprocessing.current_process().pid)
    time.sleep(0.5)


if __name__ == '__main__':
    po = multiprocessing.Pool(5)
    for i in range(10):
        po.apply_async(movie)
    po.close()
    po.join()
