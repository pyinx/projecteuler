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

result = 0
for i in range(2,10):
    tmp = ''.join(str(n) for n in range(1, i+1))
    for num in itertools.permutations(tmp, i):
        num = int(''.join(num))
        if is_prime(num):
            print num
            if num > result:
                result = num
print result

