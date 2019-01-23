# --*--coding:utf-8
# Author:cnn
def application(envion, func_p):
    """
    支持wsgi
    :param envion: 字典
    :param func_p: 函数
    :return:
    """
    func_p("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    return "你好"
