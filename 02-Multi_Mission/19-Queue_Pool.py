import multiprocessing


def put_data(queue):
    for i in range(10):
        queue.put((i+1)*121)
        if queue.qsize() == 6:
            break


def get_data(queue):
    for i in range(10):
        # 这里异步模式下Manager里的Queue的nowait方法不会报错，但正常的get还是会阻塞
        print(queue.get_nowait())
        # if queue.empty():
        #     break


if __name__ == '__main__':
    q = multiprocessing.Manager().Queue()
    p = multiprocessing.Pool(2)
    # p.apply(put_data, (q, ))
    # p.apply(get_data, (q, ))
    value = p.apply_async(put_data, (q, ))
    value.wait()
    print(value)
    p.apply_async(get_data, (q, ))
    p.close()
    p.join()
