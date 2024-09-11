def diving_gold(t, w, tesoros):
    
    matriz = [[0 for _ in range(t+1)] for _ in range(len(tesoros)+1)]
    dic = {}  # Diccionario para guardar los tesoros seleccionados en cada combinación

    for i in range(1, len(tesoros) + 1):
        for j in range(1, t + 1):
            td = w * tesoros[i-1][0]  # Tiempo de descenso
            ta = 2 * w * tesoros[i-1][0]  # Tiempo de ascenso
            totalt = td + ta  # Tiempo total para obtener el tesoro

            if totalt <= j:
                # Comparamos si es mejor tomar o no el tesoro
                A = tesoros[i-1][1] + matriz[i-1][j-totalt]
                B = matriz[i-1][j]
                if A > B:
                    dic[(i, j)] = [tesoros[i-1]]
                    if (i-1, j-totalt) in dic:
                        for te in dic[(i-1, j-totalt)]:
                            dic[(i, j)].append(te)
                    matriz[i][j] = A
                else:
                    matriz[i][j] = B
                    dic[(i, j)] = dic[(i-1, j)]
            else:
                matriz[i][j] = matriz[i-1][j]

    valor_mas_alto = matriz[len(tesoros)][t]
    tesoros_finales = dic[(len(tesoros), t)]
    return valor_mas_alto, tesoros_finales


def main():
    # Leer tiempo de buceo disponible (t) y coeficiente de profundidad (w)
    t, w = map(int, input().strip().split())

    # Leer número de tesoros disponibles
    n = int(input().strip())

    # Leer los tesoros: (profundidad, valor del oro)
    tesoros = []
    for _ in range(n):
        d, v = map(int, input().strip().split())
        tesoros.append((d, v))

    # Llamar a la función para obtener el máximo valor y los tesoros seleccionados
    valor_mas_alto, tesoros_finales = diving_gold(t, w, tesoros)

    # Imprimir el resultado
    print("\nOutput: ")
    print(valor_mas_alto)  # Imprimir el valor máximo obtenido
    print(len(tesoros_finales))  # Imprimir la cantidad de tesoros seleccionados
    for tesoro in tesoros_finales:
        print(tesoro[0], tesoro[1])  # Imprimir profundidad y valor de cada tesoro seleccionado


if __name__ == "__main__":
    main()

"""
    Solución basada en el problema de la mochila (Knapsack Problem) utilizando programación dinámica.

    Estrategia:
    - Se utiliza un enfoque **Bottom-Up (BU)** con programación dinámica. Se construye una matriz que representa
      las decisiones sobre si se toma o no un tesoro, basado en el tiempo disponible y el valor que puede generar.
    
    Complejidad:
    - **Complejidad temporal**: O(n * t), donde `n` es el número de tesoros y `t` es el tiempo máximo de buceo.
    - **Complejidad espacial**: O(n * t), ya que la matriz almacena los subproblemas correspondientes a cada tesoro y el tiempo.

    Estrategia de la solución:
    - Se crea una tabla que almacena el valor máximo de oro que se puede obtener para cada combinación de tesoros y tiempo.
    - Se actualiza la tabla para cada tesoro, sumando el tiempo necesario para sumergirse y volver a la superficie.
    - Se elige si tomar o no un tesoro en función de maximizar el oro acumulado dentro del tiempo permitido.

    Uso de Memoización:
    - Se utiliza memoización implícita a través de la matriz `matriz[i][j]`, que guarda el valor máximo de oro alcanzable
      con los primeros `i` tesoros y `j` unidades de tiempo. Esto evita recalcular subproblemas ya resueltos.
    """
