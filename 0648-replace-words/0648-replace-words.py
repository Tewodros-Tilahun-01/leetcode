class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        for c in word:
            index = ord(c) - ord("a")
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end = True
    def change_to_root(self,word):
        node = self.root
        root_word = []
        for c in word:
            index = ord(c) - ord("a")
            if not node.children[index]:
                return word
            root_word.append(c)
            node = node.children[index]
            if node.is_end:return "".join(root_word)
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        res = []
        for word in dictionary:
            trie.insert(word)

        for word in sentence.split():
            res.append(trie.change_to_root(word))
        
        return " ".join(res)
