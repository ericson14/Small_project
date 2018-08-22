import socket

if __name__ == '__main__':
    tcp_server_socket = socket.socket()
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 14452))
    tcp_server_socket.listen(128)
    client_socket, ip_port = tcp_server_socket.accept()
    data_bin = client_socket.recv(5000)
    print(data_bin.decode())
    client_socket.close()
    tcp_server_socket.close()
