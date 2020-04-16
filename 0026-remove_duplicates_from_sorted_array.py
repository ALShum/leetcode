## Use a two-pointer solution
## i,j, iterate j num at j is duplicate with num at i.
## otherwise, the next i-th element is set to num at j.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(0, len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i+=1
        return i+1
