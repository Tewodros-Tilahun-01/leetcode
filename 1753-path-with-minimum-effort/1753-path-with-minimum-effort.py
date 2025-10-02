class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        processed = set()
        heap = [(0,0,0)]
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(heights)
        cols = len(heights[0])

        while heap:
            effort, row ,col = heapq.heappop(heap)
            if (row,col) in processed:
                continue
                
            processed.add((row,col))

            if row == rows-1 and col == cols-1:
                return effort

            for dx, dy in dir:
                new_row, new_col = row + dx, col + dy
                if (0 <= new_row < rows and 
                    0 <= new_col < cols and 
                    (new_row, new_col) not in processed):
                    new_effort = abs(heights[new_row][new_col] - heights[row][col])
                    new_effort = max(effort, new_effort)
                    heapq.heappush(heap, (new_effort, new_row, new_col))
                
        return 0
