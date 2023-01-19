# import math
# class Solution:
    # def carpetBox(self, A,B,C,D):
    #     carpet = [A,B]
    #     carpet.sort()
    #     box = [C,D]
    #     box.sort()
    #     return self.carpetBoxHelper(carpet[0],carpet[1],box[0],box[1])
        
    # def carpetBoxHelper(self, A,B,C,D):
    #     moves = 0
    #     carpet = [A,B]
    #     carpet.sort()
    #     if carpet[0]*carpet[1]<=C*D:
    #         return moves
    #     elif carpet[0]*int(carpet[1]/2)<=C*D or int(carpet[0]/2)*carpet[1]<C*D:
    #         return moves+1
    #     else:
    #         return moves+self.carpetBoxHelper(carpet[0],int(carpet[1]/2),C,D)+1
    
class Solution:
    def carpetBox(self, A,B,C,D):
        #code here
        dp = dict()
        return self.solve(A,B,C,D,dp)

    def solve(self,a,b,c,d,dp):
        if (a,b) in dp:
            return dp[(a,b)]
        if max(a,b) <= max(c,d) and min(a,b) <= min(c,d):
            return 0
        x =10**9
        y = 10**9
        z = 10**9
        if min(a,b) < max(c,d):
            if a <= c or a <= d:
                x = self.solve(a,b//2,c,d,dp)+1
            if b<=c or b<=d:
                y = self.solve(a//2,b,c,d,dp)+1
        else:
            z = min(self.solve(a//2,b,c,d,dp),self.solve(a,b//2,c,d,dp)) + 1
        dp[(a,b)] = min(x,y,z)
        return dp[(a,b)]
s = Solution()
A = 836058373
B = 647572690
C = 97
D = 20
print(s.carpetBox(A,B,C,D))
