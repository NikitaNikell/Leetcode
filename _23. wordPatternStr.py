class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) == len(s.split()):
            return len(set(s.split())) == len(set(pattern)) == len(set(zip(pattern, s.split())))
        else:
            return False


s = Solution()

print(s.wordPattern(pattern = "abba", s = "dog cat cat dog"))
print(s.wordPattern(pattern = "abba", s = "dog cat cat fish"))
print(s.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
