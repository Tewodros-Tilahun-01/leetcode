class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count1 = Counter(s)
        count2 = Counter(t)
        res = 0
        for i in count1:
            if count1[i] > count2[i]:
                res += count1[i] - count2[i]
        return res