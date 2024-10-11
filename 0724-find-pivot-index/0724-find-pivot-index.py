class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightsum = sum(nums)
        leftsum = 0
        left = 0
        size = len(nums)
        while(left < size ):
            rightsum -= nums[left]
            print(rightsum,leftsum)
            if rightsum == leftsum:
                return left
            leftsum += nums[left]
            left += 1
        return -1
            