class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k= k % len(nums)
        for i in range( len(nums) // 2):
            nums[i] , nums[-1-i] = nums[-1-i], nums[i]
        for i in range( k // 2 ):
            nums[i] , nums[k-i-1] = nums[k-i-1],  nums[i]
        for i in range( k, ( k + len(nums) ) // 2 ):
            nums[i] , nums[k-i-1] = nums[k-i-1],  nums[i] 
        
        


