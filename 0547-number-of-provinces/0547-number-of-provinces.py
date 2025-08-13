class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # Path compression
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px  # No need for rank — still O(α(n))

        # Union provinces
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    union(i, j)

        # Count distinct roots
        return sum(find(i) == i for i in range(n))
