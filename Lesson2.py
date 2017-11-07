#coding:utf-8

import time

'''
date：2017-11-07
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''

"""
另外一个多行注释，用于函数的_doc_
"""

def add(a,b=3):
    """
    :param a:
    :param b:default is 3
    :return:
    """
    return a+b

astr=raw_input("Please input two number ,like 1, 2:")
alist=[int(item) for item in astr.split(',')]
if len(alist)==1:
    print add(alist[0])
else:
    print add(alist[0],alist[1])
print add.__doc__

test=add
print test(3,4)
print test.__name__

def log(msg,ts=time.time()):
    """
    这里定义了ts，这样每次调用这个函数，输出的都是同一个值，因为默认值是在函数定义时就程序直接写好的，所以应该用log方式
    先定义为None
    请注意：默认参数是函数的属性，所以当定义一个默认参数，直接分配了，所以，默认参数不要用可变变量
    :param msg:
    :param ts:
    :return:
    """
    print msg,ts
log("ths is line")
time.sleep(2)
def log2(msg,ts=None):
    if ts is None:
        ts=time.time()
    print ts,msg
log2("test")

'''
LEGB：对于变量而言，函数定义的默认属性是全局的对象，而不是变量
Globel变量
函数体内部如果想用全局变量，可以在函数体内部使用global 变量名
如
a=4
def log():
    global a
查找参数时，先找local，然后再找golbal
'''

