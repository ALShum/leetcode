## Build min cost at each steps by looking at the previous two steps
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            min_cost_prev = min(cost[i-1], cost[i-2])
            cost[i] = cost[i] + min_cost_prev
        return min(cost[-1], cost[-2])
