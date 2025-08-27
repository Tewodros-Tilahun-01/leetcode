class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        rank = [0] * 26
        def find (x):
            while x != parent[x]:
                x = parent[x]
            return x
        def union(x,y):
            py = find(y)
            px = find(x)
            if py != px:
                if rank[px] > rank[py]:
                    parent[py] = px
                if rank[py] > rank[px]:
                    parent[px] = py
                else:
                    parent[px] = py
                    rank[px] += 1
        next_op = []
        for eq in equations:
            x , y = ord(eq[0])-97 , ord(eq[3])-97
            if eq[1] == "=":
                union(x,y)
            else:
                next_op.append((x,y))
        for x,y in next_op:
            if find(x) == find(y):
                return False
        return True