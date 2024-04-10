from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Учитывая целочисленный массив, nums отсортированный в порядке неубывания, удалите несколько дубликатов на
        месте так, чтобы каждый уникальный элемент появлялся не более двух раз.
        Относительный порядок элементов должен оставаться неизменным.
        '''

        nums1 = []
        for i in nums:
            if nums1.count(i) < 2:
                nums1.append(i)
        nums[:] = nums1
        return len(nums)



s = Solution()
print(s.removeDuplicates(nums = [1,1,1,2,2,3]))
print(s.removeDuplicates(nums = [0,0,1,1,1,1,1,2,3,3]))
