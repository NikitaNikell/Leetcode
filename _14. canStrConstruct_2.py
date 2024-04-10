class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''Возможно ли из одной строки получить другую'''

        items = set(ransomNote)
        for i in items:
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True


s = Solution()

print(s.canConstruct(ransomNote = "aa", magazine = "aab"))
print(s.canConstruct(ransomNote = "aab", magazine = "baa"))
print(s.canConstruct(ransomNote = "total", magazine = "cteatetotal"))
