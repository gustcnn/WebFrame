# --*--coding:utf-8
# Author:cnn
import multiprocessing
import os
import re
import socket
import sys

from com.mini.dynamic import decorate_frame

CRLF = "\r\n"
# OBJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
OBJECT_PATH = os.path.dirname(os.path.dirname(__file__))


class Server(object):
    """通过传递字典验证请求不一样,响应不同页面"""

    def __init__(self, port):
        """初始化"""

        # 创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定ip
        self.server_socket.bind(("127.0.0.1", port))
        # 监听
        self.server_socket.listen()

    def run_forever(self):
        """循环接收客户端连接"""
        try:
            while True:
                # 等待客户端连接
                client_socket, add = self.server_socket.accept()
                # 创建进程对象,传入参数
                m = multiprocessing.Process(target=self.service_client, args=(client_socket,))
                # 启动进程
                m.start()
                # 关闭请求套接字
                client_socket.close()
        finally:
            self.stop_server()

    def stop_server(self):
        """关闭监听套接字"""
        if self.server_socket is not None:
            self.server_socket.close()

    def set_response_body(self, status, headers):
        """
        设置响应头
        :param status: 响应状态码
        :param headers: 响应头
        :return:
        """
        self.status = status
        self.headers = [("Server", "nginx_mini_web")]
        self.headers += headers

    def service_client(self, request_socket):
        """处理客户端请求"""
        recv_data = request_socket.recv(1024).decode("utf8")
        print(recv_data)
        # 获得请求头的第一行,即GET HTTP/1.1 200 OK
        recv_data_list = recv_data.splitlines()
        # print(recv_data_list)
        # 请求头不为空则有请求
        if len(recv_data_list) != 0:
            # 获得请求头
            recv_data_get = recv_data_list[0]
            # re_html = r"[^/]+(/[^ ]*)"
            # 匹配/index.html等
            re_html = r"[\w ]*(/[^ ]*)"
            re_html_result = re.match(re_html, recv_data_get)
            file_name = None
            # 判断正则匹配结果,匹配到了,获得匹配的值,如果浏览器输入/则默认返回index.html
            if re_html_result:
                # 获得/index.html等
                file_name = re_html_result.group(1)
                if file_name == "/":
                    file_name = "/index.html"
                # 判断文件名是否以.py结尾,不是返回静态页面,是返回动态页面
                if not file_name.endswith(".py"):
                    try:
                        file = open(OBJECT_PATH + "/templates" + file_name, "rb")
                    except:
                        response_404 = "HTTP/1.1 404 NOT FOUND" + CRLF
                        response_404 += "Content-Type:text/html;charset=utf-8" + CRLF
                        response_404 += CRLF
                        request_socket.send(response_404.encode("utf8"))
                        try:
                            file_404 = open(OBJECT_PATH + "/templates/404.html", "rb")
                            content_404 = file_404.read()
                            request_socket.send(content_404)
                        except:
                            print("页面不存在")
                        else:
                            file_404.close()
                    else:
                        response = "HTTP/1.1 200 OK" + CRLF
                        response += "Content-Type:text/html;charset=utf-8" + CRLF
                        response += CRLF
                        # 返回响应头给浏览器
                        request_socket.send(response.encode("utf8"))
                        html_content = file.read()
                        request_socket.send(html_content)
                        file.close()
                else:
                    response_dict = dict()
                    # 字典的value为请求路径的/index.py
                    response_dict["path_info"] = file_name
                    response_body = decorate_frame.application(response_dict, self.set_response_body)
                    headers = "HTTP/1.1 %s" % self.status + CRLF
                    for temp in self.headers:
                        headers += "%s:%s" % (temp[0], temp[1]) + CRLF
                    headers += CRLF
                    response = headers + response_body
                    request_socket.send(response.encode("utf8"))
        request_socket.close()


def main():
    """控制整体,创建一个对象,调用循环方法"""
    # args_list = sys.argv
    # if len(args_list) < 2:
    #     print("输入格式如 python ***.py 7890")
    #     return
    # else:
    #     try:
    #         port = sys.argv[1]
    #     except Exception as e:
    #         print("端口错误.")
    #         return

    server = Server(9000)
    server.run_forever()


if __name__ == '__main__':
    main()
