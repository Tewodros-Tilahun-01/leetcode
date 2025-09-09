class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))  
        rank = [0] * n  

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]

        def union(x,y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1

        for x , y in pairs:
            union(x,y)
        
        connected = defaultdict(list)
        for i in range(n):
            connected[find(i)].append(s[i])
        
        for root in connected:
            connected[root].sort(reverse=True)
        
        res = []
        for i in range(n):
            char = connected[find(i)].pop()
            res.append(char)

        return "".join(res)
