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
                parent[px] = py
            else:
                parent[py] = px
        n = len(s1)
        
        for i in range(n):
            union(s1[i],s2[i])
        
        res = []
        for s in baseStr:
            res.append(find(s))
        return "".join(res)
                