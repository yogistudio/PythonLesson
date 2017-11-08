# coding:utf-8

'''
date：2017-11-08
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''

import datetime
from subprocess import PIPE

import psutil

print(psutil.cpu_times())
print(psutil.cpu_times())
print(psutil.cpu_times().user)
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times(percpu=True))

print(psutil.virtual_memory())
print(psutil.virtual_memory().total)
print(psutil.swap_memory())

print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())
print(psutil.disk_io_counters(perdisk=True))

print(psutil.net_io_counters())
print(psutil.net_io_counters(pernic=True))

print(psutil.users())
print(psutil.boot_time())
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S'))

print(psutil.pids())
print(psutil.Process(4464))
p = psutil.Process(4464)
print(p.name())
print(p.exe())
print(p.cwd())
print(p.status())
print(p.create_time())
# print(p.uids())
# print(p.gids())
print(p.cpu_times())
print(p.memory_percent())
print(p.memory_info())
print(p.connections())
print(p.num_threads())

p = psutil.Popen(['python', '-c', 'print("hello")'], stdout=PIPE)
print(p.name())
print(p.username())
p.communicate()
