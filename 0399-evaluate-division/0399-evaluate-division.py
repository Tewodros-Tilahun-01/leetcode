class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1.0 / values[i]))
        
        def dfs(curr, dest, seen):
            if curr not in graph or dest not in graph:
                return -1.0
            if curr == dest:
                return 1.0
            seen.add(curr)
            for nxt, val in graph[curr]:
                if nxt not in seen:
                    res = dfs(nxt, dest, seen)
                    if res != -1.0:
                        return val * res
            return -1.0
        
        res = []
        for curr, dest in queries:
            res.append(dfs(curr, dest, set()))
        return res
        