class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dp(i,current_sum):
            if i == n:
                return 1 if current_sum == target else 0
            if (i,current_sum) in memo:
                return memo[(i,current_sum)]
            ways = dp(i+1, current_sum + nums[i]) + dp(i+1,current_sum - nums[i])
            memo[(i,current_sum)] = ways
            return ways
        return dp(0,0)
    
        