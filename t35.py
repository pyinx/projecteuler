#!/usr/bin/env python

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
    count = 0
    for i in xrange(2,1000000):
        if is_prime(i):
            if len(str(i)) == 1:
                count += 1
            else:
                i = str(i)
                tmp = 1
                for x in range(len(i) - 1):
                    i = i[1:] + i[0]
                    if is_prime(int(i)):
                        tmp += 1
                if tmp == len(i):
                    count += 1

print count
