class Solution:
    def maximumToys(self,N,A,Q,Queries):
        answer = []
        for i in range(0,Q):
            arr = A.copy()
            C = Queries[i][0]
            K = Queries[i][1]
            
            #remove broken toys
            if K!=0:
                deletedCount = 0
                for counter in range(2,N):
                    if K==0:
                        break
                    arr.pop(Queries[i][counter]-1-deletedCount)
                    deletedCount +=1
                    K-=1
            
            #max possible toys
            arr.sort()
            count = 0
            for x in arr:
                if C-x>=0:
                    count+=1
                    C = C-x
                else:
                    break
            answer.append(count)
        return answer
        
s = Solution()
N = 5
A = [8,6,9,2,5]
Q = 2
Queries = [[12,2,3,4],[30,0]]
print(s.maximumToys(N,A,Q,Queries))
                

  

