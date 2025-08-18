class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(step):
            if step >= n:
                return 1 if step == n else 0
            if step in memo:
                return memo[step]
            res = 0
            res += dp(step+1)
            res += dp(step+2)
            if step not in memo:
                memo[step] = res
            return res

        return dp(0)
