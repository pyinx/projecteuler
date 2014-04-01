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
if num == '1':
    print 1
    sys.exit(0)
else:
    num = int(num) + 1
#######生成三维字典
#d[x][y] = num  ###x为横坐标,y为纵坐标,num为坐标上的值
'''
       (0,1)
         |
(-1,0)———————— (1,0)
         |
       (0,-1)
'''
d = {}
for i in range(num/2):
    d[i] = {}
    d[i][i] = {}
    d[i][-i] = {}
    d[-i] = {}
    d[-i][i] = {}
    d[-i][-i] = {}
######按坐标插入数据到字典
for i in range(1,num/2+1):
    if i == 1:
        end = 1
        d[0][0] = end
        x,y=1,0
    else:
        for a in range((i-1)*2):
            end += 1
            d[x][y+a] = end
            #print 'd[%d][%d] = %d' % (x,y+a,end)
        for b in range((i-1)*2):
            end += 1
            d[x-b-1][y+a] = end
            #print 'd[%d][%d] = %d' % (x-b-1,y+a,end)
        for c in range((i-1)*2):
            end += 1
            d[x-b-1][y+a-c-1] = end
            #print 'd[%d][%d] = %d' % (x-b-1,y+a-c-1,end)
        for e in range((i-1)*2):
            end += 1
            d[x-b+e][y+a-c-1] = end
            #print 'd[%d][%d] = %d' % (x-b+e,y+a-c-1,end)
        x,y = x-b+e+1,y+a-c-1

#####根据坐标取数
for y in range(-num/2+1,num/2):
    for x in range(-num/2+1,num/2):
        print d[x][-y],
    print
