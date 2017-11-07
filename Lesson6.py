# coding:utf-8

'''
date：2017-11-07
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''
adict = {'apple': 1.5, 'pear': 1.4, 'orage': 2.3}
print sorted(adict, key=lambda x: adict[x], reverse=True)
print sorted(adict, key=lambda x: adict[x])
