class Solution(object):
    def xorBeauty(self, nums):
        n = len(nums)
        res = 0
        for i in range(n):
            res ^= nums[i]
        return res