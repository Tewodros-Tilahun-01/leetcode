class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        root = TrieNode()

        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]

        node = root
        n = len(target)
        dp = [float("inf")] * (n+1)
        dp[n] = 0
        
        for i in range(n-1,-1,-1):
            node = root
            for j in range(i,n):
                char = target[j]
                if char not in node.children:
                    break
                node = node.children[char]
                dp[i] = min(dp[i],dp[j+1]+1)
            
        return -1 if dp[0] == float("inf") else dp[0]