class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initialize variables
        fresh_oranges = 0
        minutes = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        queue = deque()

        # Count fresh oranges and add rotten oranges to queue
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1

        # If no fresh oranges, return 0
        if fresh_oranges == 0:
            return 0

        # Check if a cell is a fresh orange
        def is_fresh(row, col):
            return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1

        # BFS to spread rot
        while queue and fresh_oranges > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    
                    if is_fresh(new_row, new_col):
                        fresh_oranges -= 1
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
            
            minutes += 1

        # Return -1 if fresh oranges remain, otherwise return minutes
        return -1 if fresh_oranges != 0 else minutes