class Solution:
    def strStr(self, haystack: str, needle: str): # -> int:
        return haystack.index(needle) if needle in haystack else -1


s = Solution()

print(s.strStr(haystack = 'sadbutsad', needle = 'sad'))
print(s.strStr(haystack = 'leetcode', needle = 'leeto'))