num=2
step=num*2  ######
total=0
l=[]
for x in range(num+1):
    tmp=[]
    for y in range(num+1):
        tmp.append([x,y])
    l.append(tmp)
for i in l:
    print i

start=[0,0]
end=[num,num]

#for i in range(1,step):
#    tmp_list=[[0,0]]
    
