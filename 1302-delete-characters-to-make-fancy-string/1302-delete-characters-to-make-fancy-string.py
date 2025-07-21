class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        res = s[:2]
        for i in range(2,len(s)):
            if s[i-1] == s[i-2] == s[i]:
                continue
            else:
                res += s[i]
        return res