class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            num = abs(nums[i])
            nums[num-1] = -abs(nums[num-1]) 
        
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)

        return res
