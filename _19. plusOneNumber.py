from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num1 = int(''.join([str(i) for i in digits]))
        num1 += 1
        return [int(i) for i in str(num1)]


s = Solution()

print(s.plusOne(digits = [1,2,3]))
print(s.plusOne(digits = [4,3,2,1]))
print(s.plusOne(digits = [9, 9]))
