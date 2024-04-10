from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Учитывая целочисленный массив, nums отсортированный в порядке неубывания, удалите несколько дубликатов на
        месте так, чтобы каждый уникальный элемент появлялся не более двух раз.
        Относительный порядок элементов должен оставаться неизменным.
        '''

        index = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[index] = nums[i]
                index += 1

        return index


s = Solution()

print(s.removeDuplicates(nums = [0,0,1,1,1,1,1,2,3,3]))