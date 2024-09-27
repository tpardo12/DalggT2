import sys

def max_reliquias(R, C, matriz):
    steps = R // 2 + 1  # Number of steps to reach the central row

    # Initialize DP table
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
    dp[dp_state] = initial_relics

    # Movement directions
    directions = [-1, 0, 1]

    for step in range(1, steps):
        new_dp = {}
        for state in dp:
            indiana_pos, marion_pos, sallah_pos = state
            current_relics = dp[state]

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

                        # Update DP
                        if new_state not in new_dp or new_relics > new_dp[new_state]:
                            new_dp[new_state] = new_relics

        dp = new_dp  # Update DP for the next step

    # Find the maximum relics collected when characters reach the central row
    max_total_relics = -1
    final_row = R // 2

    for state in dp:
        indiana_pos, marion_pos, sallah_pos = state
        if ((not indiana_pos or indiana_pos[0] == final_row) and
            (not marion_pos or marion_pos[0] == final_row) and
            (not sallah_pos or sallah_pos[0] == final_row)):
            if dp[state] > max_total_relics:
                max_total_relics = dp[state]

    return max_total_relics if max_total_relics != -1 else -1

# Main function to handle input and output from command line arguments
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python archivo.py input.txt output.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as f, open(output_file, 'w') as output:
        num_cases = int(f.readline().strip())
        for _ in range(num_cases):
            R, C = map(int, f.readline().strip().split())
            matriz = [list(map(int, f.readline().strip().split())) for _ in range(R)]
            result = max_reliquias(R, C, matriz)
            output.write(f"{result}\n")
            output.flush()  # Ensure the result is written immediately

