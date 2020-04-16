## We could just calculate all distances and sort: nlogn
## Similarly we could calculate and stick inside a priority queue: nlogn
## If we use a heap, heapify (O(n)) and heappop() K times: klogn
import heapq
class Solution2:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ans = []
        ## this is dist**2, but it's monotonic so no need for sqrt
        dist_L = [(x**2 + y**2, x, y) for x,y in points]
        heapq.heapify(dist_L)
        for i in range(0, K):
            _, x, y = heapq.heappop(dist_L)
            ans.append([x,y])
        return ans

## We could also use a max_heap of size K and only store the k-closest, nlogk
## (this means we don't need to store a list of all the distances)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = []
        for x,y in points:
            dist = x**2 + y**2

            if len(h) < K:
                heapq.heappush(h, (-dist, x, y))
            else:
                d, _, _ = h[0]
                if dist < -d:
                    heapq.heappushpop(h, (-dist, x, y))

        return [hh[1:] for hh in h]
