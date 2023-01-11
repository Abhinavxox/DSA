class Solution:
    def minIncrements(self, arr, N): 
        res = need = 0
        for i in sorted(arr):
            res += max(need - i, 0)
            need = max(need + 1, i + 1)
        return res
        
s = Solution()
N = 9
arr1 = [4, 5, 4, 1, 3, 7, 6, 3, 3]
print(s.minIncrements(arr1, N))