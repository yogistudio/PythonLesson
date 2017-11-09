#coding:utf-8
'''
astr='    i  like apple'
astr.split()
astr1=' '.join(astr.split()).title()
print astr1

astr2='0123456789'
astr3=astr2.strip()
print astr3
print astr3[::-2]

print id(astr3)
'''

'''
Date:2017-11-06
基本类型及基本使用方式
'''
# aTuple=tuple('hello')
# print aTuple
#
# alist=list('hello')
# print alist
# alist[3]=42
# print alist
#
# alist=range(6)
# blist=alist
# blist[1]='test'
# print alist
# #如果blist=alist，表示将2个对象指向同一个源（重映射）
#
# clist=range(7)
# dlist=copy.copy(alist)
# flist=copy.deepcopy(alist)
#
# #重映射，全拷贝，深拷贝概念
#
# elist=[[0]]*3
# elist[0]=[43]
# print elist
# elist[1][0]=42
# print elist
#
# #所有乘法都是简单复制
#
# elist=[[0]]*3
# print elist
# elist[1][0]=42
# print elist

# import copy
# alist = [[0]]
# blist = [copy.copy(alist) for i in range(3)]
# clist = [alist for i in range(3)]
# dlist = [[[0]] for i in range(3)]
# elist = [copy.deepcopy(alist) for i in range(3)]
# print([id(i) for i in blist])
# print([id(i) for i in clist])
# print([id(i) for i in dlist])
# print([id(i) for i in elist])
# print([id(i[0]) for i in blist])
# print([id(i[0]) for i in clist])
# print([id(i[0]) for i in dlist])
# print([id(i[0]) for i in elist])

# aset=set('translation')
# print aset
# bset=set('smiles')
# print bset
#
# print aset^bset
# print aset-bset
# print bset-aset
# print aset|bset
#
# adict={'pear':1.5,'banana':2.5}
# print adict.items()
# print adict['pear']
#
# print adict.get('banana')
#
# for i in adict:
#     print i,adict[i]
#
# if 'banana' in adict:
#     adict['banana']=adict['banana']+1
# else:
#     adict['banana']=3
#
# print adict
#
# adict.setdefault('apple',5)
# print adict
#
# adict.setdefault('tamato','5')
# print adict
#
# astr='9 0 10 2 3 4'
# alist=[float(i) for i in astr.split()]
# blist=sorted(alist)[1:-1]
# sum(blist)/len(blist)
#
# [random.choice([1,5,6,7]) for i in range(1000)].count(1)
#
# [i for i in range[50] if i%3==0]


# astr='abddaaefaegesge'
# aset=set(astr)
# print {k:astr.count(k) for k in aset}
# #循环不重复字符次数
#
# adict={}
# for i in astr:
#     if i in adict:
#         adict[i]+=1
#     else:
#         adict[i]=1
# print adict
# #循环1次
#
# adict={}
# for i in astr:
#     adict[i]=adict.get(i,0)+1
# print adict
# #循环1次
#
# adict={}
# for i in astr:
#     adict.setdefault(i,0)
#     adict[i]+=1
# print adict
# #循环1次
#
# print Counter(astr)
#
# import sys
# print sys.argv[1:]
#
# print sum(float(i)  for i in sys.argv[1:])

for line in open(r'exec.md'):
    if line.strip():
        print line.rstrip('\n')

afile=open(r'test.txt','w')
afile.write('test\n')
afile.close()

afile=open(r'test.txt','a')
afile.writelines('test1')
afile.close()
