## Calculate frequencies, stream elements into a minheap and keep top K largest

## Your algorithm's time complexity must be better than O(n log n), where n is the array's size
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        h = []
        for key,val in freq.items():
            if len(h) < k:
                heapq.heappush(h, (val, key))
            else:
                _val,_key = h[0]
                if val > _val:
                    heapq.heappushpop(h, (val, key))

        return [val for key,val in h]