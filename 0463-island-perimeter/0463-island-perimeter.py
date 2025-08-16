class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(row,col,visited):
            if row < 0 or row >= len(grid) or \
            col < 0 or col >= len(grid[0]) or \
            grid[row][col] == 0:
                return 1
                
            visited.add((row,col))
            perimeter = 0
            for r , c in dir:
                new_row , new_col = row + r , col + c
                if (new_row,new_col) not in visited:
                    perimeter += dfs(new_row,new_col,visited)
            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j,set())