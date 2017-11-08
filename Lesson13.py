# coding:utf-8

'''
date：2017-11-08
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''

# import time, multiprocessing, random, logging, sys
#
#
# def doWork():
#     print sum([random.random() for i in range(10000000)])
#     sys.stdout.flush()
#
#
# if __name__ == "__main__":
#     multiprocessing.log_to_stderr(logging.DEBUG)
#     startTime = time.time()
#     time.clock()
#     aProcess = multiprocessing.Process(target=doWork, name="aProcess")
#     aProcess.start()
#     bProcess = multiprocessing.Process(target=doWork, name="bProcess")
#     bProcess.start()
#
#     aProcess.join()
#     bProcess.join()
#     print "== ", time.time() - startTime

import multiprocessing
import random
import time


def doWork(j):
    print "%s: start... : %s" % (multiprocessing.current_process().name, time.time())
    ret = j
    ret = sum([random.random() for i in range(10000000)])
    print "%s: stop...  : %s" % (multiprocessing.current_process().name, time.time())
    return j, ret


if __name__ == "__main__":  # Bug
    startTime = time.time()
    p = multiprocessing.Pool(4)  # 1
    aList = p.map(doWork, range(8))
    print aList
    print time.time() - startTime
