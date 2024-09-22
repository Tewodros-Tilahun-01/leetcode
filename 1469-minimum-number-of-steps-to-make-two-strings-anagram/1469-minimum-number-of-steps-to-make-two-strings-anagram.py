class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount = Counter(s)
        tCount = Counter(t)
        res = 0
        for i in sCount:
            if i not in tCount:
                res += sCount[i]
            elif sCount[i] > tCount[i] :
                res += sCount[i] - tCount[i]
        return res