# --*--coding:utf-8
# Author:cnn
x = 300


def t_1():
    #global x
    x = 200
    print("test1--x=%s" % x)
    def t_2():
        # 闭包里面调用函数外部的变量使用nonlocal
        nonlocal x
        print("-----1----x=%d" % x)
        x = 100
        print("-----2----x=%d" % x)

    return t_2


t1 = t_1()
# 调用test2()
t1()
