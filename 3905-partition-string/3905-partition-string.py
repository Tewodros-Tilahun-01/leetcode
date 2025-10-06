class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Solution:
    def partitionString(self, s: str) -> List[str]: 
        res = []
        root = TrieNode()

        start = 0
        while start < len(s):
            end = start
            node = root
            while end < len(s) and s[end] in node.children:
                node = node.children[s[end]]
                end += 1
            if end == len(s):break

            node.children[s[end]] = TrieNode()
            res.append(s[start:end+1])
            start = end + 1
            
        return res
