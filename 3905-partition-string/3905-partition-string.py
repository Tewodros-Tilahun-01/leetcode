class TrieNode:
    def __init__(self):
        self.children = {}
class Solution:
    def partitionString(self,s: str) -> list[str]:

        seen = set()
        segments = []
        current = ""

        for char in s:
            current += char
            if current not in seen:
                segments.append(current)
                seen.add(current)
                current = ""

        return segments