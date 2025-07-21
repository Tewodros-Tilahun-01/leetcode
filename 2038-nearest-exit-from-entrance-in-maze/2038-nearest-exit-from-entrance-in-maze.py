class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        max_row = len(maze)
        max_col = len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = {(entrance[0], entrance[1])}
        q = collections.deque()
        q.append((*entrance,0))

        while q:
            row,col,steps  = q.popleft()

            if (row == 0 or row == max_row - 1 or col == 0 or col == max_col - 1) and [row, col] != entrance:
                return steps
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (0 <= new_row < max_row and 0 <= new_col < max_col and 
                maze[new_row][new_col] == '.' and 
                (new_row, new_col) not in visited):
                
                    q.append((new_row, new_col, steps + 1))
                    visited.add((new_row, new_col))

        return -1