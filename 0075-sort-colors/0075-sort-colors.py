class Solution:
    def sortColors(self, nums):
        r = 0
        w = 0
        b = len(nums)-1

        while w <= b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                w += 1
                r += 1
            elif nums[w] == 1:w += 1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1 
                