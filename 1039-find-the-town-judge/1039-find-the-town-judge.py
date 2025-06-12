class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return n
        inside = defaultdict(int)
        outside = defaultdict(int)
        for i in trust:
            inside[i[0]] += 1
            outside[i[1]] += 1
        for i in range(1,n+1):
            if i not in inside and i in outside and outside[i] == n-1:
                return i
        return -1