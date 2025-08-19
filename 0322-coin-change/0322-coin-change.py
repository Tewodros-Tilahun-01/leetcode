class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(n,count):
            if n <= 0:
                return 0 if n == 0 else amount
            if n in memo:return memo[n]
            min_coin = float("inf")
            for coin in coins:
                min_coin = min(min_coin,1 + dp(n-coin,count+1))
            memo[n] = min_coin
            return memo[n]
        res = dp(amount,1) 
        return res if res <= amount else -1
