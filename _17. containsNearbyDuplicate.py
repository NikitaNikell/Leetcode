from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = {}
        for i in range(len(nums)):
            if nums[i] in store and i - store[nums[i]] <=k:
                return True
            store[nums[i]] = i
        return False




s = Solution()

print(s.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))   # true
print(s.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))   # true
print(s.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))   # false