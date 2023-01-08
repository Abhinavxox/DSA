class Solution:
    def countPairs (self, n, arr, k):
        # code here
        
        # count = 0
        # i=0
        # j=n-1
        # while(i<j):
        #     if(abs(arr[i]-arr[j])%k==0):
        #         count+=1
        #     j-=1
        #     if(j==i):
        #         i+=1
        #         j=n-1
        # return count
        # intialize the count
        
        count = 0
        for i in range(n):
            arr[i] = (arr[i] + k) % k
      
        hash = [0]*k
      
        for i in range(n):
            hash[arr[i]] += 1
      
        for i in range(k):
            count += (hash[i] * (hash[i] - 1)) // 2
      
        return count

s = Solution()
n = 10
arr = [5,5,10,10,2,1,7,8,9,5]
k = 3
print(s.countPairs(n,arr,k))
