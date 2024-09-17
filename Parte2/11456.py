import sys

def trainsorting(weights):
    n = len(weights)
    if n == 0:
        return 0

    # Arreglos de programación dinámica
    incr = [1] * n  # Longitud de la subsecuencia creciente hasta cada vagón
    decr = [1] * n  # Longitud de la subsecuencia decreciente desde cada vagón

    # Cálculo del arreglo 'incr' (subsecuencia creciente)
    for i in range(1, n):
        for j in range(i):
            if weights[j] < weights[i]:
                incr[i] = max(incr[i], incr[j] + 1)

    # Cálculo del arreglo 'decr' (subsecuencia decreciente)
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if weights[j] < weights[i]:
                decr[i] = max(decr[i], decr[j] + 1)

    # Imprimir los arreglos intermedios para depuración
    print(f"Pesos: {weights}")
    print(f"Subsecuencia creciente (incr): {incr}")
    print(f"Subsecuencia decreciente (decr): {decr}")

    # Calcular la longitud máxima de una subsecuencia bitónica
    max_length = 0
    for i in range(n):
        max_length = max(max_length, incr[i] + decr[i] - 1)

    print(f"Longitud máxima para este caso: {max_length}")
    return max_length

def main():
    # Comprobar si se proporcionaron los archivos de entrada y salida
    if len(sys.argv) != 3:
        print("Uso: python p.py input.txt output.txt")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as infile:
            data = infile.read().splitlines()

        t = int(data[0].strip())  # Número de casos de prueba
        index = 1
        results = []
        
        for case_num in range(1, t + 1):
            # Leer el número de vagones, puede estar en la misma línea con otros números
            while data[index].strip() == '':  # Ignorar líneas vacías
                index += 1
            n = int(data[index].strip())  # Número de vagones
            index += 1

            if n == 0:
                results.append("0")
                continue

            # Leer los pesos de los vagones, separando por espacios si están en la misma línea
            weights = []
            while len(weights) < n:
                # Dividir cada línea por espacios para obtener los números, y agregar a weights
                weights.extend(map(int, data[index].strip().split()))
                index += 1

            # Imprimir los pesos de los vagones para este caso de prueba
            print(f"\nCaso de prueba #{case_num} - Pesos: {weights}")
            
            # Calcular la subsecuencia bitónica más larga
            max_len = trainsorting(weights)
            results.append(str(max_len))

        # Escribir los resultados en el archivo de salida
        with open(output_file, 'w') as outfile:
            outfile.write("\n".join(results))
        
        print(f"Resultados escritos en {output_file}")

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {input_file}")
    except ValueError as e:
        print(f"Error de valor: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
