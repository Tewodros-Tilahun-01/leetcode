class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dp(i, can_buy):
            if i >= n:
                return 0
            if (i, can_buy) in memo:
                return memo[(i, can_buy)]

            if can_buy:
                profit = max(-prices[i] + dp(i + 1, False),dp(i + 1, True))
            else:
                profit = max(prices[i] + dp(i + 2, True),dp(i + 1, False))

            memo[(i, can_buy)] = profit
            return profit

        return dp(0, True)