"""
演示socket服务端开发
"""
import socket
#创建socket对象
socket_server = socket.socket()
#绑定ip地址和端口
socket_server.bind("localhost",8888)
#监听端口
socket_server.listen(1) #listen方法内接受一个整数传参数，表示接受的链接数

#等待客户端链接
# result :tuple = socket_server.accept()
# conn = result[0]  #客户端和服务端链接对象
# address = result[1]  #客户端的地址信息
conn, addr = socket_server.accept()
#accept返回一个二元元祖（链接对象，客户端地址）
#accept是一个阻塞方法，等待客户端的链接，如果没有，就卡在这一行不向下执行
print(f"接收到了客户端的链接，客户端信息是：{addr}")

while True:  #无限循环，无限聊天
    #接收客户端信息，要使用客户端和服务端的本次链接对象，而非socket对象
    data = conn.recv(1024).decode("utf-8")
    #recv接收的参数是缓冲区的大小，
    #recv返回的是一个字节数组也就是bytes对象，不是字符串，可以通过decode的utf-8编码，将字节数组转换为字符串对象
    print(f"客户端发来的消息是：{data}")

    #发送回复消息
    msg = input("请输入回复客户端的消息")   #.encode("utf-8")
    if msg == "quit":  #输入关键字跳出循环
        break
    conn.send(msg)

#关闭链接
conn.close()
socket_server.close()
