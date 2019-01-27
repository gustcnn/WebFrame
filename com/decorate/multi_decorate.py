# --*--coding:utf-8
# Author:cnn
"""多个装饰器装饰同一个方法"""


def add_auth(func):
    print("这是auth的功能.")

    def inner(*args, **kwargs):
        print("auth".center(20, "-"))
        result = func(*args, **kwargs)
        return result

    return inner


def add_event(func):
    print("这是event的功能.")

    def inner(*args, **kwargs):
        print("event".center(20, "-"))
        result = func(*args, **kwargs)
        return result

    return inner


# 多个装饰器装饰同一个方法时
# 在函数定义阶段：执行顺序是从最靠近函数的装饰器开始，自内而外的执行
# 在函数执行阶段：执行顺序由外而内，一层层执行
@add_auth
@add_event
def login(*args, **kwargs):
    print("第一个参数", args)
    print("第二个参数", kwargs)
    print("welcome %s to login." % args)
    return "200", "OK"


result = login("cnn", age=18)
print(result)
