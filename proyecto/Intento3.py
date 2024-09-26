def max_reliquias(R, C, matriz):
    # dp[i][A][B][C] -> max reliquias collected after i steps when Indiana is in column A, 
    # Marion is in column B, and Sallah is in column C.
    
    # Initialize DP table
    dp = [[[[float('-inf') for _ in range(C)] for _ in range(C)] for _ in range(C)] for _ in range(R // 2 + 1)]
    

    # Starting positions for Indiana (0,0), Marion (0, C-1), Sallah (R-1, C//2)
    dp[0][0][C-1][C//2] = 0

    # Traverse rows step by step (i represents row for Indiana and Marion, R-i for Sallah)
    for i in range(1, R // 2 + 1):
        for A in range(C):
            for B in range(C):
                for C_pos in range(C):
                    # Check that A, B, and C_pos are valid starting positions
                    if i == 1 and C_pos != C // 2:
                        continue  # Skip until we reach the middle column for Sallah

                    # Check that A, B, and C_pos are not in the same column
                    if A == B or A == C_pos or B == C_pos:
                        continue  # Skip if any two characters are in the same column
                    
                    # Try to move to (i, A, B, C_pos) from all possible previous positions
                    # Indiana can only move down or diagonal down
                    for dA in [-1, 0, 1]:  # Indiana moves diagonally or straight down
                        prev_A = A + dA
                        if prev_A < 0 or prev_A >= C:
                            continue  # Skip out-of-bound moves for Indiana

                        # Marion can only move down or diagonal down from the right side
                        for dB in [-1, 0, 1]:  # Marion moves diagonally or straight down
                            prev_B = B + dB
                            if prev_B < 0 or prev_B >= C:
                                continue  # Skip out-of-bound moves for Marion

                            # Sallah can only move up or diagonal up from the center
                            for dC in [-1, 0, 1]:  # Sallah moves diagonally or straight up
                                prev_C = C_pos + dC
                                if prev_C < 0 or prev_C >= C:
                                    continue  # Skip out-of-bound moves for Sallah
                                
                                # Check if the previous positions are valid and not in the same column
                                if prev_A == prev_B or prev_A == prev_C or prev_B == prev_C:
                                    continue  # Prevent collecting in the same column in the previous step

                                # Calculate reliquias collected in the current step
                                collected = 0
                                visited = set()

                                # Indiana collects if A != B and A != C_pos
                                if A not in visited and matriz[i][A] != 0:
                                    collected += matriz[i][A]
                                
                                    visited.add(A)

                                # Marion collects if B != A and B != C_pos
                                if B not in visited and matriz[i][B] != 0:
                                    collected += matriz[i][B]
                                    
                                    visited.add(B)

                                # Sallah collects if C_pos != A and C_pos != B (but from R-i)
                                if C_pos not in visited and matriz[R-i][C_pos] != 0:
                                    collected += matriz[R-i][C_pos]
                                   
                                    visited.add(C_pos)
                                
                                # Handle case where multiple trofeos are nearby
                                # Allow another collection if there are trofeos near
                                # For example, if there is a 5 or 7 in a nearby column for B or C_pos
                                if B not in visited and matriz[i][B] != 0 and matriz[i][B] != matriz[i][A]:
                                    collected += matriz[i][B]
                                    visited.add(B)

                                if C_pos not in visited and matriz[R-i][C_pos] != 0 and matriz[R-i][C_pos] != matriz[i][A]:
                                    collected += matriz[R-i][C_pos]
                                    visited.add(C_pos)
                                
                                # Update DP table with max recoleccion including alternative moves
                                dp[i][A][B][C_pos] = max(dp[i][A][B][C_pos], dp[i-1][prev_A][prev_B][prev_C] + collected)
    
    # Find the maximum number of reliquias at the last row R//2 (the middle row)
    max_reliquias = -1
    for A in range(C):
        for B in range(C):
            for C_pos in range(C):
                max_reliquias = max(max_reliquias, dp[R//2][A][B][C_pos])
    
    # Return the maximum reliquias and the treasures collected by each character
    return max_reliquias

# Example case based on the matrix from the image you shared
R, C = 5, 5
#matriz = [
 #   [0, 119, 111, 110, 100],
  #  [-1, 5, 115, 25, 5],
  #  [1, 5, 1, 5, 7],
  #  [511, 5, 5, 15, 112],
  #  [515, 113, 0, 114, 111]
#]
matriz=[[ 0,  7,  2, -1,  0],
    [ 6,  1,  8,  9,  3],
    [-1,  4,  7,  5,  2],
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
    [-1,  3,  2,  8,  7],
    [ 1,  9,  0,  6,  2]]
max_reliquias = max_reliquias(R, C, matriz)

print(f"Total maximum treasures collected: {max_reliquias}")

