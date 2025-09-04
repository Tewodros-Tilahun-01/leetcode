class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)     

        for i in range(n-1,-1,-1):
            points , brainPower = questions[i]
            dp[i] = points
            next_indx = i+brainPower+1
            if next_indx < n:
                dp[i] = max(dp[i] ,points + dp[next_indx])
            dp[i] = max(dp[i],dp[i+1])
        return max(dp)
