class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary mapping char to TrieNode
        self.is_word = False  # Marks if this node ends a segment

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word
class Solution:
    def partitionString(self,s: str) -> list[str]:
        trie = Trie()
        segments = []
        current = ""

        for char in s:
            current += char
            if not trie.search(current):
                segments.append(current)
                trie.insert(current)
                current = ""

        return segments