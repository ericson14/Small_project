import socket
import re
import sys
import gevent
from gevent import monkey
monkey.patch_all(ssl=False)


class HTTPServer(object):
    # 初始化套接字
    def __init__(self, port):
        tcp_server_socket = socket.socket()
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_server_socket.bind(("", port))
        tcp_server_socket.listen(128)
        print("服务器开启")
        self.tcp_server_socket = tcp_server_socket

    # 服务器接收
    def start(self):
        while True:
            client_server_socket, ip_port = self.tcp_server_socket.accept()
            print(ip_port, "已经连接")
            gevent.spawn(self.client_handler, client_server_socket)
            # g1 = gevent.spawn(self.client_handler, client_server_socket)
            # ex = input()
            # if ex == "q":
            #     self.tcp_server_socket.close()
            #     g1.join()
            #     break

    @staticmethod  # 客户端处理方法
    def client_handler(client_server_socket):
        # 收取请求报文
        request_data = client_server_socket.recv(5000)
        if not request_data:   # 客户端是否在线
            print("客户端已经断开")
            client_server_socket.close()
            return
        request_data = request_data.decode().split("\r\n")
        obj = re.match(r"\w+\s(\S+)\sHTTP/1\.1|0", request_data[0])
        if obj is None:
            print("不是HTTP协议")
            client_server_socket.close()
            return
        request_url = obj.group(1)  # 提取请求URL
        if request_url == "/":
            request_url = "/index.html"

        response_head = "Server: PWS/1.0\r\n"
        try:
            response_line = "HTTP/1.1 200 OK\r\n"  # 请求的网页存在，返回200
            with open("./static" + request_url, "rb") as f:
                response_body = f.read()
        except Exception as e:
            response_line = "HTTP/1.1 404 Page Not Found\r\n"  # 请求的网页不存在，返回404
            with open("./static/404.html", "rb") as f:
                response_body = f.read() + ("Error: " + str(e)).encode()
        # 发送响应报文
        response_data = (response_line + response_head + "\r\n").encode() + response_body
        client_server_socket.send(response_data)
        client_server_socket.close()


def main():
    print("执行文件时候可以添加端口，没有的话默认为26653端口")
    if sys.argv[1]:
        if not sys.argv[1].isdigit():
            print("端口号需为整数")
            return
        if not 0 <= int(sys.argv[1]) <= 65535:
            print("端口取值范围是0-65535")
            return
        h1 = HTTPServer(int(sys.argv[1]))
    else:
        h1 = HTTPServer(26653)
    h1.start()


if __name__ == '__main__':
    main()
