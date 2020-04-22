## Check for overflows:
## n > 2 ** 31 // 10 then 10 * n > max int
## note that (2 ** 31 // 10) * 10 + 8 == max int

class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x = abs(x)
        n = 0
        while x > 0:
            d = x % 10
            x = x // 10

            ## Check for overflows
            if n > 2**31 // 10 or n == 2**31 // 10 and d > 7:
                return 0
            n = n * 10 + d
        return n if not neg else -n
