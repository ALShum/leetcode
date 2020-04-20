class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)

        if len(nums) <= 2:
            return max(nums)

        largest1 = float('-inf')
        largest2 = float('-inf')
        largest3 = float('-inf')

        for n in nums:
            if n > largest1:
                largest3 = largest2
                largest2 = largest1
                largest1 = n
            elif n > largest2:
                largest3 = largest2
                largest2 = n
            elif n > largest3:
                largest3 = n
        return largest3