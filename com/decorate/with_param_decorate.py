# --*--coding:utf-8
# Author:cnn
"""装饰器带有参数"""


def set_level(level_num):
    def outter(func):
        def inner(*args, **kwargs):  # *args告诉解释器是不定长参数
            if level_num == 1:
                print("level %s 权限验证" % level_num)
            elif level_num == 2:
                print("level %s 权限验证" % level_num)
            result = func(*args, **kwargs)  # 告诉解释器拆包
            return result

        return inner

    return outter


@set_level(1)  # 先调用函数set_level(),将1做为实参传递,使用返回值outter进行装饰
def login(*args, **kwargs):
    print("欢迎%s光临." % args)
    print("你好%s" % kwargs)
    return "200", "ok"


@set_level(2)
def login_level(*args, **kwargs):
    print("欢迎%s光临." % args)
    print("你好%s" % kwargs)
    return "200", "ok"


result = login("cnn", age=18)
print(result)

result = login_level("cnn", age=19)
print(result)
