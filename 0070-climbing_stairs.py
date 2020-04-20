class Solution:
    ## Iterative solution with array
    def climbStairs2(self, n: int) -> int:
        if n <= 2:
            return n
        ary = [0] * n
        ary[0], ary[1] = 1, 2
        for i in range(2,len(ary)):
            ary[i] = ary[i-1] + ary[i-2]
        return ary[-1]

    ## Iterative solution similar to fibonacci
    def climbStairs(self, n):
        if n <= 2:
            return n
        prev1 = 1
        prev2 = 2
        for i in range(n-2):
            new = prev1 + prev2
            prev1 = prev2
            prev2 = new
        return new