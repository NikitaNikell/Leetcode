from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return sorted(nums).index(target)

        elif target > sorted(nums)[-1]:
            return len(nums)

        else:
            ans = 0
            for i in nums:
                if target < i:
                    continue
                else:
                    ans += 1
            return ans


s = Solution()

print(s.searchInsert(nums = [1,3,5,6], target = 5))    # 2
print(s.searchInsert(nums = [1,3,5,6], target = 2))    # 1
print(s.searchInsert(nums = [1,3,5,6], target = 7))    # 4
print(s.searchInsert(nums = [1,3,5], target = 4))      # 2
print(s.searchInsert(nums = [-1,3,5,6], target = 0))   # 1