#--*--coding:utf-8
#Author:cnn
#闭包
#y=k*x+b

def line(k,x,b):
    y=k*x+b
    return y
# print(line(2,3,0))
# print(line(2,3,1))
# print(line(2,3,2))
#缺省参数
def line_02(x,k=2,b=3):
    y=k*x+b
    return y
print(line_02(1))
print(line_02(2))
print(line_02(3))
class Line_05(object):
    def __init__(self,k,b):
        self.k=k
        self.b=b
    def __call__(self,x):
        print(self.k*x+self.b)
print("*"*50)
line_05_01=Line_05(2,3)
#实现__call__方法的类,引用可以()
line_05_01(0)
line_05_01(1)
line_05_01(2)

line_05_02=Line_05(3,3)
#实现__call__方法的类,引用可以()
line_05_02(0)
line_05_02(1)
line_05_02(2)
print("*"*50)
#闭包
def line_06(k,b):
    def create_y(x):
        print(k*x+b)
    return create_y
line_06_01=line_06(2,3)
line_06_01(0)
line_06_01(1)
line_06_01(2)

line_06_02=line_06(3,3)
line_06_02(0)
line_06_02(1)
line_06_02(2)


