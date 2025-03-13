class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:return stones[0] 
        max_heap = []
        for i in stones:
            heapq.heappush(max_heap, -i)
        while len(max_heap) > 1:
            heapq.heappush(max_heap, -(-heapq.heappop(max_heap) - -heapq.heappop(max_heap)))   
        return -max_heap[0] 


             