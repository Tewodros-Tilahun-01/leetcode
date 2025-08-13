class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        def dfs(i,graph,color):
            if colors[i] != 0:
                return colors[i] == color

            colors[i] = color
            for nb in graph[i]:
                c = 2 if color == 1 else 1
                if not dfs(nb,graph,c):
                    return False
            return True

        for i in range(n):
            if colors[i] == 0 and not dfs(i,graph, 1):
                return False
        return True

            

