class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxSen = 0
        for i in sentences:
           maxSen = max(len(i.split()),maxSen)
        return maxSen