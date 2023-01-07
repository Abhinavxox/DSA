import sys
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        output = []
        hash = {}
        for x in range(0,len(nums)):
            for i in range(x+1, len(nums)):
                t = target-nums[x]
                t = t-nums[i]
                j = i+1
                k = len(nums)-1
                while j<k:
                    sum = nums[j]+nums[k]
                    if sum == t: 
                        out = [nums[x],nums[i],nums[j],nums[k]]
                        if out not in output:
                            output.append(out)
                    if sum<t:
                        j+=1
                    elif sum>t:
                        k-=1
                    else:
                        j+=1
                        k-=1
        return output
    
s = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
print(s.fourSum(nums, target))