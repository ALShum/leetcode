## Binary search approach using looping

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            m = (left + right) // 2
            if m * m < x:
                left = m + 1
            elif m * m > x:
                right = m - 1
            else:
                return m
        return left - 1
