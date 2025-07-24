class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_zero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                first_zero = i
                break
        if first_zero == -1:
            return 
        for i in range(len(nums)):
            if nums[i] != 0 and i > first_zero:
                nums[first_zero] , nums[i] = nums[i],nums[first_zero]
                first_zero += 1
        
