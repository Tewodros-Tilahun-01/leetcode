class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = {node:[] for node in range(n)}

        for i in range(len(edges)):
            graph[edges[i][0]].append( (edges[i][1],-succProb[i]) )
            graph[edges[i][1]].append( (edges[i][0],-succProb[i]) )

        heap = [(-1,start_node)]
        probabilities = [2] * n
        processed = set()

        while heap:
            prb , curr_node = heapq.heappop(heap)
            if curr_node in processed:
                continue
            processed.add(curr_node)

            for nb , w in graph[curr_node]:
                if -(w * prb) < probabilities[nb]:
                    probabilities[nb] = -(w*prb)
                    heapq.heappush(heap,( (-(w*prb),nb) ))
                    
        return -probabilities[end_node] if  probabilities[end_node] != 2 else 0 
