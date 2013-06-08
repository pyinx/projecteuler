import string
s=string.ascii_uppercase

f=open('names.txt').readline().split(',')
f.sort()
total=0
for i in range(len(f)):
    tmp=sum(s.index(x) + 1 for x in f[i].replace('"',''))
    total += tmp * (i+1)
print total
