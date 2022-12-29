class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = bin(n)[2:]
        #as it is always 32 bit
        binary = binary.zfill(32)
        binary = binary[::-1]
        return int(binary, 2)


s = Solution()

n = 0b00000010100101000001111010011100
print(s.reverseBits(n))
