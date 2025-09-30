class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []  # Store up to 3 suggestions at each node

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            # Add word to suggestions if fewer than 3, maintaining lexicographical order
            if len(node.suggestions) < 3 and word not in node.suggestions:
                node.suggestions.append(word)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort products to ensure lexicographical order in suggestions
        products.sort()
        
        # Build Trie
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        # Traverse Trie character by character for searchWord
        result = []
        node = trie.root
        for c in searchWord:
            # If character exists, move to next node and collect suggestions
            if c in node.children:
                node = node.children[c]
                result.append(node.suggestions)
            else:
                # If character doesn't exist, no further matches are possible
                node.children = {}  # Prevent further traversal
                result.append([])
            # For remaining characters, append empty lists
        result.extend([[] for _ in range(len(searchWord) - len(result))])
        
        return result