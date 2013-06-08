#x=2520
#while True:
#    a=[x%i for i in range(2,21)]
#    if list(set(a)) == [0]:
#        break
#    else:
#        x += 1
#print x
#    else:
x=reduce(lambda x,y:x*y,range(1,21))
y=3*5*11*13*17*19
while x > y:
    for i in xrange(1,1000):
        a=[x%i for i in range(2,21)]
        if list(set(a)) == [0]:
            print i
            x /= i
            break
else:
    print x
    
