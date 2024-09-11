import sys

def ferry2(ferry_length, cars):
    ferry_length = ferry_length * 100
    inicio = {0: [(ferry_length, ferry_length, -1)]} #diccionario para almacenar los movimientos de los coches y loas espacios disponibles
    for car in range(len(cars)):
        lista = []
        for AB in inicio[car]:
            Ai, Bi, movimientos = AB
            if (Ai - cars[car]) == (Bi - cars[car]) and (Ai - cars[car] > 0):
                mov = '0' if movimientos == -1 else movimientos + '0' # cuando ambos casos son iguales, se agrega el coche al lado izquierdo
                lista.append((Ai - cars[car], Bi, mov))
            else:
                if (Ai - cars[car]) >= 0 and ((Ai - cars[car], Bi) not in lista):
                    mov = movimientos + '0' if movimientos != -1 else '0'# se agrega el coche al lado izquierdo
                    lista.append((Ai - cars[car], Bi, mov))
                if (Bi - cars[car]) >= 0 and ((Ai, Bi - cars[car]) not in lista): 
                    mov = movimientos + '1' if movimientos != -1 else '1' # se agrega el coche al lado derecho
                    lista.append((Ai, Bi - cars[car], mov))

        if lista:
            inicio[car + 1] = lista
        else:
            num = len(inicio) - 1
            return num, inicio[num][0][2]
    return 0, ''  # Si no se puede cargar ningún coche, devolvemos 0 y una cadena vacía

def read_input(source):
    # Función para leer la entrada, ya sea desde un archivo o desde la consola
    if source:
        return open(source, 'r')
    else:
        return sys.stdin  # Lee desde la consola

def write_output(destination):
    # Función para escribir la salida, ya sea en archivo o en la consola
    if destination:
        return open(destination, 'w')
    else:
        return sys.stdout  # Escribe en la consola

def main(input_file=None, output_file=None):
    # Abrir los archivos de entrada/salida (si se proporcionan)
    with read_input(input_file) as infile, write_output(output_file) as outfile:
        # Leer el número de casos
        T = int(infile.readline().strip())  # Número de casos de prueba
        infile.readline().strip()  # Leer la línea en blanco después del número de casos
        
        # Iterar sobre cada caso de prueba
        for _ in range(T):
            ferry_length = int(infile.readline().strip())  # Leer la longitud del ferry en metros
            
            cars = []  # Lista para almacenar las longitudes de los coches
            while True:
                car_length = int(infile.readline().strip())  # Leer la longitud de cada coche
                if car_length == 0:  # Si la longitud es 0, terminamos de leer
                    break
                cars.append(car_length)  # Añadimos el coche a la lista
            
            # Llamamos a la función para calcular el máximo de coches que pueden entrar
            total_cars, arrangement = ferry2(ferry_length, cars)
            
            # Escribir el número de coches cargados en el archivo de salida
            outfile.write(f"{total_cars}\n")
            
            # Escribir la disposición de cada coche (port o starboard) en el archivo de salida
            for side in arrangement:
                if side == '0':
                    outfile.write("port\n")  # Si el coche va en el lado izquierdo (port)
                else:
                    outfile.write("starboard\n")  # Si el coche va en el lado derecho (starboard)
            
            # Escribir una línea en blanco entre casos
            outfile.write("\n")

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
1. Solución:
   - La solución utiliza la técnica de **Bottom-Up (BU)**, ya que construimos las soluciones parciales 
     comenzando desde el primer coche, revisando las posibles combinaciones para cargar los coches.
     
2. Complejidad espacial y temporal:
   - Complejidad Temporal: O(n * L) donde `n` es el número de coches y `L` es la longitud del ferry en centímetros. 
     Por cada coche, calculamos las combinaciones de espacio restante para los dos lados (port y starboard).
   - Complejidad Espacial: O(n * L) ya que utilizamos un diccionario para almacenar las combinaciones de espacio 
     restante en cada paso.
   
   Explicación breve: El tiempo depende de cuántos coches hay y cuántas combinaciones de espacio restante en el ferry 
   evaluamos, que está ligado a la longitud del ferry y al número de coches.

3. Estrategia y uso de memoización:
   - Estrategia: La estrategia sigue un enfoque de **Programación Dinámica (Dynamic Programming)**. Vamos evaluando las 
     combinaciones de espacio disponible en ambos lados del ferry (port y starboard), coche por coche, y decidimos dónde 
     cargar cada coche para maximizar el número de coches cargados.
   - Uso de memoización: Usamos memoización al almacenar las combinaciones de espacio restante en el ferry (port y starboard)
     en el diccionario `inicio`. Esto evita recalcular combinaciones para coches previos y mejora la eficiencia al reducir el 
     número de combinaciones que necesitamos revisar en cada paso.
"""
