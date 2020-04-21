## sort both and use two pointers (nlogn + mlogm)
## hashmap (n + m, o(n) storage)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        ans = []
        for n in nums1:
            m[n] = m.get(n, 0) + 1
        for n in nums2:
            if m.get(n,0) > 0:
                m[n] = m.get(n) - 1
                ans.append(n)
        return ans
