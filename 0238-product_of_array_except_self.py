## 1. Create a Left product array L[i] = L[i - 1] * nums[i - 1]
## 2. Create a Right product array R[i] = R[i + 1] * nums[i + 1]
## 3. ans[i] = L[i] * R[i]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [1] * len(nums)
        R = [1] * len(nums)
        ans = [1] * len(nums)

        for i in range(1, len(nums)):
            L[i] = L[i-1] * nums[i-1]
            R[len(nums) - i-1] = R[len(nums) - i] * nums[len(nums) - i]

        for i in range(0, len(nums)):
            ans[i] = L[i] * R[i]
        return ans