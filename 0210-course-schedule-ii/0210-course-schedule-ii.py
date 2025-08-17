class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        incoming = [0 for i in range(numCourses)]
        res = []
        
        for c1 , c2 in prerequisites:
            incoming[c1] += 1
            graph[c2].append(c1)
        q = collections.deque([i for i in range(len(incoming)) if incoming[i] == 0])

        while q:
            print(q)

            course = q.popleft()
            res.append(course)
            for i in graph[course]:
                incoming[i] -= 1
                if incoming[i] == 0:
                    q.append(i)
        
        if len(res) == numCourses:
            return res
        return []


