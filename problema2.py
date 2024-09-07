def coinlimited(amount, coins, limits):
    
    
    # Matriz para almacenar cuántas monedas de cada denominación se usan
    coins_used = [[0] * len(coins) for _ in range(amount + 1)]
    
    # Lista para almacenar el número mínimo de monedas necesarias para cada cantidad
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Para el valor 0, se necesitan 0 monedas
    
    # Crear una copia de los límites
    limits_copy = limits[:]
    
    # Recorrer las monedas
    for i in range(len(coins)):
        while limits_copy[i] > 0:
            for j in range(amount, -1, -1):
                curr_amount = j + coins[i]
                if curr_amount <= amount:
                    if min_coins[curr_amount] > min_coins[j] + 1:
                        min_coins[curr_amount] = min_coins[j] + 1
                        coins_used[curr_amount] = coins_used[j][:]  # Copiar el array
                        coins_used[curr_amount][i] += 1

            limits_copy[i] -= 1
    
    # Verificar si no se pudo hacer el cambio exacto
    if min_coins[amount] == float('inf'):
        return None
    
    # Devolver la cantidad mínima de monedas y el desglose de monedas usadas
    return min_coins[amount]


def coinChange(amount):
    coins = [5, 10, 20, 50,100,200]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    n = 0

    for c in coins:
        for i in range(c, amount + 1):
            if dp[i - c] != float('inf'):
                dp[i] = min(dp[i], 1 + dp[i - c])
                
    if (dp[amount] == 'inf'):
        n = -1 
    else:
        n = dp[amount]
    return n






def coinsf (limits, amount):
    amount = int(amount *100)
    coins = [5, 10, 20, 50,100,200]
    maxamount = limits[0] * 5 + limits[1]*10 + limits[2]*20 + limits[3]*50 + limits[4]*100 + limits[5]*200
    
    dp = [0] * ( maxamount +1 ) 
    dq = [0] * ( maxamount +1 ) 
    tot = [0] * ( maxamount +1 ) 
   
    
    for i in range(amount , maxamount +1, 5):
        dp[i] = coinlimited(i, coins, limits)
        res = i - amount
        dq[i] = coinChange(res)

        

    
    for j in range(amount , maxamount +1, 5):
        if dp[j] != None:
            tot [j] = dp[j] + dq[j]
        else:
            tot [j] =  0
    
    tot = tot[amount:]
    min = 0
    for k in tot:
        if k != 0:
           if min == 0:
               min = k
           elif k < min:
               min = k
    print (min)
            
# Ejemplo de uso
amount = 2.70
limits = [7, 8, 2,7,0,9]
   
        
coinsf(limits, amount)


