class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(nums, cur_pos, cur_set):
            print(cur_pos)
            if cur_pos == len(nums):
                ans.append(cur_set)
                return
            backtrack(nums, cur_pos+1, cur_set)
            backtrack(nums, cur_pos+1, cur_set + [nums[cur_pos]])
        backtrack(nums, 0, [])
        return ans