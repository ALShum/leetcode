## Given a collection of candidate numbers (candidates) and a target number (target),
## find all unique combinations in candidates where the candidate numbers sums to target.
##
## Each number in candidates may only be used once in the combination.
## All numbers (including target) will be positive integers.
## The solution set must not contain duplicate combinations

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        solution = []
        def backtrack(candidates, s = [], cur = 0):
            if cur == target:
                solution.append(s)
                return
            if len(candidates) == 0 or cur > target:
                return
            backtrack(candidates[1:], s + [candidates[0]], cur + candidates[0]) #each number can only be used once
            backtrack(candidates[1:], s, cur)
        backtrack(candidates, [], 0)
        solution = set([tuple(s) for s in solution]) #remove duplicates
        solution = [list(s) for s in solution]
        return solution
