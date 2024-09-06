class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j , z  = len(nums)-1 , len(nums)
        ans = [0] * len(nums)
        while i <= j:
            z -=1
            if abs(nums[i]) > abs(nums[j]):
                ans[z] = nums[i] * nums[i]
                i += 1
            else:
                ans[z] = nums[j] * nums[j]
                j -= 1
            
        ans[z] = nums[i] * nums[i]
        return ans