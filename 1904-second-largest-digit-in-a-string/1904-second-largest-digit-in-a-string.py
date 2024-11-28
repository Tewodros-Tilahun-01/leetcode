class Solution:
    def secondHighest(self, s: str) -> int:
        res = []
        for i in s:
            if not i.isalpha() and int(i) not in res:
                res.append(int(i))
        res.sort()
        return res[-2] if len(res)>1 else -1
        
                

        
        