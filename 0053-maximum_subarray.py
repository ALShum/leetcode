## Keep track of max_so_far and sum_to_current_position if sum is positive

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumToHere = 0
        maxSoFar = float('-inf')
        for n in nums:
            sumToHere += n
            maxSoFar = max(maxSoFar, sumToHere)
            if sumToHere < 0:
                sumToHere = 0
        return maxSoFar
