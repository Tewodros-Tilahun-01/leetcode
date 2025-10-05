class TrieNode:
    def __init__(self):
        self.children = {}
        self.largest = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        n = len(word)
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c] 
            node.largest = max(node.largest,n)
    def prifix(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c] 
        return True

        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        res = 0

        words.sort(key=lambda x:-(len(x)))

        for word in words:
            rev = word[::-1]
            if not trie.prifix(rev):
                trie.insert(rev)
                res += len(word) + 1

        return res
        
        
        