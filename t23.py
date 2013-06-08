x=1
y=1
num=2
while True:
    z = x + y
    num += 1
    if len(str(z)) > 999:
        print num
        break
    x = z + y
    num += 1
    if len(str(x)) > 999:
        print num
        break
    y = z + x
    num += 1
    if len(str(y)) > 999:
        print num
        break
