class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = [] 
        i = 0
        while i < len(nums)/2:
            res.append(nums[i] + nums[-1-i])
            i += 1
        return max(res)