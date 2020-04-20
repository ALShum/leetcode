## Track lowest price so far and current profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfitSoFar = 0
        lowestPriceSoFar = float('inf')
        for p in prices:
            lowestPriceSoFar = min(lowestPriceSoFar, p)
            profit = p - lowestPriceSoFar
            maxProfitSoFar = max(profit, maxProfitSoFar)
        return maxProfitSoFar
