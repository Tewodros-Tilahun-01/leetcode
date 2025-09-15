class Solution:
    def isThree(self, n: int) -> bool:
        if n <= 3:
            return False

        sq = sqrt(n)
        if int(sq) != sq:
            return False

        d = 2
        while d * d <= sq:
            if sq % d == 0:
                return False
            d += 1
        
        return True
