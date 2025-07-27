class Solution:
    def isHappy(self, n: int) -> bool:
        visted = set()
        while n > 1 and n not in visted:
            temp = 0
            visted.add(n)
            for _ in range(len(str(n))):
                temp += ( n % 10)*(n%10)
                n = n//10
            n = temp
        return True if n == 1 else False