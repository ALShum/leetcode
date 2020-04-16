# Keep stones inside a heap to always get the largest

import heapq ## heapq is minheap by default
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = []
        for s in stones:
            heapq.heappush(stone_heap, -s)
        while len(stone_heap) > 1:
            s1 = -heapq.heappop(stone_heap)
            s2 = -heapq.heappop(stone_heap)
            if s1 != s2:
                heapq.heappush(stone_heap, -abs(s1 - s2))

        return -stone_heap[0] if stone_heap else 0
