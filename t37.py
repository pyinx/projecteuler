#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == '__main__':
    n = 0     ######计数器
    num = 10  ######从两位数开始 
    total = 0
    while n < 11:
        if is_prime(num):
            tmp1 = tmp2 = 0
            for x in xrange(1, len(str(num))):
                if is_prime(int(str(num)[x:])):
                    tmp1 += 1
            for x in xrange(len(str(num))-1, 0, -1):
                if is_prime(int(str(num)[:x])):
                    tmp2 += 1
            if tmp1 == tmp2 == len(str(num)) - 1:
                total += num
                n += 1
        num += 1
    print total
