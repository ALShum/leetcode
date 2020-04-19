## Modify simple binary search so that even if we find target we do additional searchs
## Keep track of min / max index positions for things that we found so far

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx_range = [float('inf'), float('-inf')]
        found = False

        def searchRangeInner(nums, l, u, target):
            if l >= u:
                return
            m = (l + u) // 2
            if nums[m] < target:
                searchRangeInner(nums, m+1, u, target)
            if nums[m] > target:
                searchRangeInner(nums, l, m, target)
            if nums[m] == target:
                nonlocal found
                found = True
                idx_range[0] = min(m, idx_range[0])
                idx_range[1] = max(m, idx_range[1])
                searchRangeInner(nums, m+1, u, target)
                searchRangeInner(nums, l, m, target)

        searchRangeInner(nums, 0, len(nums), target)
        if not found:
            return [-1, -1]
        return idx_range
