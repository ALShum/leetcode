## Two pointer solution but also track closest so far

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest_so_far = float('inf')
        closest_sum = None
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                dist = abs(target - s)
                if dist < closest_so_far:
                    closest_so_far = dist
                    closest_sum = s

                if s < target:
                    j+=1
                elif s > target:
                    k-=1
                else:
                    return closest_sum
        return closest_sum