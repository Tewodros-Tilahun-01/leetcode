class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = 0
        for val in nums:
            result ^= val
        
        diff_bit = result & -result
        
        first, second = 0, 0
        for val in nums:
            if val & diff_bit:
                first ^= val
            else:
                second ^= val
        
        return [first, second]