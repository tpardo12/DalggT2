def division_monedas(lista_monedas):
    """
    Esta función toma como parámetros una lista de monedas para cada ejercicio (lista_monedas).

    Args:
      lista_monedas: Una lista de listas, donde cada sublista contiene las monedas de un ejercicio.

    Returns:
      resultados: Una lista con la diferencia mínima para cada ejercicio.
    """
    resultados = []
    # Recorremos la lista de monedas
    for monedas in lista_monedas:
        # Primero calculamos la mitad de la suma de las monedas en la lista.
        suma_monedas = sum(monedas)
        mitad_suma = suma_monedas // 2

        # Matriz para hacer programación dinámica
        matriz = [False] * (mitad_suma + 1)  # si el valor [i] es igual a False, entonces i no se puede sumar con valores de las monedas
        matriz[0] = True  # porque el valor 0 se puede hacer siempre sin agregar ninguna moneda.

        for moneda in monedas:
            for j in range(mitad_suma, moneda - 1, -1):
                matriz[j] = matriz[j] or matriz[j - moneda]

        # Encontramos el valor mayor que se puede encontrar con las monedas hasta la mitad de la suma
        for j in range(mitad_suma, -1, -1):
            if matriz[j]:
                maximo = j
                break

        # Encontrar diferencia mínima
        dif_min = suma_monedas - 2 * maximo
        resultados.append(dif_min)

    return resultados

# Función principal que usa entrada estándar (stdin) y salida estándar (stdout)
def main():
    # Leer la cantidad de problemas (n) de la primera línea
    n = int(input().strip())

    lista_monedas = []

    # Leer los problemas
    for _ in range(n):
        m = int(input().strip())  # Leer la cantidad de monedas en este ejercicio
        monedas = list(map(int, input().strip().split()))  # Leer las monedas
        if len(monedas) != m:
            print(f"Error: La cantidad de monedas no coincide con el número dado.")
            return
        lista_monedas.append(monedas)

    # Llamar a la función division_monedas
    resultados = division_monedas(lista_monedas)
    print("Resultado: ")
    # Imprimir los resultados en salida estándar
    for resultado in resultados:
        
        print(resultado)

# Ejecutar el programa
if __name__ == "__main__":
    main()




# -- Sección de Explicación --
# – Su solución es BU o TP:
#   Esta solución es una **solución de abajo hacia arriba (Bottom-Up, BU)**. 
#   En lugar de resolver el problema principal directamente, primero resuelve subproblemas más pequeños, 
#   utilizando programación dinámica para construir la solución completa. 
#   Esto contrasta con la estrategia "Top-Down" (TP), que utilizaría recursión con memoización.

# – Complejidad espacial y temporal:
#   - Complejidad temporal: **O(n * m * mitad_suma)**, donde `n` es el número de problemas, `m` es el número de monedas en cada problema,
#     y `mitad_suma` es la mitad de la suma total de las monedas en el peor caso.
#     Cada problema se resuelve procesando cada moneda, y para cada moneda, se actualizan todas las posibles sumas hasta `mitad_suma`.
#     En el peor de los casos, esto es proporcional al número de monedas multiplicado por la mitad de la suma.
#
#   - Complejidad espacial: **O(mitad_suma)**. La memoria usada para almacenar los posibles valores de suma en el array `matriz`
#     depende de `mitad_suma`, que es la mitad de la suma total de las monedas en cada problema. El espacio para la matriz es
#     lineal en relación a `mitad_suma`.

# – Estrategia de la solución:
#   La estrategia se basa en programación dinámica. Se utiliza una matriz `matriz[j]` que indica si es posible lograr una suma
#   `j` con las monedas disponibles. La matriz se actualiza para cada moneda, revisando las posibles sumas de `mitad_suma` hacia 0 
#   (esto asegura que no se reutilicen monedas de manera indebida).
#   
#   Luego, el algoritmo busca el valor máximo que se puede obtener en la primera mitad (`mitad_suma`) que representa la suma más cercana
#   a la mitad del total de monedas. La diferencia mínima entre las dos particiones se calcula como la diferencia entre la suma total
#   y dos veces la suma más cercana que se puede obtener.

# – Uso de Memoización:
#   Aunque la solución no usa memoización en el sentido clásico (como en una solución Top-Down), hace uso de una forma de memoización implícita
#   mediante el almacenamiento de resultados intermedios en la matriz `matriz`. Cada vez que se procesa una moneda, los resultados de subproblemas
#   (las posibles sumas de monedas) se almacenan en la matriz y se reutilizan para evitar el cálculo redundante. Esto es clave para reducir
#   la complejidad temporal de la solución.
