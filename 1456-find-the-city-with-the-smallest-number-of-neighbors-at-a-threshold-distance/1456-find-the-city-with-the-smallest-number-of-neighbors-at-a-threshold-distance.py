class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float("inf")] * n for _ in range(n)]

        for u , v ,w in edges:
            dist[u][v] = dist[v][u] = w
        
        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j],dist[k][j] + dist[i][k])

        _min = float("inf")
        res = 0
        for i in range(n):
            count = sum([1 for j in range(n) if dist[i][j] <= distanceThreshold ])
            if count <= _min:
                _min = count
                res = i

        return res