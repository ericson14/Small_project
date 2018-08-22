from threading import Thread
import socket


def send_msg(udp_socket):
    while True:
        msg = input("\n请输入发送的信息（按“q”退出）：")
        if msg == 'q':
            break
#       dest_ip = input("\n请输入对方的IP地址：")
#       dest_port = int(input("\n请输入端口号："))
        dest_ip = "192.168.172.128"
        dest_port = 18402
        udp_socket.sendto(msg.encode(), (dest_ip, int(dest_port)))


def recv_msg(udp_socket):
    while True:
        msg = udp_socket.recvfrom(1024)
        print("\n>>>>>从{}接收到的信息：{}".format(msg[1], msg[0].decode()))


def main():
    udp_socket = socket.socket(type=socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.bind((" ", 36292))
    r_t = Thread(target=recv_msg, args=(udp_socket,), daemon=True)
    r_t.start()
    send_msg(udp_socket)


if __name__ == '__main__':
    main()
