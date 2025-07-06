class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visted = set()
        for v,u in edges:
            graph[v].append(u)
            graph[u].append(v)

        def dfs(node):
            if node == destination:
                return True
            visted.add(node)
            for nb in graph[node]:
                if nb not in visted and dfs(nb):
                    return True
            return False
        return dfs(source)

