def costoMin(n, cuts):
    # Ordenamos los cortes y agregamos los límites del palo (0 y n)
    cuts.sort()
    cuts = [0] + cuts + [n]
    
    # Número total de cortes (incluyendo 0 y n)
    m = len(cuts)

    # Creamos una tabla dp para almacenar los costos mínimos
    dp = [[0] * m for _ in range(m)]
    
    # Llenamos la tabla dp de abajo hacia arriba
    # Intervalos cortos primero y luego intervalos más largos
    for length in range(2, m):  # Longitud del intervalo que estamos evaluando
        for i in range(m - length):  # Punto inicial del intervalo
            j = i + length  # Punto final del intervalo
            dp[i][j] = float('inf')  # Inicializamos el costo como infinito
            # Probamos todos los posibles cortes entre i y j
            for k in range(i + 1, j):
                # El costo de cortar en k más los subcostos
                cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
                dp[i][j] = min(dp[i][j], cost)
    
    # El resultado final estará en dp[0][m-1], que es el costo mínimo para todo el palo
    return dp[0][m - 1]

if __name__ == "__main__":
    while True:
        l = int(input())  # Longitud del palo
        if l == 0:  # Caso de finalización
            break
        n = int(input())  # Número de cortes
        cuts = list(map(int, input().split()))  # Posiciones de los cortes
        result = costoMin(l, cuts)
        print(f"El costo minimo es de {result}.")


"""
Explicación del enfoque:

– La solución es **Bottom-Up (BU)**. Se construye la solución a partir de subproblemas más pequeños (cortes entre segmentos pequeños) y se expande hasta encontrar el costo mínimo de cortar todo el palo.
– Complejidad Temporal: O(m^3) donde m es el número total de cortes (incluyendo los extremos 0 y n). La complejidad se deriva del triple bucle: un bucle para el tamaño del intervalo, otro para el inicio del intervalo, y el tercero para iterar sobre las posibles posiciones de los cortes dentro de ese intervalo.
– Complejidad Espacial: O(m^2), ya que necesitamos una tabla dp de tamaño m × m para almacenar los costos mínimos de cortar entre diferentes posiciones.
– Estrategia: Se utiliza programación dinámica (DP) para calcular los costos mínimos de cortar el palo en diferentes subsegmentos. Usamos una tabla `dp[i][j]` donde almacenamos el costo mínimo de cortar el palo entre las posiciones `cuts[i]` y `cuts[j]`. Al llenar la tabla de forma iterativa, podemos calcular la solución óptima para el palo completo.
– **Memoización**: En esta solución no usamos memoización explícita (como en el enfoque recursivo con memoización). En su lugar, almacenamos todos los subproblemas en una tabla `dp` que es consultada iterativamente, lo que evita recalcular los costos para los mismos intervalos, lo que es análogo a memoización en este contexto.
"""
