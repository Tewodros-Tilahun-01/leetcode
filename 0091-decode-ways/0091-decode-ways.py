class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def rec(s):
            if len(s) > 0 and s[0] == "0":
                return 0
            if len(s) <= 1:
                return 1
            if s not in memo:
                memo[s] = rec(s[1:])
                memo[s] += rec(s[2:]) if int(s[:2]) < 27 and len(s) else 0
            return memo[s]
        
        return rec(s)