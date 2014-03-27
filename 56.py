#!/usr/bin/env pyton
# -*- coding: utf-8 -*-
'''
幂方数字和
古戈尔 (10^100)是一个天文数字：1后面跟着100个零；100^100更是不可想象的大:1后面跟着200个零。尽管它们非常大，但是它们的数字和为1.
求幂方a^b中，a,b < 100,最大的数字和
'''

#map(lmabda x,y:pow(x,y),range(5) range(4))
result = 0
for x in range(1,100):
    for y in range(1,100):
        tmp = sum(int(i) for i in str(pow(x,y)))
        if tmp > result:
            result = tmp
print result
