from socket import socket


def main():
    tcp_client_socket = socket()
#    server_ip = input("请输入服务器IP：")
#    server_port = int(input("输入服务器端口："))
#    tcp_client_socket.connect((server_ip, server_port))
    tcp_client_socket.connect(("192.168.172.128", 6095))
    print("连接成功！")
    tcp_client_socket.send("请求下载。。".encode())
    print("\n********可供下载的文件**********\n")
    print(tcp_client_socket.recv(2048).decode("utf-8"))
    print("\n**********************")

    file_name = input("输入要下载的文件名：")
    tcp_client_socket.send(file_name.encode())
    try:
        with open("[接收]" + file_name, "wb") as f:
            while True:
                recv_data = tcp_client_socket.recv(1024)
                if recv_data:
                    f.write(recv_data)
                else:
                    break
    except Exception as e:
        print("下载失败，原因是：" + str(e))
    else:
        print("下载完成！")
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
