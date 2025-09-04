class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols + 1)  # +1 for boundary node
        boundary_node = rows * cols  # Special node for boundary
        
        # Directions for adjacent cells (right, down to avoid redundant unions)
        directions = [(0, 1), (1, 0)]
        
        # Step 1: Union all adjacent land cells and connect boundary lands to boundary_node
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:  # Skip water
                    continue
                cell = i * cols + j
                # If on boundary, connect to boundary_node
                if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                    uf.union(cell, boundary_node)
                # Connect to right and down neighbors if they are land
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if ni < rows and nj < cols and grid[ni][nj] == 0:
                        uf.union(cell, ni * cols + nj)
        
        # Step 2: Count unique components not connected to boundary
        component_parents = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    continue
                cell = i * cols + j
                parent = uf.find(cell)
                if parent != uf.find(boundary_node):  # Not connected to boundary
                    component_parents.add(parent)
        
        return len(component_parents)