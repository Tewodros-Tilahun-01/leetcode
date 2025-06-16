class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for j in range(left,right + 1):
            flag = False
            for ayy in ranges:
                if ayy[1] >= j and ayy[0] <= j:
                    flag = True
                    break
            if not flag:
                return False
        return True