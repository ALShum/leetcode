## Recurisve and iterative solutions

class Solution:
    def fib(self, N: int) -> int:
        return self.fib1(N)

    def fib1(self, N):
        prev1 = 0
        prev2 = 1
        if N <= 1:
            return N
        for i in range(1, N):
            n = prev1 + prev2
            prev1 = prev2
            prev2 = n
        return prev2

    def fib2(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib2(N - 1) + self.fib2(N - 2)
