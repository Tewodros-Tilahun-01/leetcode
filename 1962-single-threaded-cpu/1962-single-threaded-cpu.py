class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks_w = []
        for i in range(n):
            eTime, pTime = tasks[i]
            tasks_w.append((eTime, pTime, i))
        tasks_w.sort()
        
        heap = []
        res = []
        current = tasks_w[0][0]
        idx = 0
        
        while len(res) < n:
            while idx < n and tasks_w[idx][0] <= current:
                eTime, pTime, index = tasks_w[idx]
                heapq.heappush(heap, (pTime, index))
                idx += 1
            
            if not heap:
                current = tasks_w[idx][0]
                continue
            
            pTime, index = heapq.heappop(heap)
            res.append(index)
            current += pTime
        
        return res