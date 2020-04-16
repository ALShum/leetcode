## Notice the stop condition is L<=R, this better handles the edge case where array is size 1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            print((L, R))
            m = (L + R) // 2
            print(m)
            if nums[m] == target:
                return m
            if target < nums[m]:
                R = m - 1
            else:
                L = m + 1
        return -1
