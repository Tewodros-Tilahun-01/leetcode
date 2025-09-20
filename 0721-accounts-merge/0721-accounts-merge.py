class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 0
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
                
        original_name = {}
        for a in accounts:
            name = a[0]
            for email in a[1:]:
                original_name[email] = name
        
        for a in accounts:
            email1 = a[1]
            for email2 in a[2:]:
                union(email1,email2)
        
        connected = defaultdict(list)
        for email in original_name:
            root = find(email)
            connected[root].append(email)
        
        res = []
        for root in connected:
            res.append([original_name[root]] + sorted(connected[root]))
        
        return res

