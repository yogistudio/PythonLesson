# coding:utf-8

'''
date：2017-11-07
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''
'''
filter函数
reduce函数
'''

print filter((lambda x: x > 0), range(-5, 5))
print reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
