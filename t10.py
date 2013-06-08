#!/usr/bin/env python  
#coding=utf-8  
  
sum = 2  
def is_prime(num):  
    i = 2  
    while i**2 <= num:  
        if num%i == 0:  
            return False  
        i += 1  
    return True  
  
for i in xrange(3,2000000,2):  
    if is_prime(i):  
        sum += i  
  
print sum 
