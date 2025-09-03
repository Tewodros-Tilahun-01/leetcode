class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        for x, y in stones:
            row, col = f"r{x}", f"c{y}"
            union(row, col)
        
        groups = set(find(f"r{x}") for x, y in stones)
        return len(stones) - len(groups)