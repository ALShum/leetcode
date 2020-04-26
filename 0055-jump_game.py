class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach = [False] * len(nums)
        canReach[0] = True
        for i in range(len(nums)):
            if canReach[i]:
                if (i + nums[i]) < len(nums) - 1:
                    canReach[i:(i + nums[i] + 1)] = [True] * (nums[i] + 1)
                else:
                    return True
        return canReach[-1]
