import sys


def change(amount, cur):
    
    prev = [0] * (amount + 1)
    prev[0] = 1
    for i in range(1, amount + 1):
        
        if ( i < cur[0]):
            prev[i] = 0
        else:
            prev[i]  = prev[i - cur[0]]
        
        
        
    for j in range(1, len(cur)):
        
        next = [0] * (amount + 1)
        next[0] = 1

        
        for i in range(1, amount + 1):
           
            if ( i < cur[j]):
                next[i] = prev[i]
            else:
                next[i] =  prev[i] + next[i - cur[j]]
       
        prev = next
        

    return prev[amount]


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


def  main(input_file=None, output_file=None):
    cur = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]  
    with read_input(input_file) as infile:
        outfile = write_output(output_file)  # Mantener outfile abierto todo el tiempo en modo 'a'

        for line in infile:
            if (int(float(line.split()[-1]) * 100) != 0):
                
                f  = change(int(float(line.split()[-1]) * 100) , cur)
                outfile.write(f"{f}\n")

            
        if outfile == sys.stdout:
            sys.stdout.flush()

        # Cerrar el archivo de salida si fue un archivo
        if output_file:
            outfile.close()
            
                
            
    

if __name__ == "__main__":
    input_file = None
    output_file = None
    
    # Si el usuario pasa argumentos desde la línea de comandos, los utilizamos
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    
    main(input_file, output_file)

# -- Sección de Explicación --
# – Su solución es BU o TP:
#   Esta solución es una **solución de abajo hacia arriba (Bottom-Up, BU)**. 
#   En lugar de resolver el problema principal directamente, primero resuelve subproblemas más pequeños, 
#   utilizando programación dinámica para construir la solución completa. 
#   Esto contrasta con la estrategia "Top-Down" (TP), que utilizaría recursión con memoización.

# – Complejidad espacial y temporal:
#   - Complejidad temporal: **O(n * j )**, donde `n` es el número de denominaciones, `j` es el monto al que se quiere llegar,
#     Cada problema se resuelve procesando cada moneda, teniendo en cuenta un arreglo anterior de procesamientos, para llegar a la combinancion total
#
#   - Complejidad espacial: **O(monto * 2 )**. La memoria usada para almacenar los posibles combinaciones que pueden tener las monedas en montos inferiores, y se usa el arreglo pasado y el actual para calcular todo `.

# – Estrategia de la solución:
#   La primera estragia que se penso fue hacer una matriz con el numero de filas igual al nummero de denominaciones y el numero de columnas los posibles montos hasta llegar al monto indicado
#   en dicha  matriz se llenaran las posibles posbiles combinaciones para llegar a dicho monto. no obstante observe que no es necesario almacenar toda la matriz, simplemente la fila anterior y la actual

# – Uso de Memoización:
#   la solucion reserva un arreglo anteriro para realizar los calculos actuales.