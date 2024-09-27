import sys

# Constantes
MAX = 1000001

# Estructura para representar una arista (edge)
class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

# Lista de aristas
edges = []

# Disjoint-set (union-find) para los subconjuntos
parent = [0] * MAX

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])  # Compresión de caminos
    return parent[a]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    parent[root_a] = root_b  # Unión de conjuntos

def kruskal(N, E):
    for i in range(N + 1):
        parent[i] = i

    # Ordenar las aristas por peso
    edges.sort(key=lambda edge: edge.weight)

    e = 0  # Número de aristas en el MST
    cost = 0  # Costo total del MST

    for i in range(E):
        if e >= N - 1:
            break

        # Verificar si la arista forma un ciclo
        if find(edges[i].v1) != find(edges[i].v2):
            union(edges[i].v1, edges[i].v2)
            cost += edges[i].weight
            e += 1

    return cost

def main():
    if len(sys.argv) != 3:
        print("Uso: python nombre.py input.txt output.txt")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    first_case = True

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Leer todo el contenido del archivo de entrada
        content = infile.read().strip()

        # Dividir los casos de prueba por líneas en blanco
        cases = content.split('\n\n')

        for case in cases:
            # Ignorar los casos vacíos o mal formateados
            if not case.strip():
                continue

            lines = case.strip().split('\n')
            N = int(lines[0].strip())  # Número de sitios
            old_cost = 0
            global edges
            edges = []

            # Leer las N-1 líneas de conexiones antiguas
            index = 1
            for _ in range(1, N):
                a, b, w = map(int, lines[index].split())
                old_cost += w
                index += 1

            # Leer las nuevas conexiones
            K = int(lines[index].strip())
            index += 1
            for _ in range(K):
                a, b, w = map(int, lines[index].split())
                edges.append(Edge(a, b, w))
                index += 1

            # Leer las conexiones originales
            M = int(lines[index].strip())
            index += 1
            for _ in range(M):
                a, b, w = map(int, lines[index].split())
                edges.append(Edge(a, b, w))
                index += 1

            # Calcular el nuevo costo con Kruskal
            new_cost = kruskal(N, K + M)

            # Separar los casos de prueba con una línea en blanco
            if not first_case:
                outfile.write("\n")
            first_case = False

            # Escribir el costo original y el nuevo costo
            outfile.write(f"{old_cost}\n{new_cost}\n")

if __name__ == "__main__":
    main()
