from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        heights = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()
        
        # Initialize water cells and queue
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    heights[i][j] = 0
                    queue.append((i, j))
        
        # Directions for adjacent cells (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # BFS to assign heights
        while queue:
            row, col = queue.popleft()
            current_height = heights[row][col]
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                # Check if the new position is valid and can be updated
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if heights[new_row][new_col] > current_height + 1:
                        heights[new_row][new_col] = current_height + 1
                        queue.append((new_row, new_col))
        
        return heights