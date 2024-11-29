class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even ,odd = 0,1
        while odd < len(nums) and even < len(nums):
            if not self.iseven(nums[even]) and self.iseven(nums[odd]):
                nums[odd], nums[even] =  nums[even], nums[odd]
                even += 2
                odd += 2
            else:
                if self.iseven(nums[even]):even += 2
                if not self.iseven(nums[odd]):odd += 2  
        return nums

    def iseven(self,i):
        return True if i % 2 == 0 else False