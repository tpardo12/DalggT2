def LIS (misiles):
    
    f = [[] for _ in range(len(misiles))]
    
    
    f[0].append(misiles[0])
    for i in range (1,len(misiles)):
        lis = 1
        for j in range(i):
            if (misiles[i] > misiles[j]) and (lis < len(f[j]) +1 ):
                
                f[i] = f[j][:]
                lis = len(f[j]) + 1 
        f[i].append( misiles[i])
                
   
    x = 0     
    destruidos = []
    
    for i in f:
        if len(i) > x:
            x = len(i)
            destruidos = i
    
    return(destruidos, len(destruidos))


print(LIS([2,100,3,101,4,5,6,7]))