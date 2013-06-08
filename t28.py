# -*- coding: utf-8 -*-
num=1001   ####矩阵宽度
total=1
n=1
end=1 ####end值为每圈的最后一个值
while True:
    l=[end+i*n*2 for i in range(1,5)]   #####公式为:end + i*n*2
    total += sum(l)
    end=l[-1]
    if n*2+1 == num:
        print total
        break
    else:
        n += 1     
    
