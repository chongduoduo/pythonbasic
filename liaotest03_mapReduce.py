
# -*- coding: utf-8 -*-
from functools import reduce

###test01###
def normalize(name):
    return name.title()
	
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

###test02###
def prod(L):
    def mul(x,y):
        ##print (x*y)
        return x*y 
    return reduce(mul,L)

##测试##
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

###test03###
def str2float(s):
    def fn(x, y):
        if y==0:
            return x
        else:
            return x*10+y
    def char2num(c):
        if c == '.':
            return 0
        else:
            return int(c)
    a=reduce(fn,map(char2num,s))

    #print(len(s)-s.find('.')-1)
    #print (pow(10,(len(s)-s.find('.')-1)))
    return a/pow(10,(len(s)-s.find('.')-1))

print('str2float(\'123.456\') =', str2float('12345.4563'))

	