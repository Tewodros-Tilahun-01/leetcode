class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0] * numCourses
        queue = collections.deque()
        result = []
        
        for c1, c2 in prerequisites:
            graph[c2].append(c1)
            incoming[c1] += 1
        
        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            result.append(course)
            for next_course in graph[course]:
                incoming[next_course] -= 1
                if incoming[next_course] == 0:
                    queue.append(next_course)
        
        return result if len(result) == numCourses else []