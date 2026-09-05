class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = -1
        for i in range(0,len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > bestProfit:
                    bestProfit = prices[j] - prices[i]

        return bestProfit