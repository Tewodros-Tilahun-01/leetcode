class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def prifix(self, word: str) -> bool:
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                return False
            node = node.children[char]
            if i < len(word) - 1 and not node.is_end:
                return False
        return True
class Solution:
    def longestWord(self,words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        words.sort(key=lambda x: (-len(x), x))
        for word in words:
            if trie.prifix(word):
                return word
        return ""