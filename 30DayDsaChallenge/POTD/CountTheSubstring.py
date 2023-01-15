class Solution():
    def countSubstring(self, S):
        # countOfOne = S.count('1')
        # if countOfOne==0:
        #     return 0
        # elif countOfOne==1:
        #     return 1
        # i = 0
        # j = 0
        # count = 0
        # lIndex = len(S)
        # while i<lIndex:
        #     s = S[i:j+1]
        #     if s.count('1')>(len(s)/2):
        #         count+=1
        #     j+=1
        #     if j==lIndex:
        #         i+=1
        #         j=1
        # return count

        res = [S[i: j] for i in range(len(S)) 
        for j in range(i + 1, len(S) + 1)]
        for i in range(len(res)):
            res[i] = 1 if res[i].count("1") > res[i].count('0') else 0
        return sum(res)

s = Solution()
S = '011'
print(s.countSubstring(S))
            

