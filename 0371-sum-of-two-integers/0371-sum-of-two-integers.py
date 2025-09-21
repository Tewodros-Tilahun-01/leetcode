class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            carry = (a & b) << 1
            a = (a ^ b) & 0xFFFFFFFF
            b = carry & 0xFFFFFFFF
            
        return a if a <= 0x7FFFFFFF else a - (1 << 32)
