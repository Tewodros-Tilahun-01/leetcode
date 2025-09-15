class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_element , max_element = min(nums) , max(nums)

        def gcd(n,m):
            if m == 0:
                return n
            return gcd(m,n%m)
        
        return gcd(min_element,max_element)