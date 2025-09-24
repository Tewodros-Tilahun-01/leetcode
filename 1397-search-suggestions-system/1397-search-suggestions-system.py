class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggested = []
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.suggested.append(word)
            
            
    def suggest(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                return []
            node = node.children[c]
        return node.suggested[:3]
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()

        for product in products:
            trie.insert(product)
        
        res = []
        for i in range(len(searchWord)):
            res.append(trie.suggest(searchWord[:i+1]))
        
        return res

