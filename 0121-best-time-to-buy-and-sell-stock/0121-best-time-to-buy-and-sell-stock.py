class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        profit = 0
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            profit = max(profit, prices[sell] - prices[buy])
            sell +=1
        return profit