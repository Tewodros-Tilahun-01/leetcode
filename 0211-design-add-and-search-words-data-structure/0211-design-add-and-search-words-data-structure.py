class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i == len(word):
                print(node.is_end)
                return node.is_end
            
            char = word[i]
            if char == ".":
                for key in node.children:
                    if dfs(node.children[key],i+1):
                        return True
                return False
            elif char in node.children:
                return dfs(node.children[char],i+1)
            else:
                return False
            

        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)