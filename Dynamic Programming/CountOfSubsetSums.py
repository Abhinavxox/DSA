arr = [1, 2, 3, 7, 8, 9, 10]
target_sum = 10
n = len(arr)


def count_subset_sum(arr, target_sum, n):
    t = [[0 for _ in range(target_sum + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        t[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    return t[n][target_sum]


print(count_subset_sum(arr, target_sum, n))
