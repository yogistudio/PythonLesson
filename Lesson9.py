# coding:utf-8

'''
date：2017-11-07
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''


class test1(object):
    """
    test1class
    """
    afield = "testfield"

    # 如果属性为可变对象，所有引用的类对象取值都会不可预知的修改
    # 如afiled=["test"],a=test1(),b=test1(),a.afield[0]="hello",则b的afield也会更改
    def amethod(self):
        print "testmodule"


print test1.__name__
print test1.__doc__
print test1.__dict__
print test1.__bases__

ainstance = test1()
binstance = test1()

print ainstance.afield
print binstance.afield
print ainstance.amethod()
print binstance.amethod()

print dir(ainstance)
print ainstance.__doc__
print ainstance.__dict__

ainstance.afield = "hello"
print ainstance.afield
print binstance.afield
print ainstance.__dict__
