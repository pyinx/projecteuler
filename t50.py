#!/usr/bin/env python
import itertools

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
tmp = []
for i in range(1,100):
    if is_prime(i):
        if len(str(i)) >= 2:
            for n in range(len(tmp), 0, -1):
                nums = 0
                for num in itertools.permutations(tmp, n+1):
                    if sum(num) == i:
                        nums = n
                if nums != 0:
                    print i,nums
                    break
        tmp.append(i)
        print tmp
        
