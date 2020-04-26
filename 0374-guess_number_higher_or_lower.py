# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, u = 1, n

        while l <= u:
            m = (l + u) // 2
            g = guess(m)
            if g == 0:
                return m
            if g < 0:
                u = m - 1
            else:
                l = m + 1
        return None