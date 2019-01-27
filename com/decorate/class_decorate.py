# --*--coding:utf-8
# Author:cnn
class ClassDecorator(object):
    """通用类装饰器"""
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result=self.func(*args,**kwargs)
        return result


@ClassDecorator  # 相当于login=ClassDecorator(login)
def login(*args, **kwargs):
    print("welcome %s to login." % args)
    print("--", kwargs)
    return "200", "OK"
print(login("cnn"))