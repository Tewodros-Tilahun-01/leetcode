class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        change_to_index = {}
        for index, value in enumerate(intervals):
            start, _ = value
            change_to_index[start] = index
        
        intervals.sort()
        
        n = len(intervals)
        res = [-1] * n
        
        for i in range(n):
            start, end = intervals[i]
            original_index = change_to_index[start]
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if intervals[mid][0] >= end:
                    right = mid
                else:
                    left = mid + 1
            if left < n:
                res[original_index] = change_to_index[intervals[left][0]]
                
        return res