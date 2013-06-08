#!/usr/bin/env python
x=1
y=1
z=x+y
total=0
while z < 4000000:
    total += z
    x=y+z
    y=x+z
    z=x+y
else:
    print total
