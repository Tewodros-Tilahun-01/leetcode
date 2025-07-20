class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])

        last_end = float("-inf")
        count = 0    

        for start , end in points:
            if start > last_end:
                count += 1
                last_end = end
        
        return count

