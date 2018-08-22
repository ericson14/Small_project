import socket

tcp_sever_socket = socket.socket()

tcp_sever_socket.bind(("", 6095))
tcp_sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
tcp_sever_socket.listen(1)

client_socket, client_addr = tcp_sever_socket.accept()
print("有人连接了！")
recv_data = client_socket.recv(1024)
print("{}连接了本服务器并发送了：{}".format(client_addr, recv_data.decode()))
client_socket.send("Thanks!".encode())

client_socket.close()
