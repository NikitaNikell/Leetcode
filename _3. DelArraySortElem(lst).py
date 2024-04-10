from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(sorted(set(nums)))
        k = len(nums)
        return k


s = Solution()

print(s.removeDuplicates(nums = [-1,0,0,0,0,3,3]))

