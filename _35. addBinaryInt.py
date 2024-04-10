class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """ Даны две двоичные строки a и b, верните их сумму в виде двоичной строки. """
        x = int(a, 2)
        y = int(b, 2)
        asn = bin(x + y)[2:]
        return asn


s = Solution()

print(s.addBinary(a = "1010", b = "1011"))