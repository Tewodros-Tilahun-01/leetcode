class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums
        pt1, pt2 = 0 , 1
        while pt1 < n and pt2 < n :
            if not self.isEven(nums[pt1]) and  self.isEven(nums[pt2]) :
                nums[pt1] , nums[pt2] = nums[pt2] , nums[pt1]
                pt1 += 1
                pt2 += 1
            else:
                if self.isEven(nums[pt1]):
                    pt1 += 1
                    pt2 += 1
                elif not self.isEven(nums[pt2]):
                    pt2 += 1
            
        return nums

    def isEven(self,i):
        return i%2 == 0