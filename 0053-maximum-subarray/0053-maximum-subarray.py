class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = float("-inf")
        current_max = float("-inf")
        for num in nums:
            current_max = max(num,current_max + num)
            max_sum = max(max_sum,current_max)
        return max_sum
