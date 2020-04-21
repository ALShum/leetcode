## Reverse different segments of the array
## Becareful about indexing and mod k to make sure k < n

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        k %= len(nums)
        print(k)
        self.reverse(nums, 0, len(nums))
        self.reverse(nums, 0, k)
        self.reverse(nums, k, len(nums))

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end-1] = nums[end-1], nums[start]
            start += 1
            end -= 1