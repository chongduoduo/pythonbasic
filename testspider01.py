#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import sys
import urllib2

#reload(sys)
#sys.setdefaultencoding('gbk')

response = urllib2.urlopen("https://www.zhihu.com")
print response.read()
