## Iterate into a hashset or hashtable
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        A = set(nums1)
        B = set(nums2)
        return A.intersection(B)