class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(index):
            if index >= len(cost):
                return 0  
            if index in memo:
                return memo[index]
            memo[index] = cost[index] + min(dp(index + 1), dp(index + 2))
            return memo[index]
        return min(dp(0), dp(1))