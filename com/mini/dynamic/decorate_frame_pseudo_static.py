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
    return content

#TODO
@route("/index.html")
def index():
    with open(path + "/templates/index.html", encoding='UTF-8') as f:
        content= f.read()
    # 创建Connection连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='stock_db', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute("select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on i.id=f.info_id;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()

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
                <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
            </td>
        </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6], line_info[0], line_info[0])
    #print("html",html)
    # content = re.sub(r"\{%content%\}", str(stock_infos), content)
    # content_html = re.sub(r"([^_\/\.]+)*\{%content%\}([^_\/\.]+)*",html,content)
    # print(content_html)
    return html


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
