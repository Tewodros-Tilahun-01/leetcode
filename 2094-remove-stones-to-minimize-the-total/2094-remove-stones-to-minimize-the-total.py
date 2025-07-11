class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-val for val in piles]
        heapq.heapify(piles)

        for _ in range(k):
            largest = math.ceil(-heappop(piles) / 2)
            heappush(piles,-largest)
        return -sum(piles)