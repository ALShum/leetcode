## KthLargest using a min-heap to store largest elements
## new elements are compared to the smallest item in heap
## if new element is larger, pop out smallest item and replace with new element

import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        for n in nums:
            self._heap_insert(n)

    def add(self, val: int) -> int:
        self._heap_insert(val)
        return self.h[0]

    def _heap_insert(self, elem):
        if len(self.h) < self.k:
            heapq.heappush(self.h, elem)
        else:
            if elem > self.h[0]:
                heapq.heappushpop(self.h, elem)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)