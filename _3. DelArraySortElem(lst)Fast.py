from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        newSet = set(nums)
        nums.clear()
        nums.extend(sorted(newSet))
        return len(nums)


s = Solution()

print(s.removeDuplicates(nums = [-1,0,0,0,0,3,3]))