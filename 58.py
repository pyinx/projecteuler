#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import sys

'''
螺旋素数
从1开始以如下方式逆时针螺旋，可以得到一个大小为7的螺旋方块
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
有趣的是奇数的平方都在对角线的右下角，更有趣的是，13个位于对角线的数中，有8个是素数；比率是8/13 约等于 62%。
如果像上面的螺旋那样再加一层螺旋，将得到一个大小为9的螺旋方块。如果这个步骤一直持续下去，当螺旋方块的大小为多少时，对角线上的素数比率会小于10%？
'''

def isPrime(n):  
    if n <= 1:  
        return False 
    i = 2 
    while i*i <= n:  
        if n % i == 0:  
            return False 
        i += 1 
    return True

start = 1
l1 = [1,]
l2 = []
for i in xrange(3,1000000,2):
    # 2*(i + i - 2) == 4*i - 4
    length = 4*i - 4
    tmp = [x + start for x in range(1, length + 1)]
    for x in range(4): ###4个角
        num = tmp[(i-2) + (i-1)*x]
        if isPrime(num):
            l2.append(num)
        l1.append(num)
    start = tmp[-1]
    if len(l2)/len(l1) < 0.10: #####小于10%
        print i
        sys.exit()
