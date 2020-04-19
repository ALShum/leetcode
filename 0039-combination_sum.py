## recursion, at each step, try adding the first element to sum or skipping the current element

## Given a _set_ of candidate numbers (candidates) (without duplicates) and a target number (target),
## find all unique combinations in candidates where the candidate numbers sums to target.
##
## The same repeated number may be chosen from candidates unlimited number of times.
## Note:
## All numbers (including target) will be positive integers.
## The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        def backTrack(candidates, s = [], cur = 0):
            if cur == target:
                solutions.append(s)
                return
            if len(candidates) == 0 or cur > target: #(this only works because integers are positive)
                return
            backTrack(candidates[1:], s, cur) #skip candidate
            backTrack(candidates,s + [candidates[0]], cur + candidates[0]) #try candidate
        backTrack(candidates, [], 0)
        return solutions
