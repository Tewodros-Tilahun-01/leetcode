class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        def gcf(m,n):
            if n == 0:return m
            return gcf(n,m%n)

        def lcm(n,m):
           return( m * n )  // gcf(m,n)      

        for i in range(n):
            _lcm = nums[i]
            for j in range(i,n):
                _lcm = lcm(_lcm,nums[j]) 
                if _lcm == k:
                    count += 1
                elif _lcm > k:
                    break
        
        return count
