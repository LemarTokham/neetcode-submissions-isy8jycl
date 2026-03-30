class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(len(prices)-1, i, -1):
                profit = prices[j]-prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
