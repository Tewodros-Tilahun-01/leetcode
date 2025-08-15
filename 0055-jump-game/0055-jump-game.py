class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        n = len(nums)
        for i in range(n):
            if max_jump >= n-1:
                return True
            if max_jump < i:
                return False
            max_jump = max(max_jump,i+nums[i])
        return False