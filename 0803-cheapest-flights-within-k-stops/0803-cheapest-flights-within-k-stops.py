class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prv = [float("inf")] * n
        prv[src] = 0

        for _ in range(k+1):
            curr = prv[:]

            for u , v , price in flights:
                curr[v] = min(curr[v],prv[u] + price)

            prv = curr[:]
        
        return -1 if curr[dst] == float("inf") else curr[dst]