# --*--coding:utf-8
# Author:cnn
import socket
import multiprocessing
import re
import os

CLRF = "\r\n"
OBJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


# print(OBJECT_PATH)

class Server(object):
    """web服务器"""

    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 9999

    def handler_forever(self, request_socket):
        """处理请求"""
        # 接收客户端请求
        recv_data = request_socket.recv(1024)
        recv_data_str = recv_data.decode("utf8")
        print(recv_data_str)
        # 获得请求头的第一行,即GET HTTP/1.1 200 OK
        recv_data_list = recv_data_str.splitlines()
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

    def main(self):
        # 创建socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定ip
        server_socket.bind((self.ip, self.port))
        # 创建监听
        server_socket.listen()
        try:
            while True:
                # 循环接收客户端连接
                request_socket, request_ip = server_socket.accept()
                p = multiprocessing.Process(target=self.handler_forever, args=(request_socket,))
                p.start()
                # 关闭监听套接字
                request_socket.close()
        finally:
            if server_socket is not None:
                server_socket.close()


if __name__ == '__main__':
    web_server = Server()
    web_server.main()
