class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = prices[0]
        max_profit = 0

        for price in prices:
            minimum_price = min(price, minimum_price)
            profit = price - minimum_price
            max_profit = max(profit,max_profit)
        
        return max_profit