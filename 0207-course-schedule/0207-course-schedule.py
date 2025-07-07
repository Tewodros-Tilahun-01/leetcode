
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ref = defaultdict(list)
        visited = set() 
        for course, prereq in prerequisites:
            ref[course].append(prereq)

        def dfs(course):
            if course in visited:return False
            visited.add(course)
            for prereq in ref[course]:
                if not dfs(prereq):
                    return False
            ref[course] = []
            visited.remove(course)
            return True
        
        for course in range(numCourses):
            if course not in visited and not dfs(course):return False
        
        return True