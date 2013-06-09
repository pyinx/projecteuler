#!/usr/bin/env python

dic = {}
for i in range(12, 1001):  ######min 3+4+5=12
    dic[i] = 0
    for x in range(1,i):
        for y in range(x, i):
            for z in range(y, i):
                if x**2 + y**2 == z**2:
                    if x + y + z == i:
                        dic[i] += 1
                        print '%d: %d %d %d' % (i, x, y, z)

max_len = 0
for i in dic:
    max_len = dic[i] if dic[i] > max_len else max_len
    if dic[i] > nax_len:
        max_len = dic[i]
        value = i
print value
