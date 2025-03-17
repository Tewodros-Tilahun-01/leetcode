class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for i in nums:
            if len(q) < k:
                heappush(q,i)
            elif q[0] < i:
                heappop(q)
                heappush(q,i)
        return q[0]