# coding:utf-8

'''
date：2017-11-07
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''


class Person(object):
    food = "apple"

    def eat(self):
        print "eat..." + Person.food

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Person <%s>" % self.name

    def __repr__(self):
        return self.name.title()


xiaoming = Person('Xiaoming')
huahua = Person('Huahua')

print xiaoming
print huahua.eat()
