#--*--coding:utf-8
#Author:cnn
import os
import re

path=os.path.dirname(os.path.dirname(__file__))
# #print(path)
with open(path+"/templates/index.html", encoding='UTF-8') as f:
    content = f.read()
print(content)

#匹配大括号里面的内容
re_str=r"{[^}]+}"
content=re.sub(re_str,"嘿嘿",content)
print(content)