#--*--coding:utf-8
#Author:cnn
def outter(func):
    def inner():
        print(str(func)+"inner")
        func()
    return inner
@outter
def login():
    print("login...")
@outter
def register():
    print("register...")

li=login()
ri=register()

