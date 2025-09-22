class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        parent = {}
        rank = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 0
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                if rank[px] > rank[py]:
                    parent[py] = px
                elif rank[px] < rank[py]:
                    parent[px] = py
                else:
                    parent[px] = py
                    rank[py] += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    union(f"row{i}", f"col{j}")
        

        connection = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    root = find(f"row{i}")
                    connection[root] += 1
        
        count = 0
        for group_size in connection.values():
            if group_size > 1:
                count += group_size
        
        return count