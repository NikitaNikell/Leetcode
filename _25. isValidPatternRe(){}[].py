import re

class Solution:
    def isValid(self, s: str) -> bool:
        pattern = r'\(\)|\{\}|\[\]'
        while re.search(pattern, s):
            s = re.sub(pattern, '', s)
        return not s


s = Solution()


print(s.isValid(s = "()"))
print(s.isValid(s = "()[]{}"))
print(s.isValid(s = "(]"))

