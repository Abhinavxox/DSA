wt = [1, 3, 5, 6]
val = [22, 23 ,13, 31]
w = 6
n = 4

def knapsack_recursive(weight_array, value_array, w, n):
    if(n==0 or w==0):
        return 0

    if(weight_array[n-1]<=w):
        return max(value_array[n-1]+knapsack_recursive(weight_array,value_array, w-weight_array[n-1], n-1), knapsack_recursive(weight_array,value_array, w, n-1))
    
    elif(weight_array[n-1]>w):
        return knapsack_recursive(weight_array,value_array,w,n-1)
    
t = [[-1 for i in range(w+1)] for j in range(n+1)]
def knapsack_recursive_memo(weight_array, value_array, w, n):
    if(n==0 or w==0):
        return 0
    
    if(t[n][w]!=-1):
        return t[n][w]

    if(weight_array[n-1]<=w):
        t[n][w] = max(value_array[n-1]+knapsack_recursive_memo(weight_array,value_array, w-weight_array[n-1], n-1), knapsack_recursive_memo(weight_array,value_array, w, n-1))
        return t[n][w]

    elif(weight_array[n-1]>w):
        t[n][w] = knapsack_recursive_memo(weight_array,value_array,w,n-1)
        return t[n][w]

print(knapsack_recursive(wt,val,w,n))
print(knapsack_recursive_memo(wt,val,w,n))