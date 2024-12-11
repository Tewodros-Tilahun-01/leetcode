class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        part = []
        res = []
        temp = prv = 0
        for i in range(len(s)):
            if not s[i] in part:
                temp += count[s[i]]
                part.append(s[i])
            if temp == i  + 1:
                res.append(i + 1 - prv)
                part = []
                prv = i + 1
        return res