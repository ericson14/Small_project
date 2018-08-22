import multiprocessing
import os
from time import sleep
from random import random


def copy_files(queue, file_name, source_folder, dest_folder):
    with open(source_folder + "/" + file_name, "rb") as fr:
        with open(dest_folder + "/" + file_name, "wb") as fw:
            while True:
                sleep(random())
                content = fr.read(1024)
                if content:
                    fw.write(content)
                else:
                    break
    queue.put(file_name)


def main():
    source_folder = input("请输入要复制的文件夹的名字：")
    dest_folder = source_folder + "[副本]"

    try:
        os.mkdir(dest_folder)
    except Exception as e:
        print("文件夹存在，不必创建", str(e))

    file_names = os.listdir(source_folder)
    queue = multiprocessing.Manager().Queue()
    pool = multiprocessing.Pool(3)
    for file_name in file_names:
        if os.path.isfile(file_name):
            pool.apply_async(copy_files, args=(queue, file_name, source_folder, dest_folder))
    pool.close()

    all_file_num = len(file_names)
    while True:
        file_name = queue.get()
        if file_name in file_names:
            file_names.remove(file_name)

        copy_rate = (all_file_num - len(file_names))*100/all_file_num
        print("\r%.2f%%....(%s)" % (copy_rate, file_name) + " "*50, end="")
        if copy_rate >= 100:
            break
    print()


if __name__ == '__main__':
    main()
