class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
    
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            px = find(x)
            py = find(y)
            if px == py:
                return False
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[py] < rank[py]:
                parent[px] = py
            else:
                parent[px] = py
                rank[py] += 1
            return True
                


        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))
    
        edges.sort()
        total_cost = 0
        edges_used = 0
        
        for cost, u, v in edges:
            if union(u, v):
                total_cost += cost
                edges_used += 1
                if edges_used == n - 1:  
                    break
        
        return total_cost
