def f(n):
    count=1
    while n != 1:
        if n % 2 == 0:
            n = n/2
            count += 1
        else:
            n = 3*n+1
            count += 1
    return count

max_len=0
for num in range(1,1000000):
    tmp=f(num)
    if max_len < tmp:
        max_len = tmp
        max_num = num
print max_num
