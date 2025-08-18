class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(step):
            if step >= n:
                return 1 if step == n else 0  
            if step not in memo:
                memo[step] = dp(step+1) + dp(step+2)
            return memo[step]
        return dp(0)
