class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thous = ["", "M", "MM", "MMM", "MMMM"]

        return thous[num // 1000] + hunds[num // 100 % 10] + tens[num // 10 % 10] + ones[num % 10]


s = Solution()
print(s.intToRoman(num = 3))
print(s.intToRoman(num = 1994))
