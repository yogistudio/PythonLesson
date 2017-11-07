# coding:utf-8

'''
date：2017-11-07
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''

import Lesson4
# import Lesson8
from Lesson8 import afun

print afun()

from Lesson8 import imexp

imexp.add3()
add4 = Lesson4.addn()
print add4(4)

bstr = 'Lesson3'
Lesson31 = __import__(bstr)

Lesson31.test2()

print dir(imexp)
print imexp.__dict__['add3']()
