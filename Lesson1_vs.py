# coding:utf-8

'''
date：2017-11-08
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''
import sys
floatList = [float(item) for item in sys.argv[1:]]
print("The sum was %.2f !" % sum(floatList))

import threading

a = 0
lock=threading.Lock()

def doWork():
    global a
    for i in range(1000000):  #should be OK if 10
        lock.acquire()  #lock是全局的变量，只要一个执行了，其他的thread都无法执行
        a += 1
        '''
        with lock
            a+=1
        这个办法更好，不会出现死锁
        '''
        lock.release()


aThread = threading.Thread(target=doWork, name="aThreadObject")
bThread = threading.Thread(target=doWork, name="bThreadObject")
aThread.start()
bThread.start()
aThread.join()
bThread.join()

print a
