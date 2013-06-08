x=sum(i**2 for i in range(1,101))
y=pow(reduce(lambda x,y:x+y,range(1,101)),2)
print y-x
