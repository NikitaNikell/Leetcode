class Solution:
    def isPalindrome(self, x: int) -> bool:
        """ Учитывая целое число x, верните true if x палиндром, и false иначе"""
        if len(str(x)) == 1:
            return True
        else:
            for i in range(len(str(x))//2):
                print(str(x)[i], str(x)[-1 - i])
                if str(x)[i] != str(x)[-1-i]:
                    return False
            return True


s = Solution()

print(s.isPalindrome(x = 1000021))