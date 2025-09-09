class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = {}
        connected = defaultdict(list)
        def find(x):
            if x not in parent:
                parent[x] = x
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            px = find(x)
            py = find(y)
            if px != py:
                if s[px] < s[py]:
                    parent[py] = px
                else:
                    parent[px] = py

        for x , y in pairs:
            union(x,y)
        
        for i in range(n):
            connected[find(i)].append(s[i])
        
        for key ,value in connected.items():
            connected[key] = sorted(value,reverse=True)
        
        res = []
        for i in range(n):
            char = connected[find(i)].pop()
            res.append(char)

        return "".join(res)
