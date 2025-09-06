class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        max_coin = 0
        bob = (n // 3)
        for i in range(bob,n-1,2):
            max_coin += piles[i]
        return max_coin
