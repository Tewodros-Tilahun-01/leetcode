
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ref = defaultdict(list)
        path = set()
        visited = set() 
        for course, prereq in prerequisites:
            ref[course].append(prereq)

        def dfs(cor):
            if cor in path:return False
            if cor in visited:return True
            path.add(cor)
            for prereq in ref[cor]:
                if not dfs(prereq):return False
            path.remove(cor)
            visited.add(cor)
            return True
        
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):return False
        
        return True