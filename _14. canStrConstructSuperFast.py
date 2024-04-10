from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ''' Возможно ли из строки: magazine собрать строку: ransomNote
        решение с помощью сравнение пересечений '''
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False


s = Solution()

#print(s.canConstruct(ransomNote = "aa", magazine = "aab"))
print(s.canConstruct(ransomNote = "aab", magazine = "baa"))
#print(s.canConstruct(ransomNote = "a", magazine = "b"))
#print(s.canConstruct(ransomNote = "aa", magazine = "ab"))