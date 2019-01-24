#--*--coding:utf-8
#Author:cnn
def foo():
    print("foo...")
#函数名,引用
print(foo)
print(id(foo))
#调用函数
foo()
print("---------")
#匿名函数,返回结果
foo=lambda x:x+1
print(foo)
print(id(foo))
print(foo(1))

