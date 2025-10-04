class TrieNode:
    def __init__(self):
        self.children = {}
        self.indices = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, substr: str, index: int):
        node = self.root
        for char in substr:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.indices.add(index)
    
    def get_indices(self, substr: str) -> set:
        node = self.root
        for char in substr:
            if char not in node.children:
                return set()
            node = node.children[char]
        return node.indices

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        trie = Trie()
        
        # Insert all substrings into the Trie
        for i in range(n):
            string = arr[i]
            m = len(string)
            for length in range(1, m + 1):
                for start in range(m - length + 1):
                    substr = string[start:start + length]
                    trie.insert(substr, i)
        
        res = [""] * n
        for i in range(n):
            string = arr[i]
            m = len(string)
            best_substr = None
            
            # Try each length starting from 1
            for length in range(1, m + 1):
                # Check each substring of this length
                for start in range(m - length + 1):
                    substr = string[start:start + length]
                    indices = trie.get_indices(substr)
                    if len(indices) == 1 and i in indices:
                        # Found a unique substring
                        if best_substr is None or substr < best_substr:
                            best_substr = substr
                # If a valid substring is found, no need to check longer lengths
                if best_substr:
                    res[i] = best_substr
                    break
        
        return res