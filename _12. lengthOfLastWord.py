class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


s = Solution()

print(s.lengthOfLastWord(s = "Hello World"))
print(s.lengthOfLastWord(s = "fly me   to   the moon"))
print(s.lengthOfLastWord(s = "luffy is still joyboy"))
