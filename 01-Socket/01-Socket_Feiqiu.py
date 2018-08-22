# coding=utf-8
# 飞秋端口2425
from socket import *

udp_socket = socket(type=SOCK_DGRAM)
dest_addr = ("192.168.71.28", 2425)
send_data = input("请输入要发送的内容:")
send_data += "1:123456:于海:name:32:"
udp_socket.bind(('', 6095))
udp_socket.sendto(send_data.encode("gbk"), dest_addr)
recv_data = udp_socket.recvfrom(2048)
print(recv_data[0].decode())
print("\n", recv_data[1])
udp_socket.close()
