class Solution:
    def arrangeCoins(self, n: int) -> int:
        row=1
        res=1
        while res<=n:
            res=res+row+1
            row+=1
        return row-1