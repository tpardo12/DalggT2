def term_strategy(N, M, marks):
    # Initialize dp array: dp[j] is the maximum total score achievable with j hours
    dp = [-1] * (M + 1)
    dp[0] = 0  # Zero hours spent results in a total score of 0
    
    # Iterate over each exam
    for exam in marks:
        # Temporary DP array to hold updates for this exam
        new_dp = [-1] * (M + 1)
        for j in range(M + 1):
            if dp[j] != -1:  # Only consider valid states (those where dp[j] is not -1)
                # Iterate over the possible hours spent on this exam (at least 1 hour)
                for h in range(1, M + 1):
                    if j + h <= M and exam[h - 1] >= 5:  # Ensure the score is passing (at least 5)
                        new_dp[j + h] = max(new_dp[j + h], dp[j] + exam[h - 1])
        dp = new_dp  # Update dp for the next exam
    
    # Check the best possible score
    max_total_score = max(dp)
    
    if max_total_score != -1:
        # Compute the average score
        average_score = max_total_score / N
        return f"Maximal possible average mark - {average_score:.2f}."
    else:
        return "Peter, you shouldn't have played billiard that much."

# Example Usage:
# N = 4 exams, M = 5 hours, and the marks array represents the score matrix for each exam.
N, M = 4, 5
marks = [
    [5, 5, 6, 7, 8],  # First exam: marks based on 1 to 5 hours spent
    [5, 5, 6, 7, 8],  # Second exam: same as above
    [5, 6, 7, 8, 8],  # Third exam
    [6, 7, 8, 9, 9]   # Fourth exam
]

# Output
print(term_strategy(N, M, marks))  # Expected output: Maximal possible average mark - 5.50.
