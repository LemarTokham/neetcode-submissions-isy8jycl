class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: # can't have profit if only 1 day
            return 0
        maxProfit = 0
        l = 0
        r = l+1
        while r < len(prices):
            currProfit = prices[r] - prices[l]
            print(currProfit)
            if currProfit < 0: # Check for cheaper day in future
                l=r
                r=l+1
                continue
            if currProfit > maxProfit:
                maxProfit = currProfit
            r += 1
        return maxProfit