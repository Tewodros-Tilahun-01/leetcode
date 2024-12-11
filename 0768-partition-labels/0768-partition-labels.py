class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        part = set()
        res = []
        temp = 0
        for i in range(len(s)):
            if not s[i] in part:
                temp += count[s[i]]
                part.add(s[i])
            if temp == i  + 1:
                res.append(i+1-sum(res))
                part = set()  
            print(part,temp) 
        return res