class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        n = len(questions)
        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            points , brainpower = questions[i]
            memo[i] = max(points + dp(brainpower+i+1) , dp(i+1))
            return memo[i]
        return dp(0)
