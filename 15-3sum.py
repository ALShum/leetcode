class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(0, len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            if i != 0 and nums[i] == nums[i - 1]: #duplicates
                continue
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while (j < k and nums[j] == nums[j-1]): #duplicates
                        j+=1
        return ans