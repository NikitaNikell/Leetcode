from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = prices[0], prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            right = prices[i]
            profit = right - left

            if profit > max_profit:
                max_profit = profit

            if left > right:
                left = right

        return max_profit


s = Solution()

print(s.maxProfit(prices=[7,1,5,3,6,4]))