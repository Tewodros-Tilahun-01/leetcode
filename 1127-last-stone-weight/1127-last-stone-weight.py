class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-val for val in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_big = -heapq.heappop(stones)
            second_big = -heapq.heappop(stones)
            if first_big > second_big:
                heapq.heappush(stones,-(first_big - second_big))
            if len(stones) == 0:
                stones.append(0)
        return -stones[0]


