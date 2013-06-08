#!/usr/bin/env python

def jiechen(num):
    if num > 1:
        return reduce(lambda x,y:x*y,range(1,num+1))
    else:
        return 1

n=3
total=0
while True:
     if n == sum(jiechen(int(i)) for i in str(n)):
        total += n
        print total
     n += 1
