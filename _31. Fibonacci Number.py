class Solution:
    def fib(self, n: int) -> int:
        """ Числа Фибоначчи,обычно обозначаемые, F(n)образуют последовательность, называемую последовательностью
        Фибоначчи , так что каждое число представляет собой сумму двух предыдущих, начиная с 0и 1. То есть,
        F(n) = F(n - 1) + F(n - 2), для n > 1.
        """
        if n == 0:
            return 0
        elif n in (1, 2):
            return 1
        else:
            a, b = 0, 1
            for i in range(2,n+1):
                a, b = b, a + b
            return b

s = Solution()
print(s.fib(4))