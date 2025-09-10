class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        index = 0
        
        while index < len(nums):
            if nums[index] != nums[nums[index]-1]:
               nums[nums[index]-1] , nums[index] =  nums[index] , nums[nums[index]-1]
            else:
                index += 1
                
        for i in range(1,len(nums)+1):
            if i != nums[i-1]:
                res.append(nums[i-1])

        return res
