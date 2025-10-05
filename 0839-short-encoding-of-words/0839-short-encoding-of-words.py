from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.word_len = 0  # Store length of word ending here

        root = TrieNode()
        for word in words:
            node = root
            rword = word[::-1]
            for char in rword:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word_len = len(word)  # Mark word length at leaf

        def dfs(node, depth):
            total = 0
            if not node.children and node.word_len > 0:
                total += node.word_len + 1  # Add word length + '#'
            for child in node.children.values():
                total += dfs(child, depth + 1)
            return total

        return dfs(root, 0)