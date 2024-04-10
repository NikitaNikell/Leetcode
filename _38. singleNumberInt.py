from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for i in nums:
            unique ^= i
        return unique



s = Solution()
print(s.singleNumber(nums = [4,1,2,1,2]))