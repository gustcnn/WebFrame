# --*--coding:utf-8
# Author:cnn
# 带参数和返回值的装饰器
def outter(func):
    def inner(user):
        print("权限验证.")
        result=func(user)
        return result

    return inner

@outter
def login(user):
    print("welcome %s to login."%user)
    return "200"

# t=outter(login)
# y=t("cnn")
# print(y)

result=login("cnn")
print(result)
