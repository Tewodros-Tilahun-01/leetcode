class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = Counter(nums)
        res = 0
        for i in nums:
            if i-diff in count and i + diff in count:
                res += 1
        return res