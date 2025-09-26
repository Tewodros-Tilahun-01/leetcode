class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        add = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                add += 1       
            res += add
        
        return res