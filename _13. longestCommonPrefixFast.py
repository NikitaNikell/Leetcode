from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        s = sorted(strs)    # сортируем список
        s1 = s[0]           # первый элемент в списке
        s2 = s[-1]          # последний элемент в списке

        for r1, r2 in zip(s1, s2):
            if r1 != r2:
                break
            else:
                answer += r1
        return answer


s = Solution()

print(s.longestCommonPrefix(strs = ["flower","flow","flight"]))
print(s.longestCommonPrefix(strs = ["flower"]))
print(s.longestCommonPrefix(strs = [""]))