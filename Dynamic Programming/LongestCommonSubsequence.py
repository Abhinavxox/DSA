X = 'ABCDEFGHIJ'
Y = 'ABXFE'
m = len(X)
n = len(Y)

def LCS_Recursive(X,Y,m,n):
    if(n==0 or m==0):
        return 0
    
    if(X[m-1]==Y[n-1]):
        return 1 + LCS_Recursive(X,Y,m-1,n-1)
    
    else:
        return max(LCS_Recursive(X,Y,m, n-1), LCS_Recursive(X,Y,m-1,n))
    
t = [[-1 for i in range(n+1)] for i in range(m+1)]
def LCS(X,Y,m,n):
    if(n==0 or m==0):
        return 0
    
    if(t[m][n]!=-1):
        return t[m][n]
    
    if(X[m-1]==Y[n-1]):
        t[m][n] = 1 + LCS(X,Y,m-1,n-1)
        return t[n][m]
    
    else:
        t[m][n] = max(LCS_Recursive(X,Y,m, n-1), LCS(X,Y,m-1,n))
        return t[m][n]
    
print(LCS_Recursive(X,Y,m,n))
print(LCS(X,Y,m,n))
