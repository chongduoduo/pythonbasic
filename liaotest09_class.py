#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Computer(object):

    def __init__(self, owner, brand, SN): #初始化
        self.__owner = owner
        self.__brand = brand
        self.__SerialNum = SN

    def get_info(self):
	    return self.__owner, self.__brand, self.__SerialNum

    def set_owner(self, owner):
        self.__owner = owner


PC1=Computer('Jone', 'Dell', '1X867339F3')
print(PC1.get_info())
	