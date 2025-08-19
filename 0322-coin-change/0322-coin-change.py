class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Handle edge cases
        if amount < 0 or not coins:
            return -1
        if amount == 0:
            return 0

        # Initialize DP array with infinity (or amount + 1 as sentinel)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # Sort coins to potentially skip larger coins
        coins.sort()

        # Bottom-up DP
        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:  # Skip coins larger than current amount
                    break
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # Return result or -1 if no solution exists
        return dp[amount] if dp[amount] != float('inf') else -1