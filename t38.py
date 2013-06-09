#!/usr/bin/env python

num = 2
result = 0
while True:
    tmp = ''
    for i in range(1,10):
        if len(tmp) >= 9:
            break
        else:
            tmp += str(num * i)
    if '0' not in set(tmp):
        if len(tmp) == len(set(tmp)):
            result = int(tmp) if int(tmp) > result else result
            print result
    num += 1
