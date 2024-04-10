from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ найти длину самой длинной последовательности списка """
        if not nums:
            return 0

        num_set = set(nums)
        res = 0
        for num in num_set:
            if (num - 1) not in num_set:
                length = 0
                while (num + length) in num_set:
                    length += 1
                res = max(res, length)
        return res

s = Solution()

#print(s.longestConsecutive(nums = [100,4,200,1,3,2]))
#print(s.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive(nums = [9,1,4,7,3,-1,0,5,8,-1,6]))