from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)

        nums[:] = nums[-k:] + nums[:-k]
        return nums

s = Solution()

print(s.rotate(nums = [1,2,3,4,5,6,7], k = 3))
print(s.rotate(nums = [-1,-100,3,99], k = 2))
print(s.rotate(nums = [1, 2], k = 5))
print(s.rotate(nums = [1, 2, 3], k = 4))