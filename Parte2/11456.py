def trainsorting(weights):
    n = len(weights)
    LIS = [1] * n
    LDS = [1] * n
    
    # Calculate LIS for each car
    for i in range(n):
        for j in range(i):
            if weights[i] > weights[j]:
                LIS[i] = max(LIS[i], LIS[j] + 1)
    
    # Calculate LDS for each car
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if weights[i] > weights[j]:
                LDS[i] = max(LDS[i], LDS[j] + 1)
    
    # Combine LIS and LDS for the result
    max_length = 0
    for i in range(n):
        max_length = max(max_length, LIS[i] + LDS[i] - 1)
    
    return max_length

# Example Usage
weights = [1, 2, 3]
print(trainsorting(weights))  # Output: 3
