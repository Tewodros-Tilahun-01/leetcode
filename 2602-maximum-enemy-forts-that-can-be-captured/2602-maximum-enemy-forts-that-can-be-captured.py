class Solution:
    def captureForts(self, forts: List[int]) -> int:
        pt1 , pt2 = 0,0
        max_num = 0
        for i in range(len(forts)):
            if forts[i] == 1:
                pt1 = i
            if forts[i] == -1:
                pt2 = i
            if forts[pt1] == 1 and forts[pt2] == -1:
                max_num = max(max_num,abs(pt1 - pt2) -1)
                pt1 = i
                pt2 = i
        return max_num
