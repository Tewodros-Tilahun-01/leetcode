class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        res = 0
        a = b = n//2
        index = 0
        costs.sort( key = lambda a:abs( a[0]-a[1] ) , reverse=True )
       
        while index < n:
            costA , costB = costs[index]
            if( costA < costB and a > 0 ) or b == 0:
                res += costA
                a -= 1
            else:
                res += costB
                b -= 1
            index += 1
        return res