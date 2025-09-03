class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Initialize parent array for Union-Find (for characters 'a' to 'z')
        parent = list(range(26))
        
        def find(x: int) -> int:
            # Find the root (representative) of the set containing x
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x: int, y: int):
            # Union two characters, making the smaller one the parent
            px, py = find(x), find(y)
            if px < py:
                parent[py] = px
            else:
                parent[px] = py
        
        # Build equivalence groups by unioning characters from s1 and s2
        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))
        
        # Transform baseStr by mapping each character to the smallest equivalent
        result = []
        for c in baseStr:
            smallest_char = chr(find(ord(c) - ord('a')) + ord('a'))
            result.append(smallest_char)
        
        return ''.join(result)