#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
利克瑞尔数
如果我们取47，将它逆序并求和，47 + 74 = 121，是一个回文数。
并不是所有的数都可以这么快产生回文数。例如
349 + 943 = 1292，
1292 + 2921 = 4213
4213 + 3124 = 7337
也就是说，349用了3次迭代得到一个回文数。
虽然至今没有人证明，但是有猜想认为一些数，如196，永远不产生回文数。一个数通过逆序和迭代如果永远不产生回文数则称为利克瑞尔数。因为这些数的理论本质以及方便这个问题的目的，我们假设一个数是利克瑞尔数，直到证明不是。另外，对于每个小于10000的数，给定两种可能，它或者是(i)在小于50次迭代变成循环数(ii)没有一个人，在有限的计算能力下，能够将它迭代到一个回文数。事实上，10677是第一个超过50次迭代产生回文数：4668731596684224866951378664(53次迭代，28位数)
令人惊奇的是，有一些回文数自身也是利克瑞尔数，第一个例子是4994.
求10000以下一共有多少个利克瑞尔数？
'''

def Palindrome(tmp):
    if len(str(tmp)) % 2 == 0:
        n1 = str(tmp)[:divmod(len(str(tmp)),2)[0]]
        n2 = str(tmp)[divmod(len(str(tmp)),2)[0]:]
    else:
        n1 = str(tmp)[:divmod(len(str(tmp)),2)[0]]
        n2 = str(tmp)[divmod(len(str(tmp)),2)[0]+1:]
    if str(n1) == str(n2)[::-1]:
        return True
    else:
        return False

def  Lychrel(num):
    tmp = num + int(str(num)[::-1])
    count = 1
    while count < 50:
        if Palindrome(tmp):
            return False
            break
        tmp = tmp + int(str(tmp)[::-1])
        count += 1
    else:
        return True

if __name__ == '__main__':
    total = 0
    for i in range(10000):
        if Lychrel(i):
            total += 1
    print total
