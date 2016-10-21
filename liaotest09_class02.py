#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Screen(object):
    
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int,float)):
            raise ValueError('width must be a number!')
        if value < 0:
            raise ValueError ('width must be positive!')
	
    @property
    def height(self):
        return self._height
	
    @height.setter
    def height(self, value):
        if not isinstance(value, (int,float)):
            raise ValueError('height must be a number!')
        if value < 0:
            raise ValueError ('height must be positive!')
			
    @property
    def resolution(self):
        return self._width * self._height

#a = Screen(50, 100)
#print(a.resolution)