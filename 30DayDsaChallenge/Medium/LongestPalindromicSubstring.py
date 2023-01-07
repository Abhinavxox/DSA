class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        if s[0] == s[-1]:
            return s[0] + self.longestPalindrome(s[1:-1]) + s[-1]
        else:
            return max(self.longestPalindrome(s[1:]), self.longestPalindrome(s[:-1]))

 
s = Solution()
string = "aacabdkacaa"
print(s.longestPalindrome(string))