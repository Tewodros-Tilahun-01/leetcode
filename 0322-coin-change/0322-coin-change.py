class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dp(n):
            if n < 0:
                return float("inf") 
            if n == 0:
                return 0  
            if n in memo:
                return memo[n]
            
            min_coins = float("inf")
            for coin in coins:
                min_coins = min(min_coins, 1 + dp(n - coin))
            memo[n] = min_coins
            return memo[n]
        
        result = dp(amount)
        return result if result != float("inf") else -1