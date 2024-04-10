class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,'',1)
            else:
                return False
        return True


s = Solution()

print(s.canConstruct(ransomNote = "aa", magazine = "aab"))
print(s.canConstruct(ransomNote = "aab", magazine = "baa"))
print(s.canConstruct(ransomNote = "a", magazine = "b"))
print(s.canConstruct(ransomNote = "aa", magazine = "ab"))