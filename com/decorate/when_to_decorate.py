# --*--coding:utf-8
# Author:cnn
# 验证装饰器什么时候开始执行,python解释器从上到下解释的时候,碰到@符号就开始装饰了,不是函数调用的时候才开始装饰
def outter(func):
    print("装饰器开始执行".center(20,"-"))
    def inner(user):
        print("---权限验证---")
        func(user)

    return inner


@outter  # 相当于 login=outter(login)
def login(user):
    print("welcome %s to login." % user)


#login("cnn")
