class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        grid = []
        for i in range(rowIndex+1):
            row = [0 for _ in range(i+1)]
            grid.append(row)
            row[0] = row[-1] = 1

        for i in range(2,rowIndex+1):
            n = len(grid[i])
            for j in range(1,n-1):
                grid[i][j] = grid[i-1][j-1] + grid[i-1][j]

        return grid[-1]