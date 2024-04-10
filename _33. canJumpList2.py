from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """ Возвращает минимальное количество прыжков для достижения nums [n - 1].
        Тестовые случаи генерируются таким образом, что вы можете достичь nums[n - 1].
        """
        reach, count, last = 0, 0, 0
        for i in range(len(nums)-1):
            reach = max(reach, i + nums[i])

            if i == last:
                last = reach
                count += 1
        return count

s = Solution()


print(s.jump(nums = [2,3,1,1,4]))


