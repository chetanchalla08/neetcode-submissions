class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best = 0

        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            best = max(best, profit)
        
        return best
