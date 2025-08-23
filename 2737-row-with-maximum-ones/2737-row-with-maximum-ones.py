class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        res = [0,0]
        for i in range(row):
            count = 0
            for j in range(col):
                if mat[i][j] == 1:
                    count += 1
            if res[1] < count:
                res = [i,count]
        return res