## Check if num[i-1] < num[i], if not reset start_position and calculate longestSoFar

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longestSoFar = 0
        prev = float('-inf')

        start_pos = 0
        for i in range(len(nums)):
            if prev < nums[i]:
                longestSoFar = max(longestSoFar, i - start_pos + 1)
            else:
                start_pos = i
            prev = nums[i]
        return longestSoFar