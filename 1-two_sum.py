## Store a mapping of num in array > index position
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in m and m[diff] != i:
                return [i, m[diff]]
            m[nums[i]] = i
        return []