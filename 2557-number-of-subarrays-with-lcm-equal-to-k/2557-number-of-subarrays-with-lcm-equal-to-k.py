class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        def gcf(m,n):
            if n == 0:return m
            return gcf(n,m%n)

        def lcm(n,m):
            if n >= m and n % m == 0:return n
            elif n < m and m % n == 0:return m
            else:return( m * n )  // gcf(m,n)      

        for i in range(n):
            _lcm = nums[i]
            for j in range(i,n):
                _lcm = lcm(_lcm,nums[j]) 
                if _lcm == k:
                    count += 1
                elif _lcm > k:
                    break
        
        return count
