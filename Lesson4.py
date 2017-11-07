#coding:utf-8

import time

'''
date：2017-11-07
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''
'''
高阶函数：map
map函数，类似于模板函数，有状态的函数
'''

def addn(n=3):
    def add(a):
        return a+n
    return add  #返回的是add函数，调用这个函数时，N=3被保存为add的属性

add3=addn()
print add3  #可以看出这个返回值就是一个函数，高阶函数
print add3(42)
add5=addn(5)
print add5(3)

print map(lambda x:x+10,range(5))
'''
等同于
print [i+10 for i in range(5)]
map是并发执行的，而这个是顺序的（实际上python有个全局解释性锁，不能并发）
'''

print map(pow,[1,2,3],[2,3,4])