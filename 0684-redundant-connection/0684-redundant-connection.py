class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n)]
        rank = [0] * n
        def union(x,y):
            px = find(x)
            py = find(y)
            if px != py:
                if rank[px] > rank[py]:
                    parent[py] = px
                elif rank[py] < rank[px]:
                    parent[px] = py
                else:
                    parent[px] = py
                    rank[py] += 1
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        for i , j in edges:
            x ,y = i-1,j-1
            if find(x) == find(y):
                return [i,j]
            else:
                union(x,y)