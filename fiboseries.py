def FibSer(num):
    f=[]
    f.append(0)
    f.append(1)
    for i in range(2,num):
        f.append(f[i-1]+f[i-2])
    return(f[num-1])
print(FibSer(9)) 
