class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {}
        res = nums[:]
        nums.sort()
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = i
        for i in range(len(res)):
            res[i] = count[res[i]]
        return res