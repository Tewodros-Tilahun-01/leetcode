class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(row: int, col: int) -> bool:
            # If out of bounds or already visited/water, return False for boundary connection
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if grid[row][col] != 0:
                return True
            
            # Mark as visited by changing to water
            grid[row][col] = 1
            is_closed = True
            
            # Check all four directions
            for dx, dy in directions:
                if not dfs(row + dx, col + dy):
                    is_closed = False
                    
            return is_closed
        
        
        
        # Count closed islands
        islands = 0
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        islands += 1
                        
        return islands