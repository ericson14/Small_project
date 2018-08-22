import socket

if __name__ == '__main__':
    tcp_client_socket = socket.socket()
    ip_port = ("ntlias-stu.boxuegu.com", 80)
    tcp_client_socket.connect(ip_port)

    request_line = "GET / HTTP/1.1\r\n"
    request_head = "Host: ntlias-stu.boxuegu.com\r\n"
    # 发送请求报文
    request_data = request_line + request_head + "\r\n"
    tcp_client_socket.send(request_data.encode())
    # 收到响应报文
    data_bin = tcp_client_socket.recv(5000)
    print(data_bin.decode())
    list1 = data_bin.decode().split("\r\n\r\n")
    with open("./Download/index1.html", "wb") as f:
        f.write(list1[1].encode())
        while True:
            data = tcp_client_socket.recv(3000)
            if data:
                f.write(data)
            else:
                break
    tcp_client_socket.close()
