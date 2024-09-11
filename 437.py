from itertools import permutations, count


def LIS(bloques: list):
    dp = [0] * len(bloques) 
    for i, bloque in enumerate(bloques):
        dp[i] = bloque[-1]
        for j in range(i):
            if (bloque[0] > bloques[j][0] and bloque[1] > bloques[j][1] and dp[j] + bloque[-1] > dp[i]):
                dp[i] = dp[j] + bloque[-1]
  
    return max(dp)

def main():
    for case in count(1):
        bloques = []
        n = int(input("ingresa el numero de tipo de bloques : "))
        if n == 0:
            break
        print ("ingresa los bloques: ")
        for _ in range(n):
            bloques.extend(permutations(map(int, input().split())))
        
        bloques.sort()
    
    
        print(f"Caso {case}: altura maxima = {LIS(bloques)}")
    
if __name__ == "__main__":
    main()

    
"""
# -- Sección de Explicación --
# – Su solución es BU o TP:
#   Esta solución es una **solución de arriba hacia abajo(Top-down, TP)**. 
#   Usa el recurso de memorizacion,alamcenando en arrglos las soluciones pasadas, para llegar a la final 


# – Complejidad espacial y temporal:
#   - Complejidad temporal: **O(6n^2 )**, donde `n` es el número de tipos de bloques
#
#   - Complejidad espacial: **O( 6n  )**. La memoria usada para almacenar el resultado de LIS

# – Estrategia de la solución:
     Se utilizo el algoritmo LIS para encontrar la subsecuencia mas larga entre los bloques, comparando las bases y sumando a la lista la altura de cada bloque seleccionado
     de igual forma se utilizo la herramienta permutations dentro de la libreria intertools para realizar las posibles posiciones que puede tomar cada bloque 
# – Uso de Memoización:
#   la solucion reserva un arreglo principal donde se agregan las alturas de las subseciencias, destacando a la mas grande

"""