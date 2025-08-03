class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        min_diff = float("inf")

        timePoints.sort()
        
        for i in range( len(timePoints) -1 ):
            hour1 , min1 = map( int,timePoints[i].split(":") )
            hour2 , min2 = map( int,timePoints[i+1].split(":") )
            diff = ( (hour2 - hour1) * 60 ) + min2 - min1    
            min_diff = min( min_diff , diff)


        hour1 , min1 = map( int,timePoints[0].split(":") )
        hour2 , min2 = map( int,timePoints[-1].split(":") )
        diff = (24 * 60 ) - (hour2 * 60 + min2) + hour1 * 60 + min1
        min_diff = min(min_diff , diff )

        return min_diff