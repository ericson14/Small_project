from threading import Thread
import socket


def client_handler(client_socket):
    while True:
        data = client_socket.recv(1024)
        if data:
            print(data.decode())
            client_socket.send("数据处理中.....".encode())
        else:
            print("连接已断开！")
            client_socket.close()
            break


def main():
    tcp_server_socket = socket.socket()
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server_socket.bind(("", 11780))
    tcp_server_socket.listen(128)

    while True:
        client_socket, ip_port = tcp_server_socket.accept()
        print(ip_port, "已经连接")
        t = Thread(target=client_handler, args=(client_socket, ))
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    main()
