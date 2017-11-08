# coding:utf-8

'''
date：2017-11-08
函数，模块和包，面对对象和设计模式，异常处理，正则表达式，系统脚本
'''
import re

reCmp = re.compile("\d{3,5}")  # 数字出现3-5次
if reCmp.search('http405'):
    print "Match"
else:
    print "non Match"

'''
 . 换行以外的任何字符
 + 前面一个元素出现一次或者多次
 * 前面一个元素出现零次或者多次
 {x,y} 前面一个元素出现在X和Y之间
 [] 选择  
'''

reCmp = re.compile(r'((ab)+)')  # 贪婪匹配，输出结果('ababab', 'ab')，表示可以匹配到所有
print reCmp.search('ababab').groups()
reCmp = re.compile(r'((ab)+?)')  # 非贪婪匹配，输出结果('ab', 'ab')，匹配到一个就完成
print reCmp.search('ababab').groups()

line = "This is Line"
