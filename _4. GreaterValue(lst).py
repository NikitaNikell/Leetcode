from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        k = len(nums)//2
        return nums[k]



s = Solution()

print(s.majorityElement([-1,1,1,1,2,1]))