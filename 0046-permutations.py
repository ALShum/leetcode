## Use backtracking with a loop to go through each element

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution = []
        orig_length = len(nums)
        def backtrack(nums, cur):
            if orig_length == len(cur):
                solution.append(cur)
                return
            if len(nums) == 0:
                return
            if len(nums) == 1:
                solution.append(cur + [nums[0]])
                return
            for i in range(0, len(nums)):
                backtrack(nums[:i] + nums[i+1:], cur + [nums[i]])
        backtrack(nums, [])
        return solution