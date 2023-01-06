class Solution(object):
    # def threeSum(self, nums):
    #     nums.sort()
    #     output = []
    #     for i in range(0, len(nums)):
    #         for j in range(i+1, len(nums)):
    #             for k in range(j+1, len(nums)):
    #                 if nums[i]+nums[j]+nums[k]==0:
    #                     out = [nums[i],nums[j],nums[k]]
    #                     if out not in output:
    #                         output.append(out)
    #     output.sort()
    #     return output

    #with less complexity
    def threeSum(self, nums):
        nums.sort()
        output = []
        hash = {}
        for i in range(0, len(nums)):
            sum = 0-nums[i]
            for j in range(0,len(nums)):
                if i==j:
                    break
                if sum-nums[j] not in hash:
                    hash[nums[j]] = j
                else:
                    out = [nums[i],nums[j],sum-nums[j]]
                    out.sort()
                    if out not in output:
                        output.append(out)  
            hash = {}     
        return output

s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))