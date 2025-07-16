class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        heapq.heapify(arr)
        for outside in matrix:
            for inside in outside:
                heapq.heappush(arr,inside)
        res = heapq.nlargest(len(arr) - k + 1,arr)
        return res[-1]
