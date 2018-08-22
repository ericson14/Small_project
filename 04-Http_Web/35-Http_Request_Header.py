import socket

tcp_client = socket.socket()
tcp_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_client.bind(("", 10265))
tcp_client.listen(1)
browser, ip_port = tcp_client.accept()
print(ip_port, "已经连接")
print(browser.recv(5000).decode())
tcp_client.close()
