class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end += 1
        

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        res = 0
        trie = Trie()
        for word in words:
            trie.insert(word)

        for char, child in trie.root.children.items():
            waiting[char].append(child)

        for c in s:
            if c in waiting:
                current = waiting[c]
                waiting[c] = []
                for node in current:
                    res += node.end
                    for next_c, child in node.children.items():
                        waiting[next_c].append(child)
        return res
            
        
