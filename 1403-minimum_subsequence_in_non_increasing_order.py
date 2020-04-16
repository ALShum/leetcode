## Sort and iterate from largest

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        total = sum(nums)
        nums = sorted(nums)[::-1]

        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s > total / 2:
                return nums[:i+1]
        return []