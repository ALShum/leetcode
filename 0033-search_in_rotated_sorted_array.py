## 1. Do a binary search to find the pivot element
##    check if nums[mid] > nums[mid + 1]
##    check if nums[mid - 1] > nums[mid]
##    adjust L, R, check if nums[L] >= nums[mid], this means the pivot is on the left
##    otherwise nums[L] < nums[mid], this means pivot is on the right

## 2. Do binary search on both sides of pivot element, if not pivot do a binary search on whole list
##    Becareful about off by one: to handle edge case [3,1], target = 3, when pivot element is 0,
##    make sure the Left Binary Search ranges from 0 to pivot + 1

class Solution:
    def search(self, nums, target: int):
        pivot = self.findPivot(nums)
        if pivot is None:
            return self.binarySearch(nums, 0, len(nums), target)

        L = self.binarySearch(nums, 0, pivot + 1, target)
        R = self.binarySearch(nums, pivot, len(nums), target)
        if L < 0 and R < 0:
            return -1
        return L if L >= 0 else R

    def findPivot(self, nums):
        if len(nums) <= 1:
            return None
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if m < r and nums[m] > nums[m + 1]:
                return m
            if l < m and nums[m] < nums[m - 1]:
                return m - 1
            if nums[l] >= nums[m]:
                r = m - 1
            else:
                l = m + 1
        return None

    def binarySearch(self, nums, l, r, tar):
        while l < r:
            m = (l + r) // 2
            if nums[m] == tar:
                return m
            if nums[m] < tar:
                l = m + 1
            elif tar < nums[m]:
                r = m
        return -1
