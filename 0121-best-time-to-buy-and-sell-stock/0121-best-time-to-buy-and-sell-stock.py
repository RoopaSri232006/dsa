class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum = prices[0]
        profit = 0

        for i in prices:
            minimum = min(minimum, i)
            profit = max(profit, i - minimum)

        return profit