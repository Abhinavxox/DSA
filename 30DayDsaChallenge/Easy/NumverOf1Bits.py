class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]
        binary = binary.zfill(32)
        return binary.count('1')

s = Solution()
n = 0b00000000000000000000000000001011
print(s.hammingWeight(n))