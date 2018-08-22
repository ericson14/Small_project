#!/usr/bin/python3
# coding=utf-8

import socket
import sys
import subprocess


def get_file_content(file_name, sockets):
    try:
        with open(file_name, "rb") as f:
            while True:
                content = f.read(1024)
                if content:
                    sockets.sent(content)
                else:
                    break
    except FileNotFoundError:
        print("没有要下载的文件...")
    except Exception as e:
        print("读取错误", str(e))
    else:
        print(file_name + "传输完毕")


def main():
    if len(sys.argv) != 2:
        print("请按以下方式执行：python3 xxx.py 端口号")
        print("或者: ./xxx.py 端口号")
        return
    else:
        port = int(sys.argv[1])

    tcp_server_socket = socket.socket()
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server_socket.bind(("", port))
    tcp_server_socket.listen(128)

    client_socket, client_addr = tcp_server_socket.accept()
    msg = client_socket.recv(1024).decode()

    print("来自{}的主机{}。。".format(client_addr, msg))

    file_list = subprocess.run("ls", shell=True, stdout=subprocess.PIPE)
    client_socket.send(file_list.stdout)

    file_name = client_socket.recv(1024).decode()
    print("对方请求的下载文件名为：{}".format(file_name))
    get_file_content(file_name, client_socket)

    print("下载结束，服务器选择休息。。。。")
    client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
