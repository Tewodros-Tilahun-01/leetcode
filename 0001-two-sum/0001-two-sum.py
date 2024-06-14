class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        size = len(nums)
        for index in range(size):
                count[nums[index]] = index
        for i in range(size):
            c = target - nums[i]
            if c in count and i != count[c]:
                return [i,count[c]]
        