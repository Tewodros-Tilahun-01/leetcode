class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        s = deque(sandwiches)
        count = Counter(students)
        while len(s) and s[0] in q:  
            if s[0] == q[0]:
                s.popleft()
                q.popleft()
            else:
                q.append(q.popleft())
        return len(q)