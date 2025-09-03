class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Initialize parent array for Union-Find (each character maps to itself initially)
        parent = list(range(26))  # 26 for lowercase letters a-z
        
        def find(x: int) -> int:
            # Find the root (representative) of the set containing x
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x: int, y: int):
            # Merge the sets of x and y, making the smaller character the representative
            px, py = find(x), find(y)
            if px < py:
                parent[py] = px
            else:
                parent[px] = py
        
        # Build equivalence classes by processing s1 and s2
        for c1, c2 in zip(s1, s2):
            # Convert characters to indices (a=0, b=1, ..., z=25)
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))
        
        # Construct the result by mapping each character in baseStr to the smallest in its class
        result = []
        for c in baseStr:
            # Find the smallest equivalent character (root of the set)
            smallest_char = chr(find(ord(c) - ord('a')) + ord('a'))
            result.append(smallest_char)
        
        return ''.join(result)