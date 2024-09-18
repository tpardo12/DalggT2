
import sys


def LIS(arr): 
    
    n  = len(arr)
    max = 0
    max = 0
    sum = 0

    for i in range(n):
        sum += arr[i]
        
        if sum > max:
            max = sum
        if sum < 0:
            sum = 0

    s = "losing streak"    
    if max > 0:
        s = "the winning streak is: " + str(max)
    
    return s
  
  

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
        # Número de casos de prueba
        while True:
            s = infile.readline().strip()
            if not s or s == '':
                break
            T = int(s)
            if T ==  0:
                break
            apuestas = []
            while len(apuestas)  < T:
                m = list(map(int, infile.readline().split()))
                apuestas.extend(m)  
            res = LIS(apuestas)
            
            outfile.write(res + '\n')
            
            
            if outfile == sys.stdout:
                sys.stdout.flush()

     
        if output_file:
            outfile.close()


if __name__ == "__main__":
  
    input_file = None
    output_file = None
    

    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    
    main(input_file, output_file)
    

"""
#Para correr este archivo en la terminal : python 10684.py input.txt output.txt
Explicación del enfoque:

– La solución es **Bottom-Up (BU)**. Se construye la solución a partir de subproblemas más pequeños (compraraciones entre las apuestas) y se expande hasta encontrar la sub apuesta mas grande.
– Complejidad Temporal: O(n) donde n es el número total de apuestas, ya que se hace solamente una iteracion sobre dichas apuestas.
– Complejidad Espacial: O(n), ya que solo necesitamos el arreglo con las apuestas que se realizaron 
Estrategia: Se utiliza programación dinámica (DP) para calcular la racha de perdidas o de ganancias que se ha generado, en primere lugar se penso hacer un LIS, pero no era viable ya que la racha para ser ganadora no necesariamente tenia que ser creciente, se opto por una solucion mas sencilla que simplemente 
compara los elementos del arreglo y los va sumando en varaibles temporales como sum al llegar a una perdida, la restara de sum sin afectar la racha que ya se ha obtenido, y al encontrar otras granancias las sumara temporalmente en sum y comprar con la mas grande que llevamos hasta el momento.
**Memoización**: En esta solución no usamos memoización explícita (como en el enfoque recursivo con memoización). En su lugar, almacenamos todos los subproblemas en  variables temprales que seran de utilidad para ser comparadas despues y determinar si es una racha o perdida
"""
