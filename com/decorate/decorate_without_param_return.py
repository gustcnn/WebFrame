#--*--coding:utf-8
#Author:cnn
#对无参无返回值的函数进行装饰
def set_func(func):
    def call_func():
        print("---权限验证1---")
        print("---权限验证2---")
        func()
    return call_func
#无参无返回值test1()
@set_func
def test1():
    print("----test1----")

# #a指向call_func
# a=set_func(test1)
# #调用call_func(),执行里面的代码,里面会调用test1
# a()

#调用set_func,传入test1,将返回值赋给test1,test1指向call_func
# test1=set_func(test1)
# #调用test1,执行call_func里面的代码
# test1()


test1()