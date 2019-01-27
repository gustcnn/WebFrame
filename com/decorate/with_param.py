# --*--coding:utf-8
# Author:cnn
"""带参数装饰器,如果函数没有传入值,这个方式不好"""


def outter(func):
    def inner(*args, **kwargs):  # *args告诉解释器是不定长参数
        level = args[0]  # 取不定长参数的第一个值,根据第一个值的结果,判断执行哪一步
        if level == "cnn":
            print("---%s---" % level)
        elif level == "gustcnn":
            print("---%s---" % level)
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
