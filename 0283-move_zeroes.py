## use a pointer to keep track of the insertion position at beginning of list

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pt_nonzero = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i], nums[pt_nonzero] = nums[pt_nonzero], nums[i]
                pt_nonzero+=1
