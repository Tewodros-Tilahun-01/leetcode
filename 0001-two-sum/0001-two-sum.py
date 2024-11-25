class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pt1 = 0
        while pt1 < len(nums) - 1:
            pt2 = pt1 + 1
            while pt2 < len(nums):
                if nums[pt1] + nums[pt2] == target:
                    return [pt1,pt2]
                pt2 += 1
            pt1 += 1

                    