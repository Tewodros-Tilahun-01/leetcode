class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        change_to_index = {}
        for index ,value in enumerate(intervals):
            start ,end = value
            change_to_index[start] = index

        intervals.sort(reverse=True)
        def find(start,prvStart):
            change_to_index[start]
        res = [0] * n
        for i in range(n):
            start , end = intervals[i]
            original = change_to_index[start]
            if start == end:
                res[original] = original 
            elif i == 0:
                res[original] = -1
            else:
                j = i - 1
                prvstart = None
                while j >= 0:
                    prvstart = intervals[j][0]
                    if prvstart >= end:
                        break
                    j -= 1
                res[original] = change_to_index[prvstart] if j >= 0 else -1
        return res
                
            
        


        