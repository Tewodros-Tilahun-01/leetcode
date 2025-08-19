class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dir = [(1,-1),(1,0),(1,1)]
        def isbound(row,col):
            if 0 <= row < n and 0 <= col < n:
                return True
            return False

        for i in range(n-2,-1,-1):
            for j in range(0,n):
                res = float("inf")
                for dx , dy in dir:
                    new_row , new_col = dx + i , dy + j
                    if isbound(new_row,new_col):
                        res = min( res ,matrix[i][j] + matrix[new_row][new_col])
                matrix[i][j] = res
        return min(matrix[0])