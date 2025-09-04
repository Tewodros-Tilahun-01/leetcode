class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = list(range(n+1))
        print(parent)
        def union(x,y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[px] = py
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for a , c , dist in roads:
            union(a,c)

        min_distance = float("inf")
        for a , c , dist in roads:
            if find(n) == find(a):
                min_distance = min(min_distance , dist)
        return min_distance