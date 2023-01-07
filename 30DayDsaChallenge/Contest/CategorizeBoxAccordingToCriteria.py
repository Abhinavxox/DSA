class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        if length >= 10**4 or width >= 10**4 or height >= 10**4 or length * width * height >= 10**9:
            if mass >= 100:
                return "Both"
            else:
                return "Bulky"
        else:
            if mass >= 100:
                return "Heavy"
            else:
                return "Neither"

s = Solution()
print(s.categorizeBox(1000, 35, 700, 300))

