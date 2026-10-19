class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = prices[0]
        max_profit = 0

        for num in prices:
            if num < minimum_price:
                minimum_price = num

            if num - minimum_price > max_profit:
                max_profit = num - minimum_price
        
        return max_profit