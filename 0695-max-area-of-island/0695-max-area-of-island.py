class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        dr = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        max_row = len(grid)
        max_col = len(grid[0])
        def dfs(row,col,grid):
            nonlocal dr
            if grid[row][col] == 0:
                return 0
            visited.add((row,col))
            count = 0
            if grid[row][col]:count += 1
            for r , c in dr:
                new_row = r + row
                new_col = c + col
                if (new_row,new_col) not in visited and \
                0 <= new_row < max_row and \
                0 <= new_col < max_col: \
                   count += dfs(new_row,new_col,grid)
            return count

        for i in range(max_row):
            for j in range(max_col):
                if (i,j) not in visited:
                   res = max(res,dfs(i,j,grid)) 

        return res
