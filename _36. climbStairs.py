class Solution:
    def climbStairs(self, n: int) -> int:
        """ Подъем по лестнице
        Вы поднимаетесь по лестнице. Каждый раз можно либо карабкаться, 1 либо 2 ступеньками.
        Сколькими различными способами вы можете подняться на вершину? *почти как числа фиббоначи
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

s = Solution()

print(s.climbStairs(n = 2))