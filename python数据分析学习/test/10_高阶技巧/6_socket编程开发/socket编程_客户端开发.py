"""
演示socket客户端开发
"""
import socket
#创建socket对象
socket_client = socket.socket()
#绑定ip地址和端口
socket_client.bind("localhost",8888)

while True:

    #发送消息
    msg = input("输入要给服务端发送的消息：")
    if msg == "quit":
        break
    socket_client.send(msg.encode("utf-8"))
    #接收返回消息
    recv_data = socket_client.recv(1024)
    print(f"服务端回复的消息是：{recv_data.decode('utf-8')}")

#关闭链接
socket_client.close()