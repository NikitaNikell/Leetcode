from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        for i in range(m):
            nums3.append(nums1[i])
        for i in range(n):
            nums3.append(nums2[i])

        for i, num in enumerate(sorted(nums3)):
            nums1[i] = num

        return nums1


s = Solution()

print(s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))