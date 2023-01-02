class Solution(object):

    def get_digit(self, number, i):
        return int(str(number)[i])

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = n
        counter = 0
        try:
            while True :
                if m==1:
                    return True
                if counter == 10:
                    return False
                sum = 0
                for i in range(0, len(str(m))):
                    sum = sum + self.get_digit(m, i)**2
                m = sum
                counter += 1
        except:
            return False

s = Solution()
n = 2
print(s.isHappy(n))