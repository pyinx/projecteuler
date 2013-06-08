n=2
total=0
while True:
    s=sum(int(i)**5 for i in str(n))
    if n == s:
        total += n
        print total
    n += 1
