import sys
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


def read_input(source):
    # Función para leer la entrada, ya sea desde un archivo o desde la consola
    if source:
        return open(source, 'r')
    else:
        return sys.stdin  # Lee desde la consola

def write_output(destination):
    # Función para escribir la salida, ya sea en archivo o en la consola
    if destination:
        return open(destination, 'a')  # Abrimos el archivo en modo 'append'
    else:
        return sys.stdout  # Escribe en la consola

def main(input_file=None, output_file=None):
    # Abrir los archivos de entrada/salida (si se proporcionan)
    with read_input(input_file) as infile:
        outfile = write_output(output_file)  # Abrir el archivo de salida en modo 'append'

        # Leer tiempo de buceo disponible (t) y coeficiente de profundidad (w)
        t, w = map(int, infile.readline().strip().split())

        # Leer número de tesoros disponibles
        n = int(infile.readline().strip())

        # Leer los tesoros: (profundidad, valor del oro)
        tesoros = []
        for _ in range(n):
            d, v = map(int, infile.readline().strip().split())
            tesoros.append((d, v))

        # Llamar a la función para obtener el máximo valor y los tesoros seleccionados
        valor_mas_alto, tesoros_finales = diving_gold(t, w, tesoros)

        # Escribir los resultados inmediatamente en el archivo o consola
        outfile.write(f"{valor_mas_alto}\n")
        outfile.write(f"{len(tesoros_finales)}\n")
        for tesoro in tesoros_finales:
            outfile.write(f"{tesoro[0]} {tesoro[1]}\n")

        # Si estamos escribiendo en la consola, hacer flush para imprimir inmediatamente
        if outfile == sys.stdout:
            sys.stdout.flush()

        # Cerrar el archivo de salida si fue un archivo
        if output_file:
            outfile.close()

# Punto de entrada principal del programa
if __name__ == "__main__":
    # Verificamos si se pasan argumentos de entrada y salida
    input_file = None
    output_file = None
    
    # Si el usuario pasa argumentos desde la línea de comandos, los utilizamos
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    
    main(input_file, output_file)

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
