# --*--coding:utf-8
# Author:cnn
"""不定长参数装饰器"""


def outter(func):
    def inner(*args, **kwargs):  # *args告诉解释器是不定长参数
        print("-", args)
        print("--", kwargs)
        print("inner".center(10, "-"))
        # func(args,kwargs)#告诉解释器是传递了2个参数,1个元组,1个字典
        result = func(*args, **kwargs)  # 告诉解释器拆包
        return result

    return inner


@outter
def login(*args, **kwargs):
    print("欢迎%s光临." % args)
    print("你好%s" % kwargs)
    return "200", "ok"


result = login("cnn", age=18)
print(result)
