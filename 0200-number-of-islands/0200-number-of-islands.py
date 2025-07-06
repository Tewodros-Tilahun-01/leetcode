class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visted = set()
        max_row , max_col = len(grid) , len(grid[0])
        lands = 0
        def dfs(pos):
            row ,col = pos
            if (row,col) in visted:return 0
            if row < 0 or row >= max_row or col < 0 or col >= max_col or grid[row][col] == "0":
                return 0
           
            visted.add(pos)
            dfs((row+1,col))
            dfs((row-1,col))
            dfs((row,col+1))
            dfs((row,col-1))
            return 1

        for i in range(max_row):
            for j in range(max_col):
                if grid[i][j] == "1":
                    lands += dfs((i,j))
        return lands