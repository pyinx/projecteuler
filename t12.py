length=500
num=2
while True:
    n=sum(i for i in range(num))
    l=[i for i in range(1,n+1) if n % i == 0]
    if len(l) > length:
        print n
        break
    num += 1
