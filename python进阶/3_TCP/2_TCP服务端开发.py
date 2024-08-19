"""
1.当TCP客户端程序想要和TCP服务端程序进行通信的时候必须要先建立连接
2.TCP客户端程序一般不需要绑定端口号，因为客户端是主动发起建立连接的。
3.TCP服务端程序必须绑定端口号，否则客户端找不到这个TCP服务端程序。
4.listen后的套接字是被动套接字，只负责接收新的客户端的连接请求，不能收发消息。
5.当TCP客户端程序和TCP服务端程序连接成功后，TCP服务器端程序会产生一个新的套接字，收发客户端消息使用该套接字。
6.关闭accept返回的套接字意味着和这个客户端已经通信完毕。 7.当客户端的套接字调用close后，服务器端的recv会解阻塞，返回的数据长度为0，服务端可以通过返回数据的长度来判断客户端是否
已经下线，反之服务端关闭套接字，客户端的recv也会解阻塞，返回的数据长度也为0。
"""

import socket

if __name__ == "__main__":
    # 1.创建服务端套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.绑定IP地址和端口号，如果bind中第一个参数为空，默认本机IP地址
    tcp_server_socket.bind(('',8888))
    # 3.设置监听 128:服务端等待排队链接的最大数量
    tcp_server_socket.listen(128)
    # 4.等待接受客户端的连接请求 accept阻塞等待，返回一个用来和客户端通socket，客户端的地址
    conn_socket,ip_port = tcp_server_socket.accept()
    print("客户端地址：",ip_port)
    # 5.接收数据
    recv_data = conn_socket.recv(1024)
    print("接收到的数据：",recv_data.decode('utf-8'))
    # 6.发送数据
    conn_socket.send("客户端的数据收到了：".encode('utf-8'))
    # 7.关闭套接字
    conn_socket.close()
    tcp_server_socket.close()