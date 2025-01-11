class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        s = deque(sandwiches)
        count = Counter(students)
        while len(s) and count[s[0]] > 0:  
            if s[0] == q[0]:
                count[ s.popleft() ] -= 1
                q.popleft()
            else:
                q.append(q.popleft())
        return len(s)