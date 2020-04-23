## Sieve of Eratosthenes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        n = n - 1 #since find primes < n not <= n
        sieve = [1] * n
        sieve[0] = False # 1 is not a prime
        for i in range(1, n):
            num = (i + 1)
            d = num + num
            while d < n + 1:
                sieve[d - 1] = 0
                d += num
        return sum(sieve)
