def wedding_shopping(M, garments):
    dp = [False] * (M + 1)
    dp[0] = True
    
    for category in garments:
        new_dp = [False] * (M + 1)
        for price in category:
            for m in range(M + 1):
                if dp[m] and m + price <= M:
                    new_dp[m + price] = True
        dp = new_dp
    
    # Find the maximum amount spent
    for i in range(M, -1, -1):
        if dp[i]:
            return i
    return "no solution"

# Example Usage
M = 100
garments = [[8, 6, 4], [5, 10], [1, 3, 3, 7], [50, 14, 23, 8]]
print(wedding_shopping(M, garments))  # Output: 75