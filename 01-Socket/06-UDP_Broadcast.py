import socket

udp_broadcast = socket.socket(type=socket.SOCK_DGRAM)

udp_broadcast.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

info = input("请输入要广播的信息：")
udp_broadcast.sendto(info.encode(), ("255.255.255.255", 8989))
udp_broadcast.close()
