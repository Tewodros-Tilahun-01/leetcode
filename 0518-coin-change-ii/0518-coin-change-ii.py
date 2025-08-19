class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(current_amount, index):
            if current_amount == 0:
                return 1
            if current_amount < 0 or index >= len(coins):
                return 0
            if (current_amount, index) in memo:
                return memo[(current_amount,index)]
            
            ways = 0
            if current_amount >= coins[index]:
                ways += dp(current_amount - coins[index], index)
            ways += dp(current_amount, index + 1)
            
            memo[(current_amount, index)] = ways
            return ways
        
        return dp(amount, 0)