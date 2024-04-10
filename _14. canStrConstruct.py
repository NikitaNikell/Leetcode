from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''Возможно ли из строки: magazine собрать строку: ransomNote
        решение с помощью подсчета количества каждого символа в строке
        '''

        if len(ransomNote) > len(magazine):
            return False
        else:
            srts1 = dict(Counter(ransomNote))
            srts2 = dict(Counter(magazine))
            for key, value in srts1.items():
                if key not in srts2 or value > srts2[key]:
                    return False
                else:
                    continue
            return True


s = Solution()

print(s.canConstruct(ransomNote = "aa", magazine = "aab"))
print(s.canConstruct(ransomNote = "aab", magazine = "baa"))
print(s.canConstruct(ransomNote = "a", magazine = "b"))
print(s.canConstruct(ransomNote = "aa", magazine = "ab"))
