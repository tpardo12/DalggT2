import sys

def build_pyramid(reader, r, c):
    pyramid = []
    for _ in range(r):
        pyramid.append([int(x) for x in reader.readline().split()])
    return pyramid

def solve(reader):
    # Leer el número de casos de prueba
    num_cases = int(reader.readline())
    
    results = []
    
    for _ in range(num_cases):
        # Leer las dimensiones de la pirámide
        r, c = map(int, reader.readline().split())
        
        # Construir la pirámide
        pyramid = build_pyramid(reader, r, c)
        
        mid = r // 2  # Divide por dos
        dp = [[[float('-inf')] * c for _ in range(c)] for _ in range(2)]
        relics = [[[[float('-inf')] * 2 for _ in range(c)] for _ in range(c)] for _ in range(2)]
        
        # Generar todas las combinaciones posibles para el último paso
        possible_last = [[[] for _ in range(c)] for _ in range(c)]
        
        for i in range(c):
            for j in range(c):
                combinations = []
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if 0 <= i + k < c and 0 <= j + l < c:
                            combinations.append([i + k, j + l])
                possible_last[i][j] = combinations
        
        top_result = 0
        
        for row in range(mid + 1):
            current_idx = row % 2
            prev_idx = (row + 1) % 2
            
            for i in range(c):  # Marion
                for j in range(c):  # Indiana
                    if row == 0 and (i != c - 1 or j != 0):
                        dp[current_idx][i][j] = float('-inf')
                        relics[current_idx][i][j][0] = float('-inf')
                        relics[current_idx][i][j][1] = float('-inf')
                        continue
                    elif row == 0:
                        dp[current_idx][i][j] = pyramid[row][i] + pyramid[row][j]
                        relics[current_idx][i][j][0] = pyramid[row][i]
                        relics[current_idx][i][j][1] = pyramid[row][j]
                        continue
                    
                    last_combination_max = max(
                        (dp[prev_idx][pos[0]][pos[1]], relics[prev_idx][pos[0]][pos[1]][0], relics[prev_idx][pos[0]][pos[1]][1])
                        for pos in possible_last[i][j]
                    )
                    
                    relics[current_idx][i][j][0] = last_combination_max[1]
                    relics[current_idx][i][j][1] = last_combination_max[2]
                    
                    if last_combination_max[0] < 0:  # Posición imposible
                        relics[current_idx][i][j][0] = float('-inf')
                        relics[current_idx][i][j][1] = float('-inf')
                        dp[current_idx][i][j] = float('-inf')
                    elif i == j and pyramid[row][i] == -1:  # Ambos mueren
                        relics[current_idx][i][j][0] = float('-inf')
                        relics[current_idx][i][j][1] = float('-inf')
                        dp[current_idx][i][j] = float('-inf')
                    else:
                        total = last_combination_max[0]
                        if pyramid[row][i] != -1:
                            total += pyramid[row][i]
                        if pyramid[row][j] != -1 and i != j:
                            total += pyramid[row][j]
                        dp[current_idx][i][j] = total
        
        # Fase de Sallah
        bottom = [[float('-inf')] * c for _ in range(2)]
        sallah_start = c // 2
        final_score = 0
        
        for reversed_row in range(r - 1, mid - 1, -1):
            current_idx = reversed_row % 2
            prev_idx = (reversed_row + 1) % 2
            
            if reversed_row == r - 1:
                bottom[current_idx][sallah_start] = 0
            else:
                for i in range(c):
                    if pyramid[reversed_row][i] != -1:
                        max_prev = max(bottom[prev_idx][i + d] for d in [-1, 0, 1] if 0 <= i + d < c)
                        if max_prev != float('-inf'):
                            bottom[current_idx][i] = max_prev + pyramid[reversed_row][i]
        
        for i in range(c):
            if bottom[current_idx][i] != float('-inf'):
                final_score = max(final_score, bottom[current_idx][i])
        
        results.append(final_score if final_score > 0 else -1)
    
    return results

if __name__ == "__main__":
    # Leer archivos de entrada y salida desde argumentos de línea de comando
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as reader:
        results = solve(reader)
    
    with open(output_file, 'w') as writer:
        for result in results:
            writer.write(f"{result}\n")

