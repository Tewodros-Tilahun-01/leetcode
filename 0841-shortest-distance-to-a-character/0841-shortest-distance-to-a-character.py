class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        index = []
        res = [0] * len(s)
        for i in range(len(s)):
            if s[i] == c:
                index.append(i)
        for i in range(len(s)):
            if s[i] != c:
                ans =  min([abs(i - j) for j in index])
                res[i] = ans
        return res