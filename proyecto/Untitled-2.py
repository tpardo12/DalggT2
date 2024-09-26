from typing import List

class Solution:
    def maxpick(self, grid: List[List[int]], i: int, j1: int, j2: int, j3: int, m: int, n: int, dp: List[List[List[List[int]]]]) -> int:
        if i == m - 1:  # Base case: last row for Indiana and Marion
            # Handle overlap for the last row
            if j1 == j2 == j3:  # All robots on the same cell
                return grid[i][j1]
            elif j1 == j2 or j2 == j3 or j1 == j3:  # Two robots on the same cell
                return grid[i][j1] + grid[i][j2]
            else:  # All robots on different cells
                return grid[i][j1] + grid[i][j2] + grid[i][j3]

        if dp[i][j1][j2][j3] != -1:  # Memoization check
            return dp[i][j1][j2][j3]

        # All possible moves for the three robots
        dx = [-1, 0, 1]
        max_cherries = -float('inf')
        for move1 in dx:  # Indiana's movement
            for move2 in dx:  # Marion's movement
                for move3 in dx:  # Sallah's movement (moving upwards, so row index decreases)
                    new_j1 = j1 + move1
                    new_j2 = j2 + move2
                    new_j3 = j3 + move3
                    if 0 <= new_j1 < n and 0 <= new_j2 < n and 0 <= new_j3 < n:  # Check bounds
                        # Calculate cherries based on robot positions
                        cherries = 0
                        if new_j1 == new_j2 == new_j3:  # All robots on the same cell
                            cherries = grid[i][new_j1]
                        elif new_j1 == new_j2:  # Indiana and Marion on the same cell
                            cherries = grid[i][new_j1] + grid[i][new_j3]
                        elif new_j2 == new_j3:  # Marion and Sallah on the same cell
                            cherries = grid[i][new_j1] + grid[i][new_j2]
                        elif new_j1 == new_j3:  # Indiana and Sallah on the same cell
                            cherries = grid[i][new_j1] + grid[i][new_j2]
                        else:  # All robots on different cells
                            cherries = grid[i][new_j1] + grid[i][new_j2] + grid[i][new_j3]

                        # Recursively calculate maximum cherries
                        max_cherries = max(max_cherries, cherries + self.maxpick(grid, i + 1, new_j1, new_j2, new_j3, m, n, dp))

        dp[i][j1][j2][j3] = max_cherries  # Memoize result
        return max_cherries

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 4D DP table for storing results
        dp = [[[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(m)]
        # Indiana starts at (0, 0), Marion at (0, n - 1), Sallah at (m - 1, n // 2)
        return self.maxpick(grid, 0, 0, n - 1, n // 2, m, n, dp)

# Example grid
grid = [
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
matriz2 = [
    [0, 9, 1, 0],
    [-1, 5, 5, 5],
    [1, 5, 1, 7],
    [5, 5, 5, 2],
    [0, 3, 0, 1]
]


solution = Solution()
print(solution.cherryPickup(matriz2))


