class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        def binarysearch(left,right):
            index = -1
            while left <= right:
                mid =( left + right)//2
                if nums[mid] >= target:
                    right = mid - 1 
                else:
                    left = mid + 1
                if nums[mid] == target:
                    index = mid
            return index
        index = binarysearch(0,len(nums)-1)
        while index < len(nums) and index != -1:
            if nums[index] == target:
                res.append(index)
            else:
                break
            index += 1
        return res
