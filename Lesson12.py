# coding:utf-8

'''
date：2017-11-08
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''

# import subprocess
# subprocess.check_output(r'dir')

import os

os.system(r'dir')

import time, threading


def doWork():
    name = threading.currentThread().getName()
    print "%s start..." % name
    time.sleep(3)
    print "%s stop..." % name


print time.time()
aThread = threading.Thread(target=doWork, name="aThread")
aThread.start()
bThread = threading.Thread(target=doWork, name="bThread")
bThread.start()

aThread.join()
bThread.join()
print time.time()

print '我们'
