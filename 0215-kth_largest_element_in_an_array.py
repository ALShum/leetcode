import heapq
class Solution:
    ## Quick selection algorithm
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.heapFindMaxK(nums, k)

    def heapFindMaxK(self, nums, k):
        h = nums[:k]
        heapq.heapify(h)
        rest = nums[k:]

        for n in rest:
            if n > h[0]:
                heapq.heappushpop(h, n)
        return h[0]

    def quickSelect(self, nums, k):
        low, high = 0, len(nums)
        #convert k-largest to equivalent k-smallest
        k = len(nums) - k + 1

        #k-smallest
        while low < high:
            pivot = nums[low]
            idx = low + 1
            for i in range(low + 1, high):
                if nums[i] < pivot:
                    nums[i], nums[idx] = nums[idx], nums[i]
                    idx += 1
            nums[low], nums[idx - 1] = nums[idx - 1], nums[low]

            if idx - 1 == k - 1:
                return nums[idx - 1]
            if idx - 1 < k - 1:
                low = idx
            elif idx - 1 > k - 1:
                high = idx - 1
        return None

