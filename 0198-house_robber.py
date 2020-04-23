class Solution:
    ## Backtracking approach
    def rob2(self, nums: List[int]) -> int:
        def backTrack(houses, cur = 0, s = 0):
            if cur >= len(houses):
                return s
            return max(backTrack(houses, cur+1, s), backTrack(houses, cur+2, s + houses[cur]))
        return backTrack(nums, 0, 0)

    ## DP with array
    def rob1(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        money = [0] * len(nums)
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            option1 = nums[i] + money[i - 2]
            option2 = max(money[i - 1], money[i - 2])
            money[i] = max(option1, option2)
        return money[-1]

    ## DP constant memory
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        prev1 = nums[0]
        prev2 = max(nums[0], nums[1])
        maxSoFar = 0
        for i in range(2, len(nums)):
            option1 = nums[i] + prev1
            option2 = max(prev1, prev2)
            maxSoFar = max(maxSoFar, option1, option2)
            prev1 = prev2
            prev2 = max(option1, option2)
        return maxSoFar