import socket
import threading


def recv_msg(udp_socket):
    while True:
        recv_msg = udp_socket.recvfrom(1024)
        recv_ip = recv_msg[1]
        recv_msg = recv_msg[0].decode("utf-8")
        # 3. 显示接收到的数据
        print(">>>%s:%s" % (str(recv_ip), recv_msg))


def send_msg(udp_socket, dest_ip, dest_port):
    while True:
        send_data = input("请输入要发送的数据：")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 7788))
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方端口："))
    t1 = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))
    t1.start()
    t2 = threading.Thread(target=recv_msg, args=(udp_socket,))
    t2.start()


if __name__ == '__main__':
    main()
