class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Initialize parent dictionary for union-find
        parent = {}
        
        def find(x):
            # Find the root of the set containing x with path compression
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            # Merge the sets containing x and y
            parent[find(x)] = find(y)
        
        # Step 1: Process all "==" equations to group equal variables
        for eq in equations:
            if eq[1] == '=':
                x, y = eq[0], eq[3]
                union(x, y)
        
        # Step 2: Check "!=" equations for conflicts
        for eq in equations:
            if eq[1] == '!':
                x, y = eq[0], eq[3]
                if find(x) == find(y):
                    return False
        
        return True