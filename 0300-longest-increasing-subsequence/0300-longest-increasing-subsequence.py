class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        
        def dp(i):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            
            count = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    count = max(count, 1 + dp(j))
            
            memo[i] = count
            return memo[i]
        
        result = 1
        for i in range(n):
            result = max(result, dp(i))
        return result