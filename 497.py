import sys


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



def read_input(source):
    # Función para leer la entrada, ya sea desde un archivo o desde la consola
    if source:
        return open(source, 'r')
    else:
        return sys.stdin  # Lee desde la consola

def write_output(destination):
    # Función para escribir la salida, ya sea en archivo o en la consola
    if destination:
        return open(destination, 'a')  # Modo 'a' para escribir sin sobreescribir el contenido
    else:
        return sys.stdout  # Escribe en la consola

def main(input_file=None, output_file=None):
    # Abrir los archivos de entrada/salida (si se proporcionan)
    with read_input(input_file) as infile:
        outfile = write_output(output_file)  # Mantener outfile abierto todo el tiempo en modo 'a'

        # Leer el número de casos
        T = int(infile.readline().strip())  # Número de casos de prueba
        infile.readline().strip()  # Leer la línea en blanco después del número de casos

        # Iterar sobre cada caso de prueba
        for _ in range(T):
            cent = True
            misiles = []
            while cent:
                m = infile.readline().strip()
                if not m or m == '':
                    break
                misiles.append(int(m))
            res = LIS(misiles)
            outfile.write(f"max hits: {res[1]}\n")
            for i in res[0]:
                outfile.write(f"{i}\n")
                
                
            # Escribir una línea en blanco entre casos
            outfile.write("\n")
            
            # Si es sys.stdout, asegurarse de que se vacíe el buffer y se imprima de inmediato
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