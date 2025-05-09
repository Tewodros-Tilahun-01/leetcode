class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = 0
        res = 0
        while right < len(nums):
            x = nums[right] - nums[left] 
            if x == 1:
                res = max(right-left+1,res)
                right += 1
            elif x > 1:
                left += 1
            else:
                right += 1
        return res