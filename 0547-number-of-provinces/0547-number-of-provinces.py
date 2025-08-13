class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [0] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]

        def union(x,y):
            px = find(x)
            py = find(y)
            if px != py:
                if rank[px] > rank[py]:
                    parent[py] = px
                elif rank[py] > rank[px]:
                    parent[px] = py
                else:
                    parent[px] = py
                    rank[py] += 1
            
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    union(i,j)
                    
        provinces = set()
        for child in parent:
            provinces.add(find(child))
        return len(provinces)