# --*--coding:utf-8
# Author:cnn
import os
from utils.mysql_util import ConnMysql
import pymysql
import re

"""支持伪静态"""
path = os.path.dirname(os.path.dirname(__file__))

URL_FUNC_DICT = dict()


def route(path):
    def set_func(func):
        URL_FUNC_DICT[path] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


@route("/center.html")
def center():
    with open(path + "/templates/center.html", encoding="utf8") as f:
        content = f.read()
    mysql = ConnMysql()
    stock_infos = mysql.execute_myql("select * from info;")
    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/300268.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="300268">
            </td>
        </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6])

    # content = re.sub(r"\{%content%\}", str(stock_infos), content)
    content = re.sub(r"{[^}]+}", html, content)
    return content

@route("/index.html")
def index():
    with open(path+"/templates/index.html",encoding='UTF-8') as f:
        content = f.read()
    mysql=ConnMysql()
    stock_infos=mysql.execute_myql("select * from info;")
    print(stock_infos)
    tr_template = """<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
        </td>
        </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6],line_info[7])

    #re_str=r"{[^}]+}" 匹配{%content%}里面的内容
    content = re.sub(r"{[^}]+}", html, content)

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
        func = URL_FUNC_DICT[file_name]
        return func()
    except Exception as e:
        return "产生了异常%s" % str(e)
