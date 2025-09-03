class Solution:
    def minSteps(self,n: int) -> int:
        if n == 1:
            return 0
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n //= d
            d += 1
            if d * d > n:
                if n > 1:
                    ans += n  # n is prime
                break
        return ans