#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

num = sys.argv[1]
if not num.isdigit():
    raise TypeError('must be a number')
    sys.exit(255)
if int(num) % 2 == 0:
    raise TypeError('must be a odd number')
    sys.exit(255)
if num == '0':
    print ''
elif num == '1':
    print 1
else:
    start = 1
    num = int(num)+1
    for i in xrange(1,num,2):
        if i == 1:
            print i
        else:
            length = 4*i - 4
            tmp = [x + start for x in range(1, length + 1)]
            start = tmp[-1]
            print tmp

