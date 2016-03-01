# -*- coding: utf-8 -*-
from urllib.request import urlopen

f = urlopen('http://qitta.com/advent-calendar/2014')

print (f.code)

headers = f.getheader('content-type')
print (headers)

print (f.info().get_content_charset())

print (f.read())