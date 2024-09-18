import sys

def solve_case(n, train):
    """
    Función que resuelve cada caso individualmente.
    Recibe:
    - n: número de vagones.
    - train: lista con los pesos de los vagones, donde ya está reflejada en orden inverso.
    
    Devuelve:
    - El tamaño de la subsecuencia más larga (LIS) que se puede formar.
    """
    lis = []
    if n > 0:
        lis.append(train[0])  # Inicializamos la subsecuencia con el primer valor

    # Vamos a iterar sobre los 2n elementos para manejar las dos mitades (original e invertida)
    for i in range(1, 2 * n):
        if train[i] > lis[-1]:  # Si el valor es mayor que el último en la subsecuencia
            lis.append(train[i])  # Extendemos la subsecuencia
        else:
            # Usamos búsqueda binaria para encontrar la posición donde debe ir el valor
            index = lower_bound(lis, train[i])
            lis[index] = train[i]  # Reemplazamos en la posición correcta para mantener la subsecuencia

    return len(lis)

def lower_bound(lis, value):
    """
    Encuentra la posición donde debería insertarse el valor en la lista 'lis' usando búsqueda binaria.
    """
    low, high = 0, len(lis)
    while low < high:
        mid = (low + high) // 2
        if lis[mid] < value:
            low = mid + 1
        else:
            high = mid
    return low

def main(input_source=sys.stdin, output_dest=sys.stdout):
    """
    La función principal del programa que organiza los casos de prueba, lee la entrada, y llama a la
    función que resuelve cada caso individualmente.
    """
    # Leer el número de casos de prueba
    case = int(input_source.readline().strip())
    
    while case > 0:
        n = int(input_source.readline().strip())  # Leer el número de vagones
        train = [0] * (2 * n)
        
        # Lectura de los valores y construcción de la lista "train"
        for i in range(n):
            train[i + n] = int(input_source.readline().strip())  # Leer los pesos
            train[n - i - 1] = train[i + n]  # Reflejar la lista de manera inversa
        
        # Llamamos a la función que resuelve el caso y obtenemos el resultado
        result = solve_case(n, train)
        
        # Escribimos el resultado
        output_dest.write(f"{result}\n")
        
        # Disminuimos el número de casos restantes
        case -= 1

if __name__ == "__main__":
    # Si hay argumentos de archivo, los usa. Si no, usa consola.
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as input_file:
            if len(sys.argv) > 2:
                with open(sys.argv[2], 'w') as output_file:
                    main(input_source=input_file, output_dest=output_file)
            else:
                main(input_source=input_file)
    else:
        main()  # Usa la entrada y salida estándar (consola)

"""
Respuestas a las preguntas:

1. **¿La solución es Bottom-Up (BU) o Top-Down (TP)?**
   - La solución es **Bottom-Up (BU)**. Empezamos desde los vagones más pequeños y vamos construyendo la subsecuencia más larga posible, utilizando la información previa para extenderla paso a paso.

2. **Complejidad temporal y espacial:**
   - **Temporal:** \(O(n \log n)\). Esto se debe a que, para cada vagón, realizamos una búsqueda binaria (usando la función `lower_bound`), que tiene un costo de \(O(\log n)\) para cada uno de los \(n\) elementos. La búsqueda binaria optimiza la inserción en la subsecuencia.
   - **Espacial:** \(O(n)\). Solo necesitamos un array de tamaño \(n\) para mantener la subsecuencia más larga (LIS), además del array `train` que tiene longitud \(2n\) para manejar las dos mitades de la lista original (orden directo e invertido).

3. **Explicación de la estrategia de la solución:**
   - La estrategia utilizada es una combinación de la **Subsecuencia más larga creciente (LIS)** y la **Subsecuencia decreciente más larga (LDS)**. Para cada vagón, decidimos si lo colocamos al principio o al final del tren. El objetivo es maximizar la longitud del tren con los vagones ordenados de manera decreciente por peso.
   - **Memoización:** La memoización está presente implícitamente en el uso del array `lis`, donde almacenamos los resultados parciales de la subsecuencia más larga. Esto evita que tengamos que recalcular desde el principio en cada paso, lo que mejora la eficiencia del algoritmo.
"""
