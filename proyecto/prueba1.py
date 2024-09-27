import sys
from io import StringIO

class ProblemaP1:
    def __init__(self):
        self.reader = sys.stdin

    def build_pyramid(self, r, c):
        pyramid = []
        for current_row in range(r):
            row = list(map(int, self.reader.readline().split()))
            pyramid.append(row)
        return pyramid

    def solve(self, r, c):
        mid = r // 2
        pyramid = self.build_pyramid(r, c)

        dp = [[[float('-inf')] * c for _ in range(c)] for _ in range(2)]
        relics = [[[[float('-inf'), float('-inf')] for _ in range(c)] for _ in range(c)] for _ in range(2)]

        possible_last = [[[] for _ in range(c)] for _ in range(c)]

        for i in range(c):
            for j in range(c):
                combinations = []
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        try:
                            ignored = dp[0][i + k][j + l]
                            combinations.append((i + k, j + l))
                        except IndexError:
                            pass
                possible_last[i][j] = combinations

        top_result = 0

        for row in range(mid + 1):
            current_idx = row % 2
            prev_idx = (row + 1) % 2
            for i in range(c):
                for j in range(c):
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
                        [(dp[prev_idx][pos[0]][pos[1]], relics[prev_idx][pos[0]][pos[1]][0], relics[prev_idx][pos[0]][pos[1]][1]) 
                         for pos in possible_last[i][j]], key=lambda x: x[0], default=(float('-inf'), float('-inf'), float('-inf'))
                    )

                    relics[current_idx][i][j][0] = last_combination_max[1]
                    relics[current_idx][i][j][1] = last_combination_max[2]

                    if last_combination_max[0] < 0:
                        relics[current_idx][i][j][0] = float('-inf')
                        relics[current_idx][i][j][1] = float('-inf')
                        dp[current_idx][i][j] = float('-inf')
                    elif i == j and pyramid[row][i] == -1:
                        relics[current_idx][i][j][0] = float('-inf')
                        relics[current_idx][i][j][1] = float('-inf')
                        dp[current_idx][i][j] = float('-inf')
                    elif i == j:
                        dp[current_idx][i][j] = pyramid[row][i] + last_combination_max[0]
                        player_to_add = -1
                        if last_combination_max[1] >= 0:
                            player_to_add = 0
                        elif last_combination_max[2] >= 0:
                            player_to_add = 1
                        if player_to_add != -1:
                            relics[current_idx][i][j][player_to_add] += pyramid[row][i]
                    else:
                        total = last_combination_max[0]
                        deaths = 0
                        if pyramid[row][i] == -1:
                            relics[current_idx][i][j][0] = float('-inf')
                            if last_combination_max[1] > 0:
                                total -= last_combination_max[1]
                            deaths += 1
                        elif last_combination_max[1] >= 0:
                            total += pyramid[row][i]
                            relics[current_idx][i][j][0] += pyramid[row][i]

                        if pyramid[row][j] == -1:
                            relics[current_idx][i][j][1] = float('-inf')
                            if last_combination_max[2] > 0:
                                total -= last_combination_max[2]
                            deaths += 1
                        elif last_combination_max[2] >= 0:
                            total += pyramid[row][j]
                            relics[current_idx][i][j][1] += pyramid[row][j]

                        dp[current_idx][i][j] = total if deaths < 2 else float('-inf')

            top_result = current_idx

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
                    if reversed_row != mid:
                        if pyramid[reversed_row][i] == -1:
                            bottom[current_idx][i] = float('-inf')
                        else:
                            candidates = [bottom[prev_idx][i]]
                            if i > 0:
                                candidates.append(bottom[prev_idx][i - 1])
                            if i < c - 1:
                                candidates.append(bottom[prev_idx][i + 1])
                            bottom[current_idx][i] = max(candidates) + pyramid[reversed_row][i] if max(candidates) != float('-inf') else float('-inf')
                    else:
                        for j in range(c):
                            for k in range(c):
                                value = dp[top_result][j][k]
                                if pyramid[reversed_row][i] != -1:
                                    candidates = [bottom[prev_idx][i]]
                                    if i > 0:
                                        candidates.append(bottom[prev_idx][i - 1])
                                    if i < c - 1:
                                        candidates.append(bottom[prev_idx][i + 1])
                                    prev_value = max(candidates)
                                    if i != j and i != k and prev_value != float('-inf'):
                                        value += prev_value + pyramid[reversed_row][i]
                                    elif prev_value != float('-inf'):
                                        value += prev_value
                                if value > final_score:
                                    final_score = value

        return final_score if final_score != 0 else -1

# Función para ejecutar las pruebas con las matrices de entrada
def test_case(matrix, rows, cols):
    input_data = "\n".join(" ".join(map(str, row)) for row in matrix) + "\n"
    sys.stdin = StringIO(input_data)  # Simular la entrada
    problema = ProblemaP1()
    resultado = problema.solve(rows, cols)
    print(f"Resultado: {resultado}")

# Definición de matrices
matriz1 = [
    [0, 9, 1, 10, 0],
    [-1, 5, 5, 25, 5],
    [1, 5, 1, 5, 7],
    [5, 5, 5, 15, 2],
    [55, 3, 0, 4, 1]
]

matriz2 = [
    [0, 7, 2, -1, 0],
    [6, 1, 8, 9, 3],
    [-1, 4, 7, 5, 2],
    [2, 1, 9, -1, 4],
    [5, 6, 3, 8, 7],
    [9, 2, 1, 4, -1],
    [8, -1, 3, 6, 5],
    [4, 7, 2, 1, 9],
    [3, 5, 6, 7, 8],
    [-1, 1, 2, 3, 4],
    [5, 8, 7, -1, 6],
    [6, 9, 3, 2, 1],
    [7, 4, -1, 5, 8],
    [2, 1, 6, 7, 3],
    [9, 4, 5, 8, 2],
    [8, 3, 2, 1, -1],
    [4, 6, 9, 5, 7],
    [1, 2, 8, 3, 9],
    [5, 6, 4, 9, 1],
    [-1, 3, 2, 8, 7],
    [1, 9, 0, 6, 2]
]

matriz3 = [
    [0, 9, 1, 10, 0],
    [-1, -1, 5, -1, 5],
    [1, 5, 1, 5, 7],
    [5, 5, 5, 15, 2],
    [55, 3, 0, 4, 1]
]

matriz7 = [
    [0, 3, 0],
    [1, -1, 4],
    [2, 6, 8],
    [-1, 1, 3],
    [9, 2, 5],
    [4, 7, -1],
    [3, 8, 6],
    [1, 9, 2],
    [8, 4, 5],
    [6, 7, 1],
    [2, 3, -1],
    [7, 5, 9],
    [1, 8, 4],
    [-1, 6, 2],
    [5, 3, 7],
    [9, 1, 8],
    [4, 2, 6],
    [3, -1, 5],
    [6, 8, 1],
    [2, 7, 9],
    [-1, 0, 4]
]

matriz5 = [
    [0, 7, 2, -1, 0],
    [6, 1, 8, 9, 3],
    [-1, -1, -1, -1, -1],
    [2, 1, 9, -1, 4],
    [5, 6, 3, 8, 7],
    [9, 2, 1, 4, -1],
    [8, -1, 3, 6, 5],
    [4, 7, 2, 1, 9],
    [3, 5, 6, 7, 8],
    [-1, 1, 2, 3, 4],
    [5, 8, 7, -1, 6],
    [6, 9, 3, 2, 1],
    [7, 4, -1, 5, 8],
    [2, 1, 6, 7, 3],
    [9, 4, 5, 8, 2],
    [8, 3, 2, 1, -1],
    [4, 6, 9, 5, 7],
    [1, 2, 8, 3, 9],
    [5, 6, 4, 9, 1],
    [-1, -1, -1, -1, -1],
    [1, 9, 0, 6, 2]
]

# Pruebas
print("Prueba matriz1:")
test_case(matriz1, 5, 5)

print("\nPrueba matriz2:")
test_case(matriz2, 21, 5)

print("\nPrueba matriz3:")
test_case(matriz3, 5, 5)

print("\nPrueba matriz7:")
test_case(matriz7, 21, 3)

print("\nPrueba matriz5:")
test_case(matriz5, 21, 5)
