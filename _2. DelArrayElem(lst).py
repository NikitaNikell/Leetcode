from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> list[int]:
        nums[:] = [i for i in nums if i != val]
        k = len(nums)
        return k, nums


s = Solution()
print(s.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))




