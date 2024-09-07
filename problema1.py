def change(amount, cur):
    
    prev = [0] * (amount + 1)
    prev[0] = 1
    for i in range(1, amount + 1):
        
        if ( i < cur[0]):
            prev[i] = 0
        else:
            prev[i]  = prev[i - cur[0]]
        
        
        
    for j in range(1, len(cur)):
        
        next = [0] * (amount + 1)
        next[0] = 1

        
        for i in range(1, amount + 1):
           
            if ( i < cur[j]):
                next[i] = prev[i]
            else:
                next[i] =  prev[i] + next[i - cur[j]]
       
        prev = next
        

    return prev[amount]



def  tocents( amount):
    amount = amount *100
    cur = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]  
    return change (int(amount) , cur)

print(tocents(0.20))