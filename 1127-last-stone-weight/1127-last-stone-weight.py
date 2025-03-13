class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:return stones[0] 
        max_heap = []
        for i in stones:
            heapq.heappush(max_heap, -i)
        while len(max_heap) > 1:
            largest1 = -heapq.heappop(max_heap)
            largest2 = -heapq.heappop(max_heap)
            if largest1 != largest2:
                heapq.heappush(max_heap, -(largest1 - largest2))
        return -max_heap[0] if len(max_heap) == 1 else  0


             