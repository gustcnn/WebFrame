# --*--coding:utf-8
# Author:cnn
import time


def login():
    return "gustcnn welcome our website %s" % time.ctime()


def register():
    return "thank you for your register %s" % time.ctime()


def profile():
    return "profile %s" % time.ctime()


def application(file_name):
    """根据用户名判断调用哪个方法,更好的解耦,不用修改server代码"""
    #print(file_name)
    if file_name == "/login.py":
        return login()
    elif file_name == "/register.py":
        return register()
    elif file_name == "/profile.py":
        return profile()
    else:
        return "not found your page."
