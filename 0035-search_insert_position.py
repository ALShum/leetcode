## Binary search with a slightly different failure ending condition

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = 0
        def searchInsertInner(nums, target, L, R):
            nonlocal ans
            if L >= R:
                ans = L
                return
            m = (L + R) // 2
            if nums[m] == target:
                ans = m
                return
            if nums[m] < target:
                searchInsertInner(nums, target, m+1, R)
            if nums[m] > target:
                searchInsertInner(nums, target, L, m)
        searchInsertInner(nums, target, 0, len(nums))
        return ans
