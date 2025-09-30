class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u , v , cost in times:
            graph[u-1].append((v-1,cost))
        
        visited = set()
        time = [float("inf") for node in range(n)]
        time[k-1] = 0
        heap  = [(0,k-1)]

        while heap:
            cost , curr = heapq.heappop(heap)
            
            if curr in visited:
                continue

            visited.add(curr)

            for nb , weight in graph[curr]:
                curr_time = weight + cost
                if curr_time < time[nb]:
                    time[nb] = curr_time 
                    heapq.heappush(heap,(curr_time,nb))
                    
        res = max(time)
        return -1 if res == float("inf") else res