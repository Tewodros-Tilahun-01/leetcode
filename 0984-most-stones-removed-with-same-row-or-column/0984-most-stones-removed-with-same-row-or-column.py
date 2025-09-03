class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        rank = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 0
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
        
        for x, y in stones:
            row, col = f"r{x}", f"c{y}"
            union(row, col)
        
        groups = set(find(f"r{x}") for x, y in stones)
        return len(stones) - len(groups)