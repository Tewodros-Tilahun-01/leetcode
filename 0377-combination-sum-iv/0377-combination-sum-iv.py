class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(target):
            if target == 0:
                return 1
            if target in memo:
                return memo[target]
            ways = 0
            for num in nums:
                if target - num >= 0:
                    ways += dp(target-num)
            memo[target] = ways
            return memo[target] 

        return dp(target)