class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([str(i) for i in s.split()[::-1]])



s = Solution()

print(s.reverseWords(s = "the sky is blue"))    # blue is sky the
print(s.reverseWords(s = "  hello world  "))    # world hello