class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:return False
        if x == 0:return True
        y = ""
        z = x
        
        while z > 0:
            y += str(z % 10)
            z = z//10
        y = int(y)

        return y == x

