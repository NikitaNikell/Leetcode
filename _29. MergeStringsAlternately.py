class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        total = ""
        if len(word1) == len(word2):
            for i in range(len(word1)):
                total += word1[i]
                total += word2[i]

        elif len(word1) > len(word2):
            for i in range(len(word1)):
                if i < len(word2):
                    total += word1[i]
                    total += word2[i]
                else:
                    total += word1[i]

        elif len(word2) > len(word1):
            for i in range(len(word2)):
                if i < len(word1):
                    total += word1[i]
                    total += word2[i]
                else:
                    total += word2[i]
        return total




s = Solution()


print(s.mergeAlternately(word1 = "abc", word2 = "pqr")) # apbqcr
print(s.mergeAlternately(word1 = "ab", word2 = "pqrs")) # apbqrs
print(s.mergeAlternately(word1 = "abcd", word2 = "pq")) # apbqcd