class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1)+1, len(s2)+1
        dp = [[-1] * (n) for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0:dp[i][j] = j  
                elif j == 0:dp[i][j] = i  
                
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[m-1][n-1]