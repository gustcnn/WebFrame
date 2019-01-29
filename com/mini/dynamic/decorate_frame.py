# --*--coding:utf-8
# Author:cnn
import os

path = os.path.dirname(os.path.dirname(__file__))

# URL_FUNC_DICT = {
#     "/index.py": index,
#     "/register.py": register,
#     "/login.py": login
# }
URL_FUNC_DICT = dict()


def route(path):
    def set_func(func):
        URL_FUNC_DICT[path] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


@route("/center.py")
def center():
    with open(path + "/templates/center.html", encoding="utf8") as f:
        content = f.read()
    return content


@route("/index.py")
def index():
    with open(path + "/templates/index.html", encoding='UTF-8') as f:
        content = f.read()
    return content


def application(envion, func_p):
    """
    字典传参数,判断请求的页面,根据请求,动态响应页面
    :param envion: 字典
    :param func_p: 函数
    :return:
    """
    # 请求文件名如/index.py
    file_name = envion["path_info"]
    func_p("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    # if file_name in URL_FUNC_DICT:
    #     func = URL_FUNC_DICT[file_name]
    #     return func()
    try:
        func=URL_FUNC_DICT[file_name]
        return func()
    except Exception as e:
        return "产生了异常%s"%str(e)
