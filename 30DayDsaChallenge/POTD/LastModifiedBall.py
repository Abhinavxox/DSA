class Solution():
    def solve(self, N, A):
        c = 1
        for i in range(N-1,-1,-1):
            if A[i] != 9:
                break
        return i+1

s = Solution()
N = 4
A = [0,0,1,9]
print(s.solve(N,A))
            