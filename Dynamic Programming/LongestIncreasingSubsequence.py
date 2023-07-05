def lis(sequence):
    n = len(sequence)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

sequence = [10, 9, 2, 5, 3, 7, 101, 18]
print(lis(sequence)) 
 