x=600851475143
l=[]
while x > 1 :
    for i in xrange(2,100000000):
        if divmod(x,i)[1] == 0:
            x=divmod(x,i)[0]
            l.append(i)
            break
print max(l)
