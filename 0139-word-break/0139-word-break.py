class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        i = 0 
        dp = [False] * (len(s)+1)
        dp[0] = True

        while i < len(s):
            
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word and dp[i] and not dp[i+len(word)]:
                    dp[i+len(word)] = True
            i += 1
        return dp[len(s)]