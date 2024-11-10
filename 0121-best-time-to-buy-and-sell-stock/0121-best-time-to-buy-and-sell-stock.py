class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_num = prices[0]
        for i in prices:
            min_num = min(min_num,i)
            max_profit = max(max_profit,i - min_num)
        return max_profit