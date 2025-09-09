class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_orange = 0
        min_minutes = 0
        rows , cols = len(grid) , len(grid[0])
        directions = [(0,1),(0,-1),(-1,0),(1,0)]

        def isFresh(row,col):
            return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1
        def bfs(queue):
            nonlocal fresh_orange , min_minutes
            while queue:
                for _ in range(len(queue)):
                    row , col = queue.popleft()
                    
                    for dx , dy in directions:
                        new_row , new_col = row + dx , col + dy
                        
                        if isFresh(new_row , new_col):
                            fresh_orange -= 1
                            grid[new_row][new_col] = 2
                            queue.append((new_row,new_col))
                    
                min_minutes += 1
                if fresh_orange == 0:
                        break
            
        
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_orange += 1
        
        if fresh_orange == 0:
            return 0
        bfs(queue)
        return -1 if fresh_orange != 0 else min_minutes
        