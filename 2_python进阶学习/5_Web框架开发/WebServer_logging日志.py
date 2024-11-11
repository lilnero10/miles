import socket
import threading
import dynamic.frame #服务器代码和框架代码截耦合，修改时互不影响
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime) - %(filename)s[line:%(lineno)d] - %(levelname)s : %(message)s',
                    filename="log.txt",
                    filemode='w')

# 把提供服务的Web服务器抽象成一个类（HttpWebServer）
class HttpWebServer:
    # 提供Web服务器的初始化方法，在初始化方法里面创建socket对象
    def __init__(self):
        # 1.编写一个TCP服务端程序
        # 创建socekt
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口复用
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定地址
        self.tcp_server_socket.bind(('', 8080))
        # 设置监听
        self.tcp_server_socket.listen(128)

    def handle_client_request(self, client_socket):
        # 获取浏览器的请求信息
        client_request_data = client_socket.recv(1024).decode()
        print(client_request_data)
        # 获取用户请求资源的路径
        request_data = client_request_data.split(" ")
        request_path = request_data[1]

        # 判断客户端是否关闭，避免浏览器关闭，解析空字符串报错（这里空字符串作为数据传过来，长度为1）
        if len(request_data) == 1:
            client_socket.close()
            return

        # 判断如果不加后缀，直接返回根目录主页
        if request_path == "/":
            request_path = "/index.html"

        # 服务器判断是否动态资源
        if request_path.endswith(".html"):
            """动态资源"""
            logging.info("动态资源" + request_path)
            # 应答行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 应答头
            response_header = "Context-Type: text/html;charset=utf-8\r\n"
            # 应答体
            response_body = dynamic.frame.application(request_path)
            # 应答数据
            response_data = response_line + response_header + "\r\n" + response_body
            client_socket.send(response_data.encode("utf"))
            client_socket.close()
        else:
            """静态资源"""
            logging.info("静态资源" + request_path)
            # 3.读取固定页面数据，把页面数据组装成HTTP响应报文数据发送给浏览器
            # 根据请求资源的路径，读取指定文件的数据
            try:
                with open(" ./static" + request_path, "rb") as f:
                    file_data = f.read()
            except Exception as e:
                logging.error("访问错误路径" + str(e))
                # 返回404错误数据
                # 应答行
                response_line = "HTTP/1.1 404 NOT FOUND\r\n"
                # 应答头
                response_header = "Server: pwb\r\n"
                # 应答体
                response_body = "404 NOT FOUND sorry"
                # 应答数据
                # 组装指定文件数据的响应报文，发送给浏览器
                response_data = (response_line + response_header + "\r\n" + response_body).encode()
            else:
                # 应答行
                response_line = "HTTP/1.1 200 0K\r\n"
                # 应答头
                response_header = "Server: pwb\r\n"
                # 应答体
                response_body = file_data
                # 应答数据
                # 组装指定文件数据的响应报文，发送给浏览器
                response_data = (response_line + response_header + "\r\n").encode() + response_body
            finally:
                # 4.HTTP响应报文数据发送完成以后，关闭服务于客户端的套接字
                client_socket.close()

    # 提供一个开启Web服务器的方法，让Web服务器处理客户端请求操作。
    def start(self):
        while True:
            # 2.获取浏览器发送的HTTP请求报文数据
            # 建立链接
            client_socket, client_addr = self.tcp_server_socket.accept()

            # 当客户端和服务端建立连接成功，创建子线程，使用子线程专门处理客户端的请求，防止主线程阻塞
            sub_thread = threading.Thread(target=self.handle_client_request, args=(client_socket,))
            sub_thread.start()


if __name__ == "__main__":
    my_web_server = HttpWebServer()
    my_web_server.start()
