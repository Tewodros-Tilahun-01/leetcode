class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_palindrome(x):
            if x < 0:
                return False
            reversed_num = 0
            temp = x
            while temp > 0:
                reversed_num = reversed_num * 10 + temp % 10
                temp //= 10
            return reversed_num == x
        
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        while True:
            if is_palindrome(n) and is_prime(n):
                return n
            n += 1
            if 10**7 < n < 10**8:
                n = 10**8