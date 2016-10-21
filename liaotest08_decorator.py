#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('calling %s():' %func.__name__)
        return func(*args, **kw) #执行一下函数func并返回
    return wrapper
	
@log
def now():
    print('2016-09-02')

now()
print(now.__name__)
