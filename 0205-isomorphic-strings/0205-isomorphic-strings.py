class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s ) != len(t):
            return False
        rep = {}
        rep2 = {}
        for i in range(len(s)):     
            if s[i] not in rep:
                rep[s[i]] = t[i]
            elif rep[s[i]] != t[i]:
                return False
            if t[i] not in rep2:
                rep2[t[i]] = s[i]
            elif rep2[t[i]] != s[i]:
                return False
            
        return True