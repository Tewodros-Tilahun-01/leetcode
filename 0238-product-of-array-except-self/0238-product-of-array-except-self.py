class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sm = 1 
        num1 = []
        num2 = [0] * len(nums)
        for i in nums:
            num1.append(sm)
            sm *= i
        sm = 1
        for i in range(len(nums)-1,-1,-1):
            num2[i] = sm 
            sm *= nums[i]
            
        for i in range(len(nums)):
            nums[i] = num1[i] * num2[i]
        return nums
       