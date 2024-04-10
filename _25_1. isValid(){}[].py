class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(' : ')',
                 '{' : '}',
                 '[' : ']'
                 }

        for perem in s:
            if perem in pairs.keys():
                stack.append(perem)
            elif len(stack) == 0 or perem != pairs[stack.pop()]:
                return False

        return len(stack) == 0


s = Solution()

print(s.isValid(s = "()"))
print(s.isValid(s = "()[]{}"))
print(s.isValid(s = "(]"))



