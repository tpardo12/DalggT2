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




def main():
    misiles = list(map(int, input("ingresa los misiles: ").strip().split()))
    m = LIS(misiles)[0]
    print(LIS(misiles)[0], "misiles destruidos: " )
    return None


if __name__ == "__main__":
    main()
"""
# -- Sección de Explicación --
# – Su solución es BU o TP:
#   Esta solución es una **solución de arriba hacia abajo(Top-down, TP)**. 
#   Usa el recurso de memorizacion,alamcenando en arrglos las soluciones pasadas, para llegar a la final 


# – Complejidad espacial y temporal:
#   - Complejidad temporal: **O(n^2 )**, donde `n` es el número de misiles 
#
#   - Complejidad espacial: **O( n  )**. La memoria usada para almacenar el resultado de LIS

# – Estrategia de la solución:
     Se utilizo el algoritmo LIS para encontrar la subsecuencia mas larga necesaria para determinar que misiles se destruiran
# – Uso de Memoización:
#   la solucion reserva un arreglo principal donde se agregan las subsecuencias de los misilies que posterior mente se seleccionara la mas larga para indicar el resultado

"""