import socket

tcp_client_socket = socket.socket()

server_ip = input("请输入服务器IP：")
server_port = int(input("请输入端口号："))
tcp_client_socket.connect((server_ip, server_port))

send_data = input("发送的消息是：")
tcp_client_socket.send(send_data.encode())

recv_data = tcp_client_socket.recv(1024)
print("接收到：", recv_data.decode())

tcp_client_socket.close()
