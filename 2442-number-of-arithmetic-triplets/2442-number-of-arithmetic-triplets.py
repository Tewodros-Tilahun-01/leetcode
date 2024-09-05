class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        check = set(nums)
        count = 0
        for i in nums:
            if i - diff in check and i + diff in check:
                count += 1
        return count