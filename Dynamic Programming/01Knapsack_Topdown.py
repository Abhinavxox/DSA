val = [60, 100, 120]
wt = [10, 20, 30]
w = 50
n = len(val)

def knapsack_topdown(wt,val,w,n):
    t = [[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if(i==0 or j==0):
                t[i][j] = 0

            elif(wt[i-1]<=j):
                t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]], t[i-1][j])

            elif(wt[i-1]>j):
                t[i][j] = t[i-1][j]

    return t[n][w]

print(knapsack_topdown(wt,val,w,n))