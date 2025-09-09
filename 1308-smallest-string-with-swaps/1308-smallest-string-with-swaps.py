class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Initialize Union-Find data structure
        parent = list(range(len(s)))
        
        def find(x: int) -> int:
            # Find root parent with path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int) -> None:
            # Unite two indices under same root
            parent[find(x)] = find(y)
        
        # Step 1: Build connected components using Union-Find
        for x, y in pairs:
            union(x, y)
        
        # Step 2: Group indices by their root parent
        groups = {}
        for i in range(len(s)):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)
        
        # Step 3: Convert string to list for manipulation
        result = list(s)
        
        # Step 4: For each group, sort characters and place in sorted order
        for indices in groups.values():
            # Get characters at these indices
            chars = [s[i] for i in indices]
            # Sort characters lexicographically
            chars.sort()
            # Place sorted characters back in their indices
            for i, char in zip(sorted(indices), chars):
                result[i] = char
        
        # Step 5: Convert back to string and return
        return ''.join(result)