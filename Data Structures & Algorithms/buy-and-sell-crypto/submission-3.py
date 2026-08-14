class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for sell in prices:
            profit = max(profit, sell-buy)
            buy = min(buy, sell)

        return profit