# --*--coding:utf-8
# Author:cnn
# 对带参数,无返回值的函数进行装饰

def outter(func):
    def inner(user):
        print("---权限验证---")
        func(user)

    return inner


# def login(user):
#     print("welcome %s to login."%user)
#
# t=outter(login)
# t("cnn")
@outter
def login(user):
    print("welcome %s to login." % user)


login("cnn")
