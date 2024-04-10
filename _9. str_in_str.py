class Solution:
    def strStr(self, haystack: str, needle: str): # -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1


s = Solution()

print(s.strStr(haystack = 'sadbutsad', needle = 'sad'))
print(s.strStr(haystack = 'leetcode', needle = 'leeto'))