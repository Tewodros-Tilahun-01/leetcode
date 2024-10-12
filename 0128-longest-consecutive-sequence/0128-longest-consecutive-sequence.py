class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxsize = 0
        currentsum = 0
        for i in sorted(set(nums)):
            if i - 1 in count:
                currentsum +=1
            else:
                currentsum = 1
            maxsize = max(maxsize,currentsum)
        return maxsize