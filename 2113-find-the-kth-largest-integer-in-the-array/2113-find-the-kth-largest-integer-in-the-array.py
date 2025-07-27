class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [-int(val) for val in nums ]
        heapq.heapify(nums)
        largest = heapq.nsmallest(k,nums)
        return str(-largest[-1])