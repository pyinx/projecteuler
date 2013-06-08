l=[]
n=2
while True:
    tmp=[i for i in range(1,n/2+1) if n%i==0]
    if len(tmp) == 1:
        l.append(n)
    n+=1
    if len(l) == 10001:
        break
print l[-1]
