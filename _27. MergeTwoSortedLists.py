# Definition for singly-linked list.

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        # Создаем фиктивный узел, чтобы иметь доступ к началу объединенного списка
        node = ListNode()
        current = node

        # Продолжаем слияние, пока есть узлы в обоих списках
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Если остались узлы в одном из списков, присоединяем их к объединенному списку
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Возвращаем начало объединенного списка (после фиктивного узла)
        return node.next




s = Solution()

print(s.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))