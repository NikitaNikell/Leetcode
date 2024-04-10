from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """ Учитывая массив целых чисел nums и целое число target,
        верните индексы двух чисел так, чтобы их сумма составляла target.
        """
        numMap = {}
        l = len(nums)

        for i in range(l):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        return []


s = Solution()

print(s.twoSum(nums = [2,7,11,15], target = 9))     #[0,1]
# print(s.twoSum(nums = [3,2,4], target = 6))         #[1,2]
# print(s.twoSum(nums = [3,3], target = 6))           #[0,1]
# print(s.twoSum(nums = [3,2,3], target = 6))         #[0,2]
# print(s.twoSum(nums = [2,5,5,11], target = 10))     #[1,2]
# print(s.twoSum(nums = [2,5], target = 10))          #[]