class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Initialize DP array
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: one way to make sum 0 (empty combination)
        
        # Iterate through all sums from 1 to target
        for i in range(1, target + 1):
            # For each sum, try all numbers in nums
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        
        return dp[target]