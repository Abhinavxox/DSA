class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z']
        }
        if digits=="":
            return []
        elif len(digits)==1:
            return dict[digits]
        else:
            return [x+y for x in dict[digits[0]] for y in self.letterCombinations(digits[1:])]
s = Solution()
digits = "23"
print(s.letterCombinations(digits))

