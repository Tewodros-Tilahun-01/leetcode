class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        i = 0
        d = len(s)
        for letter in s:
            if  letter =="I":
                res.append(i)
                i += 1
            else:
                res.append(d)
                d -= 1
        if letter =="I":
            res.append(i)
            i += 1
        else:
            res.append(d)
            d -= 1
        return res
