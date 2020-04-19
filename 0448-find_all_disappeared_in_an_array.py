## since nums is [1,n], iterate through range(1,n) and flip the elements we see
## the missing numbers are related to the unflipped integer positions

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) -1
            nums[idx] = abs(nums[idx]) * -1
        nums = [i + 1 for i in range(len(nums)) if nums[i] > 0]
        return nums
