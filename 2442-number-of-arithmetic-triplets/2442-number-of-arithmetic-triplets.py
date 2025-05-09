class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        numMap = set(nums)
        count = 0
        for i in nums: 
            if i + diff in numMap and i - diff in numMap:
                count += 1
        return count