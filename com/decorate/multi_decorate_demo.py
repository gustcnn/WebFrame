# --*--coding:utf-8
# Author:cnn

"""返回<h1>***<h1>"""
def set_h1(func):
    print("----h1----")
    def call_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return "<h1>" + result + "<h1>"

    return call_func

def set_td(func):
    print("----td----")
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return "<td>" + result + "<td>"

    return inner

@set_h1
@set_td
def login(user):
    print("welcome %s to login." % user)
    return "欢迎登录lucid系统"


print(login("cnn"))
