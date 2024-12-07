class Solution:
    def captureForts(self, forts: List[int]) -> int:
        res = pt2 = 0
        for pt1 ,value in enumerate(forts):
            if value:
                if forts[pt2] == -value:
                    res = max(res,pt1-pt2-1)
                pt2 = pt1
        return res