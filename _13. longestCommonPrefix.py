from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            if len(strs[0]) == 0:
                return ""
            else:
                return strs[0]
        else:
            rez = strs[0]
            for i in range(1, len(strs)):
                cur = strs[i]
                reader = 0
                lastCommon = 0
                while reader < len(rez) and reader < len(cur):
                    if rez[reader] == cur[reader]:
                        lastCommon += 1
                    else:
                        break
                    reader +=1
                rez = rez[:lastCommon]
            return rez


s = Solution()

#print(s.longestCommonPrefix(strs = ["flower","flow","flight"]))
#print(s.longestCommonPrefix(strs = ["flower"]))
print(s.longestCommonPrefix(strs = [""]))
