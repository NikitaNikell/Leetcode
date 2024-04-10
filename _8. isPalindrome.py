class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        txt = ''.join(i.lower() for i in s if i.isalnum())
        return txt == txt[::-1]




s = Solution()

print(s.isPalindrome(s = "A man, a plan, a canal: Panama"))
print(s.isPalindrome(s = "race a car"))
print(s.isPalindrome(s = " "))
print(s.isPalindrome(s = "0П"))
