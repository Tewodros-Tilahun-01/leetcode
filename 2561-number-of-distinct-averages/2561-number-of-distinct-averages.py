class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        res = set()
        left , right  = 0 , len(nums)-1
        while left < right:
            res.add( (nums[left] + nums[right]) / 2 )
            left +=1 
            right -= 1
        return len(res)