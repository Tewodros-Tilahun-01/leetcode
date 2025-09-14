class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True for _ in range(n)]
        is_prime[0] = is_prime[1] = False
        d = 2

        while d * d <= n-1:
            if is_prime[d]:
                i = d * 2
                while i <= n-1:
                    is_prime[i] = False
                    i += d
            d += 1

        return len([i for i in range(n) if is_prime[i]])
        
