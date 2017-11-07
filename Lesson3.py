#coding:utf-8

import time

'''
date：2017-11-07
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''
'''
查找参数时，先找local，然后再找golbal
'''
a=5
def prints():
    global a
    #global表示使用全局变量a
    a1=a+1
    a=a+1
    print a1
prints()

def test2():
    print a

test2()