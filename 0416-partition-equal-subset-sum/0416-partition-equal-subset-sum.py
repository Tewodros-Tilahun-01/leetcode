class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        dp = [0] * ((total//2) + 1)
        dp[0] = 1
        for num in nums:
            for i in range(len(dp)-1,-1,-1):
                if dp[i] == 1 and i + num < len(dp):
                    dp[i+num] = 1                    
        return dp[-1] == 1
                    



