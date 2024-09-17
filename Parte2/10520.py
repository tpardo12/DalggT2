import sys

# Función que calcula la matriz a según las reglas dadas
def calculate_matrix(n, an1):
    # Crear una matriz de tamaño n x n inicializada en 0
    a = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    # Establecer el valor base a[n,1]
    a[n][1] = an1

    # Calcular los valores de la matriz a según las reglas definidas
    for length in range(2, n + 1):  # Ir aumentando la longitud de las subsecuencias
        for i in range(1, n - length + 2):  # Inicio de la subsecuencia
            j = i + length - 1  # Fin de la subsecuencia
            if i < j:
                a[i][j] = max(a[i][k] + a[k+1][j] for k in range(i, j))

    return a[1][n]

# Función principal que procesa los archivos de entrada y salida
def main():
    if len(sys.argv) != 3:
        print("Uso: python p.py input.txt output.txt")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as infile:
            data = infile.read().splitlines()

        results = []

        for line in data:
            if line.strip() == "":
                continue

            n, an1 = map(int, line.split())
            result = calculate_matrix(n, an1)
            results.append(str(result))

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
