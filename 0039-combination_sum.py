## recursion, at each step, try adding the first element to sum or skipping the current element

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        def backTrack(candidates, s = [], cur = 0):
            if cur == target:
                solutions.append(s)
                return
            if len(candidates) == 0 or cur > target:
                return
            backTrack(candidates[1:], s, cur) #skip candidate
            backTrack(candidates,s + [candidates[0]], cur + candidates[0]) #try candidate
        backTrack(candidates, [], 0)
        return solutions
