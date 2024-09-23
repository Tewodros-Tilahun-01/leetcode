class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        size = len(nums)
        count = 0
        for i in range(size):
            for j in range(size):
                if i != j and nums[i] + nums[j] == target:
                    count += 1

        return count