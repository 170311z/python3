# -*- codeing: utf-8 -*-

import requests

r = requests.get('http://qitta.com/advent-calender/2014')

print (r.status_code)

print (r.encoding)

print (r.text)