## Since we can have more than one transaction with no fees
## Just buy if the previous price is lower than current price and add those to profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitSoFar = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profitSoFar += prices[i] - prices[i - 1]
        return profitSoFar
