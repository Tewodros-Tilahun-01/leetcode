class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in redEdges:
            graph[u].append((v, True))
        for u, v in blueEdges:
            graph[u].append((v, False))
        
        res = [-1] * n
        res[0] = 0
        q = deque([(0, None)])
        visited = set([(0, None)])
        
        dist = 0
        while q:
            for _ in range(len(q)):
                node, prev_color = q.popleft()
                
                for neighbor, edge_color in graph[node]:
                    if (prev_color is None or edge_color != prev_color) and (neighbor, edge_color) not in visited:
                        visited.add((neighbor, edge_color))
                        q.append((neighbor, edge_color))
                        if res[neighbor] == -1:
                            res[neighbor] = dist + 1
            dist += 1
        
        return res