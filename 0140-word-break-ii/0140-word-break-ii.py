class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = {len(s): [""]}
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        for start in range(len(s)-1,-1,-1):
            valid_sentence = []
            node = trie.root

            for end in range(start,len(s)):
                char = s[end]
                if char not in node.children:
                    break
                node = node.children[char]
                
                if node.isEnd:
                    current_word = s[start:end + 1]
                    for next_sentence in dp[end + 1]:
                        if next_sentence:
                            valid_sentence.append(current_word + " " + next_sentence)
                        else:
                            valid_sentence.append(current_word)
             
            dp[start] = valid_sentence

        return dp[0]


