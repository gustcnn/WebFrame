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
