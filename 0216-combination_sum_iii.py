## Find all possible combinations of k numbers that add up to a number n,
## given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

## All numbers will be positive integers.
## The solution set must not contain duplicate combinations.
## No duplicate elements, in range(1,10) so we don't need to prune duplicate solutions
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        solution = []
        elements = list(range(1, 10))
        def backtrack(elem = elements, s = [], cur = 0):
            if cur == n and len(s) == k:
                solution.append(s)
                return
            if cur > n or len(s) > k or len(elem) < 1:
                return
            backtrack(elem[1:], s + [elem[0]], cur + elem[0])
            backtrack(elem[1:], s, cur)
        backtrack(elements, [], 0)
        return solution
