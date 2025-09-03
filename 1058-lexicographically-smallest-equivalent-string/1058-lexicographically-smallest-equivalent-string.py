class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if px > py:
                px , py = py , px
            parent[py] = px
        n = len(s1)
        
        for c1, c2 in zip(s1, s2):
            union(c1, c2)
        
        res = []
        for s in baseStr:
            res.append(find(s))
        return "".join(res)
                