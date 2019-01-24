#--*--coding:utf-8
#Author:cnn
import os
import sys
#获得参数
args_list=sys.argv
print(args_list[1],args_list[2])
path=os.path.dirname(os.path.dirname(__file__))
print(path)