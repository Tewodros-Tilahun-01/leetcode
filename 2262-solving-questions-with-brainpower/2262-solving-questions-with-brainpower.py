class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # dp[i] represents max points from index i onward
        
        for i in range(n - 1, -1, -1):
            points, jump = questions[i]
            next_question = min(n, i + jump + 1)  # Next valid index after jump
            dp[i] = max(points + dp[next_question], dp[i + 1])  # Take current or skip
            
        return dp[0]