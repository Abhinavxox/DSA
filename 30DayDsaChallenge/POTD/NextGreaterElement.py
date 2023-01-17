class Solution:
    def nextLargerElement(self,arr,n):
        i = 0
        j = i+1
        output = []
        while(i<n):
            if i==n-1:
                output.append(-1)
                break
            if arr[i]<arr[j]:
                output.append(arr[j])
            j+=1
            if j==n-1:
                i+=1
                j=i+1
        return output 

s = Solution()
arr = [6,8,0,1,3]
n = 5
print(s.nextLargerElement(arr,n))