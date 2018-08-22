import re
import gevent
import socket
import _65_Frame
from gevent import monkey
monkey.patch_all(ssl=0)


class HTTPServer(object):
    """HTTP 服务器类"""
    def __init__(self):
        """建立套接字"""
        self.port = 19234
        tcp_server = socket.socket()
        tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_server.bind(("", self.port))
        tcp_server.listen(128)
        print("服务器已开启。。")
        self.tcp_server = tcp_server

    def start(self):
        """开启服务器"""
        while True:
            client_server, client_addr = self.tcp_server.accept()
            g1 = gevent.spawn(self.client_handler, client_server)
            if KeyboardInterrupt:
                g1.join()
                self.tcp_server.close()
                break

    def client_handler(self, client_server):
        """处理客户端请求"""
        request_data = client_server.recv(1024)
        if not request_data:
            print("请求已经断开")
            client_server.close()
            return
        request_head = request_data.decode().split("\r\n")[0]
        result = re.match(r'\w+\s+(\S+)\s+HTTP/1\.(1|0)', request_head)
        if result is None:
            print("不符合HTTP协议")
            client_server.close()
            return
        resource = result.group(1)
        if resource == "/":
            resource = "/index.html"
        if resource.endswith(".html"):
            self.dynamic_resource(client_server, resource)
        else:
            self.static_resource(resource, client_server)

    @staticmethod
    def dynamic_resource(client_server, resource):
        """处理动态资源请求"""
        status, headers, response_body = _76_Frame.dynamic_resource({"PATH_INFO": resource})
        response_line = "HTTP/1.1 {}\r\n".format(status)
        response_headers = "Server: PWS/1.1\r\n"
        for header in headers:
            response_headers += "{}: {}\r\n".format(*header)
        response_data = response_line + response_headers + "\r\n" + response_body
        client_server.send(response_data.encode())
        client_server.close()

    @staticmethod
    def static_resource(resource, client_server):
        """处理静态资源"""
        response_head = "Server: PWS/1.1\r\n"
        response_line = ""
        response_body = ""
        try:
            file = open("./static" + resource, "rb")
            response_line = "HTTP/1.1 200 OK\r\n"

        except Exception as e:
            response_line = "HTTP/1.1 404 Page Not Found\r\n"
            response_body = "<h>哎哟，页面出错了{}。。。。</h>".format(str(e)).encode()
        else:
            response_body = file.read()
            file.close()
        finally:
            response_data = (response_line + response_head + "\r\n").encode() + response_body
        client_server.send(response_data)
        client_server.close()


def main():
    h1 = HTTPServer()
    print("端口{}".format(h1.port))
    h1.start()


if __name__ == '__main__':
    main()
