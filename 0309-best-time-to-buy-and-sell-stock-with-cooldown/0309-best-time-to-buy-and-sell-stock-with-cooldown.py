class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        
        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            best = dp(i + 1)
        
            for j in range(i + 1, n):
                if prices[j] > prices[i]:
                    best = max(best, prices[j] - prices[i] + dp(j + 2))
            memo[i] = best
            return memo[i]
        
        return dp(0)