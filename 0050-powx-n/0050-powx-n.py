class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        def rec(x,n):
            print(x,n)
            if n == 1 :
                return x
            if n == -1:
                return 1/x
          
            if n % 2 == 0:
                val = rec(x,n//2) 
                return val * val
            elif n > 0:
                return x * rec(x,n-1)
            if n < 0:
                return 1/x * rec(x,n+1)
        return rec(x,n)


            