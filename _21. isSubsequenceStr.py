class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Можно-ли из строки t собрать строку s, при этом по строке t можно пройтись
        один раз слева-направо для подбора букв.
        """

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)



s = Solution()

#print(s.isSubsequence(s = "abc", t = "ahbgdc"))
#print(s.isSubsequence(s = "axc", t = "ahbgdc"))
print(s.isSubsequence(s = "acb", t = "ahbgdc"))
#print(s.isSubsequence(s = "ab", t = "baab"))