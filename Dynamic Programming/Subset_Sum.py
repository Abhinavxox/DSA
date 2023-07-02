arr = [12, 13, 14, 15, 16]
sum = 11
n = len(arr)

def subset_sum(arr, sum, n):
    t = [[False for i in range(sum+1)] for j in range(n+1)]
    #first column is true as for sum 0 every value is true
    for i in range(n+1):
        t[i][0] = True

    #first row is false as no items
    for i in range(1,sum+1):
       t[0][i] = False

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if (arr[i-1]<=j):
                t[i][j] = (t[i-1][j-arr[i-1]] or t[i-1][j])
            elif  (arr[i-1]>j):
                t[i][j] = t[i-1][j]

    return t[n][sum]

print(subset_sum(arr,sum,n))

        

