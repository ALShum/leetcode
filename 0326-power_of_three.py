## Loop by dividing by until the result is 1 or < 1

import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        epsilon = 0.001
        return abs(math.log(n, 3) % 1) <= 2 * epsilon
#Could you do it without using any loop / recursion?
