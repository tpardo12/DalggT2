def murcia_skyline(heights, widths):
    N = len(heights)
    LIS = [0] * N
    LDS = [0] * N
    
    for i in range(N):
        LIS[i] = widths[i]
        for j in range(i):
            if heights[i] > heights[j]:
                LIS[i] = max(LIS[i], LIS[j] + widths[i])
    
    for i in range(N - 1, -1, -1):
        LDS[i] = widths[i]
        for j in range(i + 1, N):
            if heights[i] > heights[j]:
                LDS[i] = max(LDS[i], LDS[j] + widths[i])
    
    max_increasing = max(LIS)
    max_decreasing = max(LDS)
    
    if max_increasing >= max_decreasing:
        return f"Increasing ({max_increasing}). Decreasing ({max_decreasing})."
    else:
        return f"Decreasing ({max_decreasing}). Increasing ({max_increasing})."

# Example Usage
heights = [10, 100, 50, 30, 80, 10]
widths = [50, 10, 10, 15, 20, 10]
print(murcia_skyline(heights, widths))  # Output: Increasing (85). Decreasing (50).