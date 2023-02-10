class Solution:
    def minimizeSum(self, N, arr):
        
        # arr.sort()
        # minSum = 0
        # while(N>1):
        #     sum = arr[0]+arr[1]
        #     minSum += sum
        #     arr = arr[2:]
        #     arr.append(sum)
        #     arr.sort()
        #     N-=1
        # return minSum

        #with less complexity
        # arr.sort()
        # minSum = 0
        # while(N>1):
        #     sum = arr[0]+arr[1]
        #     minSum += sum
        #     arr = arr[2:]
        #     pointer = 0
        #     flag = False
        #     if(len(arr)!=0):
        #         while(not flag):
        #             if (len(arr)==0 or pointer>=len(arr)):
        #                 break
        #             if(sum<=arr[pointer]):
        #                 arr.insert(pointer, sum)
        #                 flag = True
        #             pointer +=1     
        #         if (not flag):
        #             arr.append(sum)      
        #     N-=1
        # return minSum

        #with less complexity and less space using min heap
        self.insert(arr)
        minSum = 0
        while(N>1):
            sum = arr[0]+arr[1]
            minSum += sum
            arr = arr[2:]
            arr.append(sum)
            self.insert(arr)
            N-=1
        return minSum


    def Minheapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.Minheapify(arr, n, largest)

    def insert(self, arr):
        n = len(arr)
        for i in range(n, -1, -1):
            self.Minheapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.Minheapify(arr, i, 0)

s = Solution()
N = 5
arr = [2, 4, 7, 1, 2]
print(s.minimizeSum(N, arr))


