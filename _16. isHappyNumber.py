class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        while n > 9:
            total = sum([int(i)**2 for i in str(n)])
            if total == 1 or total == 7:
                return True
            else:
                return s.isHappy(total)

        return False



s = Solution()

print(s.isHappy(n = 19))
print(s.isHappy(n = 1))
print(s.isHappy(n = 7))
print(s.isHappy(n = 2))