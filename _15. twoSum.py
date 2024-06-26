from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """ Учитывая массив целых чисел nums и целое число target,
        верните индексы двух чисел так, чтобы их сумма составляла target.
        """

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []   # No solution found


s = Solution()

print(s.twoSum(nums = [2,7,11,15], target = 9))     #[0,1]
print(s.twoSum(nums = [3,2,4], target = 6))         #[1,2]
print(s.twoSum(nums = [3,3], target = 6))           #[0,1]
print(s.twoSum(nums = [3,2,3], target = 6))         #[0,2]
print(s.twoSum(nums = [2,5,5,11], target = 10))     #[1,2]
print(s.twoSum(nums = [2,5], target = 10))          #[]


