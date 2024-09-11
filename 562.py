import argparse
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

def leer_desde_consola():
    """
    Lee la entrada desde la consola para obtener los datos de los ejercicios.
    """
    n = int(input().strip())  # Leer el número de ejercicios
    lista_monedas = []

    for _ in range(n):
        m = int(input().strip())  # Leer el número de monedas
        monedas = list(map(int, input().strip().split()))  # Leer monedas para cada ejercicio
        lista_monedas.append(monedas)  # Añadir la lista de monedas para cada ejercicio

    return lista_monedas  # Retornar una lista de listas de monedas

def leer_desde_archivo(archivo_entrada):
    """
    Lee la entrada desde un archivo de texto para obtener los datos de los ejercicios.
    """
    lista_monedas = []
    with open(archivo_entrada, 'r') as f:
        n = int(f.readline().strip())  # Leer el número de ejercicios
        for _ in range(n):
            m = int(f.readline().strip())  # Leer el número de monedas para el ejercicio actual
            monedas = list(map(int, f.readline().strip().split()))  # Leer las monedas para el ejercicio actual
            lista_monedas.append(monedas)  # Añadir la lista de monedas

    return lista_monedas

def escribir_resultado_a_archivo(archivo_salida, resultados):
    """
    Escribe los resultados en un archivo de salida.
    """
    with open(archivo_salida, 'a') as f:
        for resultado in resultados:
            f.write(f"{resultado}\n")

def main():
    parser = argparse.ArgumentParser(description="Programa que resuelve el problema de división de monedas.")
    parser.add_argument('--input', type=str, help="Archivo de entrada (opcional). Si no se proporciona, se usará la entrada por consola.")
    parser.add_argument('--output', type=str, help="Archivo de salida (opcional). Si no se proporciona, se usará la salida por consola.")

    args = parser.parse_args()

    # Leer los datos desde archivo o consola
    if args.input:
        lista_monedas = leer_desde_archivo(args.input)
    else:
        lista_monedas = leer_desde_consola()

    # Procesar los datos
    resultados = division_monedas(lista_monedas)

    # Escribir los resultados en archivo o consola
    if args.output:
        escribir_resultado_a_archivo(args.output, resultados)
    else:
        print("Resultados:")
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
