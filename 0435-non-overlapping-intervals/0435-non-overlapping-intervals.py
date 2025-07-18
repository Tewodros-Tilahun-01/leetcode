class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = float("-inf")
        res = 0
        intervals.sort(key=lambda x: x[1])
        for interval in intervals:

            if interval[0] < end:
                res += 1
            else:
                end = interval[1]
        return res