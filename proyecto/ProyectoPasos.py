def max_reliquias(R, C, matriz):
    steps = R // 2 + 1  # Number of steps to reach the central row

    # Initialize DP table with initial positions and collected relics
    dp = {}

    # Starting positions
    positions = {}
    initial_relics = 0
    counted_cells = set()

    # Indiana's starting position
    if matriz[0][0] != -1:
        positions['indiana'] = (0, 0)
        initial_relics += matriz[0][0]
        counted_cells.add((0, 0))
    else:
        positions['indiana'] = None

    # Marion's starting position
    if matriz[0][C - 1] != -1:
        positions['marion'] = (0, C - 1)
        if (0, C - 1) not in counted_cells:
            initial_relics += matriz[0][C - 1]
            counted_cells.add((0, C - 1))
    else:
        positions['marion'] = None

    # Sallah's starting position
    if matriz[R - 1][C // 2] != -1:
        positions['sallah'] = (R - 1, C // 2)
        if (R - 1, C // 2) not in counted_cells:
            initial_relics += matriz[R - 1][C // 2]
            counted_cells.add((R - 1, C // 2))
    else:
        positions['sallah'] = None

    # Initialize DP with starting positions
    dp_state = (positions['indiana'], positions['marion'], positions['sallah'])
    dp[dp_state] = (initial_relics, [(positions['indiana'], positions['marion'], positions['sallah'])])

    # Movement directions
    directions = [-1, 0, 1]

    for step in range(1, steps):
        new_dp = {}
        for state in dp:
            indiana_pos, marion_pos, sallah_pos = state
            current_relics, path = dp[state]

            # Generate possible moves for each character
            indiana_moves = []
            if indiana_pos:
                row, col = indiana_pos
                if row + 1 < R:
                    for d in directions:
                        new_col = col + d
                        if 0 <= new_col < C and matriz[row + 1][new_col] != -1:
                            indiana_moves.append((row + 1, new_col))
                if not indiana_moves:
                    indiana_moves.append(None)  # Indiana cannot move
            else:
                indiana_moves.append(None)  # Indiana is already dead

            marion_moves = []
            if marion_pos:
                row, col = marion_pos
                if row + 1 < R:
                    for d in directions:
                        new_col = col + d
                        if 0 <= new_col < C and matriz[row + 1][new_col] != -1:
                            marion_moves.append((row + 1, new_col))
                if not marion_moves:
                    marion_moves.append(None)  # Marion cannot move
            else:
                marion_moves.append(None)  # Marion is already dead

            sallah_moves = []
            if sallah_pos:
                row, col = sallah_pos
                if row - 1 >= 0:
                    for d in directions:
                        new_col = col + d
                        if 0 <= new_col < C and matriz[row - 1][new_col] != -1:
                            sallah_moves.append((row - 1, new_col))
                if not sallah_moves:
                    sallah_moves.append(None)  # Sallah cannot move
            else:
                sallah_moves.append(None)  # Sallah is already dead

            # Combine all possible moves
            for new_indiana in indiana_moves:
                for new_marion in marion_moves:
                    for new_sallah in sallah_moves:
                        new_state = (new_indiana, new_marion, new_sallah)
                        new_counted_cells = set()
                        new_relics = current_relics

                        # Collect relics at new positions
                        if new_indiana and new_indiana not in new_counted_cells:
                            new_relics += matriz[new_indiana[0]][new_indiana[1]]
                            new_counted_cells.add(new_indiana)
                        if new_marion and new_marion not in new_counted_cells:
                            new_relics += matriz[new_marion[0]][new_marion[1]]
                            new_counted_cells.add(new_marion)
                        if new_sallah and new_sallah not in new_counted_cells:
                            new_relics += matriz[new_sallah[0]][new_sallah[1]]
                            new_counted_cells.add(new_sallah)

                        # Update DP with path tracking
                        new_path = path + [(new_indiana, new_marion, new_sallah)]
                        if new_state not in new_dp or new_relics > new_dp[new_state][0]:
                            new_dp[new_state] = (new_relics, new_path)

        dp = new_dp  # Update DP for the next step

    # Find the maximum relics collected when characters reach the central row
    max_total_relics = -1
    final_path = None
    final_row = R // 2

    for state in dp:
        indiana_pos, marion_pos, sallah_pos = state
        if ((not indiana_pos or indiana_pos[0] == final_row) and
            (not marion_pos or marion_pos[0] == final_row) and
            (not sallah_pos or sallah_pos[0] == final_row)):
            if dp[state][0] > max_total_relics:
                max_total_relics = dp[state][0]
                final_path = dp[state][1]

    # Print the path if found
    if final_path:
        print("Pasos de cada personaje:")
        for step, (indiana, marion, sallah) in enumerate(final_path):
            print(f"Step {step}:")
            print(f"  Indiana: {indiana}")
            print(f"  Marion: {marion}")
            print(f"  Sallah: {sallah}")

    return max_total_relics if max_total_relics != -1 else -1

# Example matrices provided
R, C = 5, 5

matriz1 = [
    [0, 9, 1, 10, 0, 0, 0],
    [-1, 5, 5, 25, 0, 0, 5],
    [1, 5, 1, 5, 7, 0, 1],
    [5, 5, 5, 15, 2,0 , 1],
    [55, 3, 0, 0, 1,0 ,1 ]
]

matriz2=[[ 0,  7,  2, -1,  0],
    [ 6,  1,  8,  9,  3],
    [-1,  4,  7,  5,  2],
    [ 2,  1,  9, -1,  4],
    [ 5,  6,  3,  8,  7],
    [ 9,  2,  1,  4, -1],
    [ 8, -1,  3,  6,  5],
    [ 4,  7,  2,  1,  9],
    [ 3,  5,  6,  9,  8],
    [-1,  1,  5,  3,  4],
    [ 5,  8,  7, -1,  6],
    [ 6,  9,  3,  2,  1],
    [ 7,  4, -1,  5,  8],
    [ 2,  1,  6,  7,  3],
    [ 9,  4,  5,  8,  2],
    [ 8,  3,  2,  1, -1],
    [ 4,  6,  9,  5,  7],
    [ 1,  2,  8,  3,  9],
    [ 5,  6,  4,  9,  1],
    [-1,  3,  2,  8,  7],
    [ 1,  9,  0,  6,  2]]

matriz3 = [
    [0, 9, 1, 10, 0],
    [-1, -1, 5, -1, 5],
    [1, 5, 1, 5, 7],
    [5, 5, 5, 15, 2],
    [55, 3, 0, 4, 1]
]

matriz4=[
    [0,1,1,1,0],
    [0,1,3,1,0],
    [0,1,1,1,0],
    [4,3,1,1,0],
    [2,3,3,1,4],
    [1,2,3,4,5],
    [1,2,0,3,2]
]

matriz5=[
    [0,0,0,0,0,0,0],
    [1,0,0,0,10,10,10],
    [1,0,0,0,10,10,10],
    [1,0,0,0,0,10,10],
    [1,0,0,0,10,10,10],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]

matriz6=[
    [0,0,0],
    [-1,1,-1],
    [1,1,1],
    [0,1,0],
    [0,0,0]

]

matriz7=[
     [ 0,  3,  0],
    [ 1, -1,  4],
    [ 2,  6,  8],
    [-1,  1,  3],
    [ 9,  2,  5],
    [ 4,  7, -1],
    [ 3,  8,  6],
    [ 1,  9,  2],
    [ 8,  4,  5],
    [ 6,  7,  1],
    [ 2,  3, -1],
    [ 7,  5,  9],
    [ 1,  8,  4],
    [-1,  6,  2],
    [ 5,  3,  7],
    [ 9,  1,  8],
    [ 4,  2,  6],
    [ 3, -1,  5],
    [ 6,  8,  1],
    [ 2,  7,  9],
    [-1,  0,  4]
]

matriz8=[[ 0,  7,  2, -1,  0],
    [ 6,  1,  8,  9,  3],
    [-1,  -1,  -1,  -1,  -1],
    [ 2,  1,  9, -1,  4],
    [ 5,  6,  3,  8,  7],
    [ 9,  2,  1,  4, -1],
    [ 8, -1,  3,  6,  5],
    [ 4,  7,  2,  1,  9],
    [ 3,  5,  6,  7,  8],
    [-1,  1,  2,  3,  4],
    [ 5,  8,  7, -1,  6],
    [ 6,  9,  3,  2,  1],
    [ 7,  4, -1,  5,  8],
    [ 2,  1,  6,  7,  3],
    [ 9,  4,  5,  8,  2],
    [ 8,  3,  2,  1, -1],
    [ 4,  6,  9,  5,  7],
    [ 1,  2,  8,  3,  9],
    [ 5,  6,  4,  9,  1],
    [-1,  -1,  -1,  -1,  -1],
    [ 1,  9,  0,  6,  2]]

resultado1 = max_reliquias(R, 7, matriz1)
resultado2 = max_reliquias(21, 5, matriz2)
resultado3 = max_reliquias(R, C, matriz3)
resultado4 = max_reliquias(7,5,matriz4)
resultado5 = max_reliquias(9,7,matriz5)
restulado6 = max_reliquias(5,3,matriz6)
resultado7 = max_reliquias(21,3,matriz7)
resultado8 = max_reliquias(21,5,matriz8)


print(f"Total máximo de reliquias recolectadas en matriz1: {resultado1}")
print(f"Total máximo de reliquias recolectadas en matriz2: {resultado2}")
print(f"Total máximo de reliquias recolectadas en matriz3: {resultado3}")
print(f"Total máximo de reliquias recolectadas en matriz4: {resultado4}")
print(f"Total máximo de reliquias recolectadas en matriz4: {resultado5}")
print(f"Total máximo de reliquias recolectadas en matriz4: {restulado6}")
print(f"Total máximo de reliquias recolectadas en matriz4: {resultado7}")
print(f"Total máximo de reliquias recolectadas en matriz4: {resultado8}")
