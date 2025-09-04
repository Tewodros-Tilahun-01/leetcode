class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        visted = set()
        max_row , max_col = len(grid) , len(grid[0])
        def isBound(row,col):
            if 0 <= row < max_row and 0 <= col < max_col:
                return True
            else:
                return False
        def dfs(row,col):
            if not isBound(row,col):
                return False
            if grid[row][col] == 1:
                return True
            
            visted.add((row,col))
            valid = True
            for dx , dy in dir:
                r , c = dx + row , dy + col
                if (r,c) not in visted and not dfs(r,c):
                        valid = False
            return valid

        islands = 0
        for i in range(max_row):
            for j in range(max_col):
                if (i,j) not in visted and grid[i][j] == 0 and dfs(i,j):
                    islands += 1
        return islands