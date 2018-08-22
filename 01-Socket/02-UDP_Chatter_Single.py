import socket


def send_msg(udp_socket, ip_port):
    msg = input("\n请输入发送的信息：")
    udp_socket.sendto(msg.encode(), ip_port)


def rcv_msg(udp_socket):
    str1, ip_port = udp_socket.recvfrom(1024)
    print(">>>{}:{}".format(ip_port, str1.decode()))


def main():
    udp_socket = socket.socket(type=socket.SOCK_DGRAM)
    udp_socket.bind(("", 6152))
    dest_ip = input("\n请输入对方的IP地址：")
    dest_port = int(input("\n请输入端口号："))
    while True:
        print("*"*30)
        print("UDP 简易聊天")
        print("\n1. 发送消息（顺便接收）")
        print("2. 退出")
        print("*"*30)
        op_num = input("请输入要操作的功能序号：")

        if op_num == "1":
            send_msg(udp_socket, (dest_ip, dest_port))
        elif op_num == "2":
            print("\n感谢使用，再见")
            break
        else:
            print("没有此功能，请重新输入。。。")
            continue
        rcv_msg(udp_socket)
    udp_socket.close()
    return True


if __name__ == "__main__":
    main()
