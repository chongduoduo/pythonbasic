# -*-coding:utf-8 -*-
##for yield research

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b  #b值赋给a, a+b值赋给b
        n = n + 1

fab(8)