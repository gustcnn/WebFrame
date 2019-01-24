# --*--coding:utf-8
# Author:cnn
import os

path=os.path.dirname(os.path.dirname(__file__))


def login():
    with open(path + "/templates/login.html", encoding="utf8") as f:
        content = f.read()
    return content


def index():
    with open(path + "/templates/header.html", encoding='UTF-8') as f:
        content = f.read()
    return content


def register():
    with open(path + "/templates/register.html", encoding="utf8") as f:
        content = f.read()
    return content
def application(envion, func_p):
    """
    字典传参数,判断请求的页面,根据请求,动态响应页面
    :param envion: 字典
    :param func_p: 函数
    :return:
    """
    #请求文件名如/index.py
    file_name=envion["path_info"]
    func_p("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    if file_name=="/index.py":
        return index()
    elif file_name=="/login.py":
        return login()
    elif file_name=="/register.py":
        return register()

