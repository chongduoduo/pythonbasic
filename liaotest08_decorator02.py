#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('Begin call %s:' %func.__name__)
        f=func(*args, **kw) #func(*args, **kw)是执行func，等于25，然后把25赋值给f. 这句话执行了func函数。
        print('End call %s' %func.__name__)
        return(f) #把执行func好的结果返回
    return wrapper

@log
def mul(n):
    print ("executing")   
    return n*n; 

mul(5)
#print(mul.__name__)
