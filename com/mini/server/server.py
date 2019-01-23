# --*--coding:utf-8
# Author:cnn
import socket
import multiprocessing
import re
import os

CLRF = "\r\n"
OBJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class Server(object):
    """多进程面向对象服务器"""
    def __init__(self):
        """初始化"""
        #创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #绑定ip
        self.server_socket.bind(("127.0.0.1", 9000))
        #监听
        self.server_socket.listen()

    def run_forever(self):
        """循环接收客户端连接"""
        try:
            while True:
                #等待客户端连接
                client_socket, add = self.server_socket.accept()
                #创建进程对象,传入参数
                m = multiprocessing.Process(target=self.service_client, args=(client_socket,))
                #启动进程
                m.start()
                #关闭请求套接字
                client_socket.close()
        finally:
            self.stop_server()
    def stop_server(self):
        """关闭监听套接字"""
        if self.server_socket is not None:
            self.server_socket.close()

    def service_client(self, request_socket):
        """处理客户端请求"""
        recv_data = request_socket.recv(1024).decode("utf8")
        print(recv_data)
        # 获得请求头的第一行,即GET HTTP/1.1 200 OK
        recv_data_list = recv_data.splitlines()
        # print(recv_data_list)
        if len(recv_data_list) != 0:
            recv_data_get = recv_data_list[0]
            # re_html = r"[^/]+(/[^ ]*)"
            re_html = r"[\w ]*(/[^ ]*)"
            re_html_result = re.match(re_html, recv_data_get)
            file_name = None
            # 判断正则匹配结果,匹配到了,获得匹配的值,如果浏览器输入/则默认返回index.html
            if re_html_result:
                file_name = re_html_result.group(1)
                if file_name == "/":
                    file_name = "/index.html"
            try:
                file = open(OBJECT_PATH + "/htmls" + file_name, "rb")
            except:
                response_404 = "HTTP/1.1 404 NOT FOUND" + CLRF
                response_404 += "Content-Type:text/html;charset=utf-8" + CLRF
                response_404 += CLRF
                request_socket.send(response_404.encode("utf8"))
                try:
                    file_404 = open(OBJECT_PATH + "/htmls/404.html", "rb")
                    content_404 = file_404.read()
                    request_socket.send(content_404)
                except:
                    print("页面不存在")
                else:
                    file_404.close()
            else:
                response = "HTTP/1.1 200 OK" + CLRF
                response += "Content-Type:text/html;charset=utf-8" + CLRF
                response += CLRF
                # 返回响应头给浏览器
                request_socket.send(response.encode("utf8"))
                html_content = file.read()
                request_socket.send(html_content)
                file.close()
        request_socket.close()
def main():
    """控制整体,创建一个对象,调用循环方法"""
    server = Server()
    server.run_forever()

if __name__ == '__main__':
    main()