#coding:utf-8

import time

'''
date：2017-11-07
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''
'''
查找参数时，先找local，然后再找golbal
为什么使用元组传参和字典传参？应为有些数据或者字段就是元组和字典，这样更方便，另外可以方便函数的调用，用于框架等
add（4,5）==add（*（4,5))
add(a=4,b=5)==add(**{'a':4,'b':5})


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

'''
行参举例
python中没有函数的重载，后门一个定义的，会覆盖前面一个,一下例子会只能3个参数
'''
def add(a=1,b=2):
    return a+b
def add(a,b,c):
    return a+b+c
'''
正确办法
'''
def add(*argvs):
    return sum(argvs)

print add(1,2,3,4,5)  #等价于 atuple=(12,3,4,5) ,print add(*atuple)

'''
字典传入
'''
def add3(a,**argv):
    print a
    print argv
    return a+sum(argv.values())

print add3(3,b=2,c=5,d=23)

'''
lambda函数，参数在:前面，返回在:后面
'''
fun=lambda x:x**2
print fun(3)

'''
或者
'''
print (lambda x:x**2)(4)