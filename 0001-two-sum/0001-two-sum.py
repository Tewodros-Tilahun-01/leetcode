class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            cp = target - nums[i]
            if cp in hashmap:
                return [hashmap[cp],i]
            hashmap[nums[i]] = i