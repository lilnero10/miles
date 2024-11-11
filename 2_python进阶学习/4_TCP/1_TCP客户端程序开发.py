"""
参数1：‘AF_INET'，表示IPv4地址类型
参数2：‘SOCK_STREAM'，表示TCP传输协议类型
"""
import socket

if __name__ == "__main__":
    #1、创建客户端套接字对象
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2、和服务端套接字建立链接
    tcp_client_socket.connect(("127.0.0.1", 8080))
    #3、发送数据
    tcp_client_socket.send("nihao".encode("utf-8"))
    #4、接受数据 recv阻塞等待数据的到来
    recv_data = tcp_client_socket.recv(1024)
    print(recv_data.decode("utf-8"))
    #5、关闭客户端套接字
    tcp_client_socket.close()