class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = prices[0]
        max_price = 0
        best = 0

        for price in prices:
            minimum_price = min(minimum_price, price)
            profit = price - minimum_price

            best = max(best, profit)

        return best
            