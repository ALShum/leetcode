## Iterate through elements E and mark num[E] by flipping it into a string
## Check which element is unmarked

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            idx = int(nums[i])
            if idx < len(nums):
                nums[idx] = str(nums[idx])

        for i in range(len(nums)):
            if type(nums[i]) == int:
                return i
        return len(nums)